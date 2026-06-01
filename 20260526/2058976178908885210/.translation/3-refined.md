# Pydantic 修好了我的 Agent 记忆

**作者：** Akshay ([@akshay_pachaar](https://x.com/akshay_pachaar))  
**日期：** 2026年5月26日  
**来源：** [Pydantic fixed my Agent's Memory](https://x.com/akshay_pachaar/status/2058976178908885210)

你的 agent 记住了一切，却什么都没真正理解。

Agent 记忆是从向量数据库起步的。把事实切成块（chunk）存起来，再按相似度检索。

平时都还好用，可一旦某个问题需要把分散在不同块里的事实串起来，它就崩了。问题不在相似度，而在结构。

后来知识图谱被拿来救场：实体当节点，关系当边，靠遍历而不是靠匹配。

但大多数团队又撞上了另一堵墙。

你给 agent 配一个知识图谱当记忆，默认情况下，结构是由负责抽取的那个 LLM 自己说了算的。

实体分什么类型、关系叫什么名字、带哪些属性，全是它挑的。

挑出来的结果，往往特别笼统。

举个例子。你在做一个客户支持 agent，喂给它 50 段支持对话，里面有客户、有工单、有功能、有升级处理的历史。

然后你问它：“哪些企业客户还有没解决的 sev-1 工单？”

数据明明都在图谱里。可每一张支持工单都被存成了一个“Topic”节点，每个客户都是“Object”，每条关系都叫“RELATES_TO”。

你没法按类型、按严重程度、按套餐等级去筛。查出来的全是噪声。

agent 其实什么都没忘。只是从来没人告诉它，该把注意力放在哪儿。

![](images/img-01.jpg)

解法其实很直接：提前把 schema 定下来。告诉抽取模型，你这个领域里有哪些类型的实体、哪些关系是合法的、每样东西又该带哪些属性。

这套事先定好的结构，有个名字叫本体（ontology）。你可以把它理解成 agent 大脑的 schema。

下面我们就来捋一遍：这件事为什么重要、不做会出什么问题、以及怎么用一套 100% 开源的方案把它落地。

## 为什么扁平检索撑不起多跳推理

基于向量的记忆，是把事实存成一段段文本块，再按语义相似度去捞。这套办法平时够用，但有一种情况它就不行了——当一个问题需要的几条事实，根本不在同一个块里。

比如关于某个项目，存了这么三条事实：

- Alice 负责 Project Atlas
- Project Atlas 跑在 PostgreSQL 上
- PostgreSQL 集群周二宕机了

现在问一句“Alice 的项目受周二那次宕机影响了吗”，这就得把三条全凑齐才答得上来。

![](images/img-02.jpg)

可向量搜索只会捞出第 1 条和第 3 条，因为这两条都带着问题里出现的词。第 2 条才是关键——它通过 Project Atlas 把 Alice 和 PostgreSQL 连了起来，偏偏它既没提 Alice，也没提周二。于是相似度搜索就把它漏了。

知识图谱不一样。它把实体存成节点，关系存成边。它不是去匹配文字，而是顺着连接一路走下去。

正是“Alice → 负责 → Project Atlas → 跑在 → PostgreSQL”这条链，让多跳推理成立。而这条链，扁平的向量检索是完全看不见的。

## 一条记忆管线，以及抽取卡在哪个位置

每一个基于图谱的 agent 记忆系统，大体都走着同一条管线：

- **摄入（Ingest）：** 原始数据进来——对话消息、文档、JSON 业务数据。
- **抽取（Extract）：** 一个 LLM 读这些原始数据，判断里面有哪些实体、它们之间是什么关系、哪些属性重要。
- **存储（Store）：** 抽出来的实体变成节点，关系变成边，全部落进图谱。
- **检索（Retrieve）：** 等到查询的时候，系统去图谱里搜，把相关的事实拼起来。
- **交付（Deliver）：** 拼出来的事实整理成一段上下文，塞进 agent 的提示词里。

真正决定一切的，是抽取这一步。你的图谱里装着什么、长成什么结构、之后哪些东西查得到，全在这一步定下来。

![](images/img-03.jpg)

问题就出在这儿。大多数框架里，这一步是个黑盒：你把文本丢进去，LLM 帮你拣出一堆“实体”和“关系”，吐回来一组节点和边。类型怎么分、标签怎么起、带什么属性，统统是它自己拿主意。

你对它分了什么、怎么分的，一点话语权都没有。

那要怎么办呢？接着往下看。

## 用 Pydantic 把 schema 定下来

解法，其实就是 AI 技术栈里到处都在用的那一招。

FastAPI 的接口，配的是 Pydantic 响应模型。

函数调用的工具，配的是 Pydantic schema。

到了 Zep 里，agent 记忆走的也是同一条路。

你用 `EntityModel`（它就是 Pydantic 里 `BaseModel` 的子类）来定义自己的实体类型，里面放上 `EntityText` 字段，再配上描述，去引导抽取模型。

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

这里的文档字符串（docstring）和字段描述很关键。描述写得好、带上具体例子，抽取器才有足够的信号去分得准。

而且上面这些 Pydantic 描述，不只是在告诉它怎么分类，更是在教它一套它本来不懂的词汇。

Technology 这个实体也是一样的写法。

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

边的类型则用 `EdgeModel`，它们也各自带着自己的属性。

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

最后，用 `EntityEdgeSourceTarget` 加上 source/target 约束，把它们接进图谱——这一步规定了，哪些实体类型能通过哪种边连在一起：

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

这段代码定死了两条规矩：

- `WORKS_ON` 只能把 User 连到 Project；
- `USES_TECHNOLOGY` 只能把 User 连到 Technology。

凡是不符合这些约束的关系，都不会生成一条带类型的边。

到这儿先小结一下，我们已经有了这些东西：

![](images/img-04.jpg)

## 底层到底发生了什么

当一段对话在 schema 已经生效的情况下被摄入时，Zep 的抽取管线会跑完五步：

- **实体抽取**：把文本里的命名实体认出来。
- **实体消解**：把重复的合并掉（“Nexus”和“the Nexus project”会归成同一个节点）。
- **事实抽取**：认出关系，把它们输出成带类型的边。
- **事实消解**：发现互相矛盾的地方，让过时的事实失效（但历史会留着）。
- **时间抽取**：解析其中的时间信息，给每条边标上它的有效期。

你写的那份 pydantic schema，引导的就是第 1 步和第 3 步。实体类型告诉抽取器该找什么，带约束的边类型告诉它该把哪些关系归成哪类。至于消解和时间处理，是自动完成的。

## 跑一遍，看看实际长什么样

我们摄入一段对话，里面有个叫 Alex 的开发者在聊他手上的活儿——一个还在活跃开发的 web app，叫 Nexus，还聊到了他用的技术栈和各自的熟练度：

![](images/img-05.jpg)

去查 Project 节点，返回的就是 Nexus，而且 `project_status` 和 `project_type` 这两个属性都填好了。

![](images/img-06.jpg)

这个节点不再是个笼统的“Topic”或“Object”，而是一个实打实的 Project，带着 schema 里定义好的结构化字段。

边也一样是带类型的。

`WORKS_ON` 上带着 role：lead developer。

![](images/img-07.jpg)

`USES_TECHNOLOGY` 上，Python 和 Docker 标的是 proficiency：advanced，TypeScript 标的是 proficiency：intermediate。

![](images/img-08.jpg)

到这一步，你就能按状态筛项目、按类别筛技术，问一句“哪些活跃项目用了 PostgreSQL”，也能得到一个干脆利落的答案。

## 上下文模板

最后一块拼图，是上下文模板——它负责把这些带类型的事实，拼成一段可以直接塞进提示词的内容。

你来定要包含哪些边类型、哪些实体类型，Zep 会把它们连同时间标注一起，格式化成一整段字符串，注入到 agent 的提示词里。

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

出来大概是这个样子：

![](images/img-09.jpg)

最后这段上下文里，每一条都是带类型、带时间标注的，还携带着定义好的属性。模板存一次就行，之后在 agent 调用里用 ID 引用它即可。

## 10/10/10 这个约束，以及把 schema 当成推理的边界

Zep 卡了一条硬限制：自定义实体类型最多 10 个，自定义边类型最多 10 个，每个类型最多 10 个字段。

![](images/img-10.jpg)

这是故意的，就是要逼开发者先想清楚——在这个领域里，到底什么才重要，而不是一股脑把什么都建模进去。

那些 source/target 约束还有另一层作用：它们像护栏一样，圈定了一个 agent 被允许记住的范围。如果 schema 里压根没有一条从 Project 连到 Competitor 的边，那么哪怕一段对话里同时提到了这两者，抽取模型也不会去建这条关系。

换句话说，schema 划定了「什么样的记忆才算数」的边界。

这背后的道理，和带类型的函数调用是一样的：在那里，我们约束 LLM 的输出空间，让它没法吐出不合法的参数。记忆的 schema，是把同一套约束，用在了 agent 该存什么上。

上手时，先挑 3-4 个实体类型、3-4 个边类型，把你领域里 80% 的逻辑覆盖住，剩下的再一点点加。

一个不讲 schema 规矩的 agent 记忆，本质上就是一个表现得跟向量库没两样的图谱。

某种意义上，你花了搭图谱的力气，却没尝到结构化检索的甜头。

而 schema，就是把这份甜头拿回来的办法。又因为它本来就是 Pydantic，所以也没什么新东西要学。

对那些领域专门的应用来说，这一点尤其要紧。LLM 抽取处理通用知识还算凑合，可一旦你的领域里有内部术语、有和常用词撞名的产品名、或者有训练数据里压根没出现过的行话，没人引导的抽取就只会产出一堆废话。schema 正好补上这个缺口——它把领域里的词汇直接带进抽取那一步，于是 LLM 哪怕从没见过你这套说法也没关系，它要的只是你写下的那些定义。

![](images/img-11.jpg)

Zep 的 GitHub 仓库在这儿 →（看完别忘了点个 star 🌟）

谢谢阅读！
