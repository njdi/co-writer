# Pydantic 修好了我的 Agent 的记忆

**作者：** Akshay ([@akshay_pachaar](https://x.com/akshay_pachaar))  
**日期：** 2026年5月26日  
**来源：** [Pydantic fixed my Agent's Memory](https://x.com/akshay_pachaar/status/2058976178908885210)

你的 agent 记住了一切，却什么都不理解。

Agent 记忆始于向量数据库。把事实存为块（chunk），按相似度检索。

它一直能用，直到某个查询需要跨块连接事实。然后它就崩溃了。问题不在相似度，而在结构。

知识图谱曾是修复方案。实体作为节点，关系作为边，用遍历代替匹配。

但大多数团队撞上了另一堵墙。

当你给 agent 一个知识图谱作为记忆时，默认行为是：负责抽取的 LLM 自己决定结构。

它挑选实体类型、关系标签和属性。

结果是通用化的。

举个例子，你在构建一个客户支持 agent。你喂给它 50 段支持对话，涵盖客户、工单、功能和升级历史。

你问：“哪些企业客户有未解决的 sev-1 工单？”

图谱里有这些数据。但每个支持工单都被存为一个“Topic”节点。每个客户都是一个“Object”。每个关系都是“RELATES_TO”。

没有办法按类型、严重程度或套餐等级过滤。查询返回的是噪声。

agent 什么都没忘。是没人告诉它该关注什么。

![](images/img-01.jpg)

修复很直接：预先定义 schema。告诉抽取模型你的领域里存在哪些类型的实体，哪些关系是有效的，每个实体携带哪些属性。

那个组织蓝图叫做本体（ontology）。把它想象成你 agent 大脑的 schema。

让我们走一遍：为什么这很重要，没有它会出什么问题，以及如何用一个 100% 开源的方案来实现它。

## 为什么扁平检索在多跳推理上会失败

基于向量的记忆把事实存为文本块，按语义相似度检索。这在某个查询需要连接不出现在同一个块里的事实之前都能用。

考虑关于一个项目存储的三条事实。

- Alice 管理 Project Atlas
- Project Atlas 运行在 PostgreSQL 上
- PostgreSQL 集群在周二宕机了

像“Alice 的项目受到了周二宕机的影响吗”这样的查询需要这三条全部。

![](images/img-02.jpg)

向量搜索只会检索出事实 1 和 3，因为两者都提到了相关词语。事实 2 是连接 Alice 到 PostgreSQL（通过 Project Atlas）的桥梁，但它既没提到 Alice 也没提到周二。相似度搜索会漏掉它。

知识图谱把实体存为节点，关系存为边。它不是匹配文本，而是遍历连接。

那条链（Alice → 管理 → Project Atlas → 运行在 → PostgreSQL）正是让多跳推理成立的东西，而它对扁平向量检索是不可见的。

## 记忆管线，以及抽取在其中的位置

每个基于图谱的 agent 记忆系统都遵循一个共同的管线：

- **摄入（Ingest）：** 原始数据进来（对话消息、文档、JSON 业务数据）
- **抽取（Extract）：** 一个 LLM 读取原始数据，决定存在哪些实体、什么关系连接它们、哪些属性重要
- **存储（Store）：** 抽取出的实体变成节点，关系变成边，全部持久化到图谱里
- **检索（Retrieve）：** 在查询时，系统搜索图谱并组装相关事实
- **交付（Deliver）：** 检索出的事实被格式化成一个上下文块，注入到 agent 的提示词里

抽取这一步是一切被决定的地方。它决定你的图谱包含什么、如何被组织、以及下游有什么是可查询的。

![](images/img-03.jpg)

问题来了。在大多数框架里，这一步是个黑盒。你传入文本，一个 LLM 拉出“实体”和“关系”，你得到节点和边。LLM 自己决定类型、标签、属性。

你对它分类什么、怎么分类毫无控制权。

让我们来理解如何修复它。

## 用 Pydantic 定义 schema

修复方案就是 AI 技术栈里到处都在用的那个模式。

FastAPI 端点用 Pydantic 响应模型。

函数调用工具用 Pydantic schema。

Agent 记忆在 Zep 里也是同样的方式。

用 `EntityModel`（Pydantic 的 `BaseModel` 的子类）定义自定义实体类型，配上 `EntityText` 字段和引导抽取模型的描述。

```python
from zep_cloud.external_clients.ontology import EntityModel, EntityText
from pydantic import Field

class Project(EntityModel):
    """
    Represents a specific software project, application, 
    or codebase that the user is building or contributing to.
    """

    project_status: EntityText = Field(
        description="Current status: active, completed, paused, or archived.",
    )
    project_type: EntityText = Field(
        description="Type of project: web app, mobile app, API, CLI tool, etc.",
    )
```

这里的文档字符串（docstring）和字段描述很重要，因为带有具体例子的好描述能给抽取器足够的信号去准确分类。

上面那些 Pydantic 描述不只是分类指令。它们教给了抽取器它本来不知道的词汇。

一个 Technology 实体遵循同样的模式。

```python
class Technology(EntityModel):
    """
    Represents a programming language, framework, library, 
    database, or tool that the user works with.
    """

    tech_category: EntityText = Field(
        description="Category: programming language, framework, database, etc.",
    )
```

边类型用 `EdgeModel`，并携带它们自己的属性。

```python
from zep_cloud.external_clients.ontology import EdgeModel

class WorksOn(EdgeModel):
    """The user is currently working on, building, or contributing to a project."""
    role: EntityText = Field(
        description="User's role: lead developer, contributor, maintainer, etc.",
    )

class UsesTechnology(EdgeModel):
    """The user actively uses or works with a specific technology."""
    proficiency: EntityText = Field(
        description="Proficiency level: beginner, intermediate, advanced, or expert.",
    )
```

最后，用 `EntityEdgeSourceTarget` 给出 source/target 约束，把它们接入图谱，这定义了哪些实体类型可以通过哪些边类型连接：

```python
from zep_cloud import EntityEdgeSourceTarget

client.graph.set_ontology(
    entities={"Project": Project, "Technology": Technology},
    edges={
        "WORKS_ON": (
            WorksOn,
            [EntityEdgeSourceTarget(source="User", target="Project")],
        ),
        "USES_TECHNOLOGY": (
            UsesTechnology,
            [EntityEdgeSourceTarget(source="User", target="Technology")],
        ),
    },
)
```

这段代码强制规定：

- `WORKS_ON` 只能连接一个 User 和一个 Project
- `USES_TECHNOLOGY` 只能连接一个 User 和一个 Technology。

任何不符合这些约束的关系都不会产生一条带类型的边。

总结一下，这是我们目前得到的东西：

![](images/img-04.jpg)

## 底层发生了什么

当一段对话在 schema 生效的情况下被摄入时，Zep 的抽取管线会运行五个步骤：

- **实体抽取** 识别文本中的命名实体
- **实体消解** 合并重复项（“Nexus”和“the Nexus project”变成同一个节点）
- **事实抽取** 识别关系并把它们输出为带类型的边
- **事实消解** 检测矛盾，使过时的事实失效（保留历史）
- **时间抽取** 解析时间引用，并把它们映射到每条边上的有效期窗口

你的 pydantic schema 引导第 1 步和第 3 步。实体类型告诉抽取器要找什么。带约束的边类型告诉它要分类什么关系。消解和时间处理是自动发生的。

## 实际走一遍看看它的样子

我们摄入一段对话，里面一个叫 Alex 的开发者讨论他的工作（一个叫 Nexus 的活跃 web app、他的技术栈、熟练度）：

![](images/img-05.jpg)

查询 Project 节点会返回 Nexus，并带有填充好的 `project_status` 和 `project_type` 属性。

![](images/img-06.jpg)

这个节点不是一个通用的“Topic”或“Object”。它是一个 Project，带有 schema 中定义的结构化字段。

边也是带类型的。

`WORKS_ON` 携带 role: lead developer

![](images/img-07.jpg)

`USES_TECHNOLOGY` 对 Python 和 Docker 携带 proficiency: advanced，对 TypeScript 携带 proficiency: intermediate。

![](images/img-08.jpg)

现在就可以按状态过滤项目、按类别过滤技术，并以精确的答案查询“哪些活跃项目使用 PostgreSQL”。

## 上下文模板

最后一块拼图是上下文模板，它把带类型的事实组装成一个可直接放进提示词的块。

你可以定义要包含哪些边类型和实体类型，Zep 会把它们连同时间注解格式化成一个单一字符串，注入到 agent 的提示词里。

```python
client.context.create_context_template(
    template_id="dev-context",
    template="""# PROJECTS
%{edges types=[WORKS_ON] limit=5}

# TECH STACK
%{edges types=[USES_TECHNOLOGY] limit=10}

# PROJECT DETAILS
%{entities types=[Project] limit=5}

# TECHNOLOGIES
%{entities types=[Technology] limit=10}""",
)
```

它看起来像这样：

![](images/img-09.jpg)

结果上下文块里的每一条都是带类型、带时间注解的，并携带定义好的属性。模板存一次，在 agent 调用里用 ID 引用它。

## 10/10/10 约束，以及把 schema 作为推理边界

Zep 强制一个硬性限制：10 个自定义实体类型、10 个自定义边类型、每个类型 10 个字段。

![](images/img-10.jpg)

这是有意为之的，是为了逼一个开发者去想清楚在一个领域里什么才重要，而不是把一切都建模出来。

source/target 约束还充当了护栏，限定一个 agent 被允许记住什么。如果一个 schema 不包含一条连接 Project 到 Competitor 的边类型，抽取模型就不会创建那种关系，即使一段对话同时提到了两者。

schema 定义了有效记忆的空间。

这和带类型的函数调用背后是同一个原则——在那里我们约束 LLM 的输出空间，让它无法产生无效的参数。记忆 schema 把同样的约束应用到 agent 存储什么上。

从 3-4 个实体类型和 3-4 个边类型开始，它们捕获你领域逻辑的 80%，然后逐步增加复杂度。

没有 schema 纪律的 agent 记忆，是一个行为像向量库的图谱。

某种程度上，你付出了构建图谱的成本，却没拿到结构化检索的好处。

schema 是你把那个好处拿回来的方式，而且因为它是 Pydantic，所以没有什么新东西要学。

对领域特定的应用来说尤其如此。LLM 抽取在通用知识上工作得还不错，但一旦你的领域有内部术语、与常用词撞车的产品名、或训练数据里没有的行话，无引导的抽取就会产出废话。schema 弥合了那个鸿沟。它把领域词汇直接带进抽取这一步，所以 LLM 不需要事先见过你的术语。它只需要你写下的定义。

![](images/img-11.jpg)

你可以在这里找到 Zep 的 GitHub 仓库 →（别忘了点 star 🌟）
