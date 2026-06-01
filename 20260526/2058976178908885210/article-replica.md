# Pydantic 修好了我的 Agent 记忆

**作者：** Akshay ([@akshay_pachaar](https://x.com/akshay_pachaar))  
**日期：** 2026年5月26日  
**来源：** [Pydantic fixed my Agent's Memory](https://x.com/akshay_pachaar/status/2058976178908885210)

先说个让人有点泄气的现象：你的 agent 好像什么都记得，可你一问它点稍微绕的东西，它又什么都答不上来。

这事得从头讲。

最早，大家是用向量数据库给 agent 做记忆的。做法很朴素：把信息切成一段一段的小块存起来，等你要用的时候，按意思相近去把它捞回来。

这招平时挺好使。可总有那么一类问题，需要把藏在好几个块里的事实拼到一块儿才答得上来——一到这种时候，它就抓瞎了。说到底，卡住它的不是「像不像」，而是「有没有结构」。

后来知识图谱被请出来救场。它换了个思路：把一个个事物当成节点，把它们之间的关系当成线，要找答案，不是去比对文字，而是顺着这些线一路走过去。

听起来挺好。可大多数团队走到这一步，又撞上了一堵新墙。

事情是这样的：你给 agent 配了知识图谱当记忆，可这张图长成什么样，默认是由那个负责「抽取」的 LLM 自己说了算的。东西该分成几类、关系该叫什么名、每样又该带哪些信息——全凭它一个人拍板。

它拍出来的板，往往特别笼统、特别没用。

举个具体的例子你就懂了。

假设你在做一个客服 agent，喂给它 50 段客服对话，里头有客户、有工单、有产品功能，还有一路升级处理的来龙去脉。

然后你问它：「哪些大客户手上还压着没解决的 sev-1 严重工单？」

数据明明都在图里。可问题来了——每一张工单，它都笼统地存成了一个叫「Topic」的节点；每个客户，都叫「Object」；每一条关系，一律叫「RELATES_TO」。

这下你没法按类型筛，没法按严重程度筛，也没法按客户的套餐等级筛。问出去，回来的全是一团噪声。

其实 agent 一点东西都没忘。只是从头到尾，没人告诉过它：你到底该盯着什么看。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDYyMTNkMjQ3OGZhZGY0YzBhMDZmYzE5YjZlNWZmMGNfYWRkN2ZmZmFhNTUzMmE2NzI5YWQzYzIwZWFkZTQ2MjFfSUQ6NzY0NDAwMTM2ODQwMzMxNTg5OF8xNzc5NzU3NzkwOjE3Nzk4NDQxOTBfVjM)

那怎么办？办法其实特别直白：别等它自己瞎猜，提前把规矩立好。明明白白告诉抽取模型——我这行当里，有哪几类东西、它们之间哪些关系算数、每样东西又该记下哪些信息。

这套提前立好的规矩，有个正经名字，叫「本体」（ontology）。你不用被这个词吓到，把它当成 agent 那颗大脑的「登记表」就行。

接下来，我们就慢慢看三件事：这套登记表为什么这么要紧、不立它会出什么乱子、以及怎么用一套完全开源的工具把它落地。

## 为什么「碰运气式」的检索撑不起多跳推理

先说回向量记忆。它的本事，是把事实存成一段段文字，再按意思相近去捞。平时够用。可有一种情况它就彻底没辙了——你要的几条线索，偏偏不在同一段文字里。

举个小例子。关于某个项目，系统里存了这么三句话：

- Alice 负责 Project Atlas 这个项目
- Project Atlas 跑在 PostgreSQL 上
- PostgreSQL 集群周二那天宕机了

现在你问一句：「Alice 的项目，受周二那次宕机影响了吗？」

要答得上来，这三句话一句都不能少。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzYxYWM5YmQxYjRkYmJjZGQwNDA3NDI3MmU2NTk5NTRfYWY4OTliYjM3NDc1ZDI0YWY5OTg5NzViZGU1Mjc1ZjRfSUQ6NzY0NDAwMTM3NTkxMjk3MTQ4Ml8xNzc5NzU3NzkwOjE3Nzk4NDQxOTBfVjM)

可向量搜索只会把第一句和第三句捞回来——因为这俩里都带着你问题里出现的词。真正的关键其实是第二句：是它，通过 Project Atlas，把 Alice 和 PostgreSQL 这两头给接上了。可偏偏第二句里既没提 Alice，也没提周二。于是相似度搜索两眼一抹黑，直接把它漏了过去。

知识图谱就不会犯这个错。它把每样东西存成节点，把关系存成线，找答案的时候不是去对字眼，而是顺着线往下走。

正是「Alice → 负责 → Project Atlas → 跑在 → PostgreSQL」这一串，撑起了所谓的「多跳推理」。而这一串，扁平的向量检索是压根看不见的。

## 一条记忆流水线，看看「抽取」卡在哪一环

不管哪家做基于图谱的 agent 记忆，大体都走着同一条流水线：

- **摄入（Ingest）**：原始材料进来——可能是对话、文档，也可能是一堆 JSON 业务数据。
- **抽取（Extract）**：一个 LLM 把这些材料读一遍，判断里面有哪些事物、它们之间是什么关系、哪些信息值得记。
- **存储（Store）**：抽出来的事物变成节点，关系变成线，统统落进图里。
- **检索（Retrieve）**：等你提问的时候，系统去图里翻，把相关的事实凑齐。
- **交付（Deliver）**：把凑齐的事实理成一段话，塞进 agent 的提示词里。

这一圈下来，真正定生死的，是「抽取」这一环。你的图里最后装着什么、长成什么样、以后哪些问题答得出来——全在这一步定了下来。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDFlZDJlNjRjNzcxNzFhNjg4ZjNhYzU3ZjdhZTY2NjhfNzc0MWY1YjgzMDUxMmVhYmVlOTFhOWY0N2QwOWU5NGZfSUQ6NzY0NDAwMTM4NTM4MTc5Mjk4OV8xNzc5NzU3NzkwOjE3Nzk4NDQxOTBfVjM)

问题恰恰就出在这儿。

在大多数框架里，这一环是个不透明的黑盒：你把文字丢进去，LLM 帮你挑出一堆「事物」和「关系」，再吐回来一组节点和线。可分成几类、叫什么名、带什么信息，全是它一个人闷头决定的，你插不上嘴。

那这口气怎么咽？别急，往下看就有办法了。

## 用 Pydantic 把规矩立下来

说出来你可能会笑——这个办法，其实就是整个 AI 圈早就用滥了的那一招。

FastAPI 写接口，配的是 Pydantic 的响应模型。

让模型调用函数，配的也是 Pydantic 的 schema。

到了 Zep 这儿做 agent 记忆，走的还是同一条老路。

具体怎么做？你用 `EntityModel`（说白了它就是 Pydantic 里 `BaseModel` 的一个子类）来定义自己要的事物类型，往里放上 `EntityText` 字段，再给每个字段写句说明，去给抽取模型带路。

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

这里的文档说明（docstring）和字段说明，可不是写来好看的。说明写得越具体、越带例子，抽取模型心里就越有谱，分起类来也就越准。

更妙的是，上面这些 Pydantic 说明，做的其实不只是「告诉它怎么分类」这一件事——它顺手还教会了模型一套它原本根本不认识的词。

再来一个 Technology 实体，写法一模一样。

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

至于「关系」这条线，用的是 `EdgeModel`，它同样能带上自己的信息。

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

最后一步，把它们接进图里，用 `EntityEdgeSourceTarget` 加上「从哪头连到哪头」的约束——这一句，就规定死了哪类事物之间能用哪种关系连起来：

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

这段代码立了两条死规矩：

- `WORKS_ON` 这种关系，只能从 User 连到 Project；
- `USES_TECHNOLOGY` 这种关系，只能从 User 连到 Technology。

凡是不守这两条规矩的关系，一律不会生成一条正经的、带类型的线。

到这儿先停下喘口气，小结一下——我们手上现在有了这些东西：

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjhhM2Y2ZWYyMGIyMDg5ZGZhMTdmMDczNWY0ZDY1ZjNfODRiODU5YWZmNzdhMjFhNWZkN2E4ZmRkNzQ2ODFkMzJfSUQ6NzY0NDAwMTM5NDE3NzM5NTkxNF8xNzc5NzU3NzkwOjE3Nzk4NDQxOTBfVjM)

## 掀开盖子，看看底下到底在忙什么

当一段对话在「规矩已经立好」的前提下被摄入时，Zep 的抽取流水线，会一口气走完五步：

- **实体抽取**：先把文字里那些有名有姓的事物认出来。
- **实体消解**：把重复的捏成一个（比如「Nexus」和「the Nexus project」，会被认成同一个节点）。
- **事实抽取**：把关系认出来，输出成一条条带类型的线。
- **事实消解**：发现前后打架的地方，让过时的说法作废（不过老底子会留着，方便回溯）。
- **时间抽取**：把对话里的时间信息解析出来，给每条线标上「这话在哪段时间里算数」。

而你写下的那份 schema，引导的正是其中的第一步和第三步：实体类型告诉它该找什么，带约束的关系类型告诉它该把哪些关系归成哪一类。剩下的消解和时间处理，它自己就默默办了，不用你操心。

## 上手跑一遍，看看到底长啥样

我们摄入这么一段对话：里头有个叫 Alex 的开发者，在聊自己手上的活儿——一个还在热火朝天开发的 web app，名叫 Nexus；顺带也聊了他用的技术栈，以及每样技术他到什么熟练度。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmU0YmJhODU4MDczOWNjMWFlYTM1ZGFkN2FjODY0N2RfYmRhZjJkMjljZjk1OGU3YzRmMWUyNzdkNTdiYzY1YTlfSUQ6NzY0NDAwMTQwMDg4MDI1NDEzMV8xNzc5NzU3NzkwOjE3Nzk4NDQxOTBfVjM)

这时候你去查 Project 节点，回来的就是 Nexus，而且 `project_status`（状态）和 `project_type`（类型）这两栏，都老老实实填好了。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGYzYmFlOTlkMGRhMzhiYzMyNmNmZGRjZWZiNjA3MzZfM2Y2OTQ2ZjVkYWQwNjc1NmI0MGRmODBiNjYzNzBlMjlfSUQ6NzY0NDAwMTQxMjc3MDI3MDQyNl8xNzc5NzU3NzkxOjE3Nzk4NDQxOTFfVjM)

注意，这个节点不再是个含含糊糊的「Topic」或者「Object」了——它就是一个正经的 Project，身上带着你在 schema 里定好的那些结构化字段。

关系那头也一样，每条线都带着类型。

比如 `WORKS_ON` 这条线上，就标着 role：lead developer（角色：主力开发）。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzUzYzFlZGZmNDgxNDlkZDEwZGM2YzgwMzg2OTEwYzRfYWU3Y2NjMGMyOWZjYTY0MzlkNzE1MGNlYzZmNzkyNTJfSUQ6NzY0NDAwMTQxOTAxNzcwMjYxNV8xNzc5NzU3NzkxOjE3Nzk4NDQxOTFfVjM)

再比如 `USES_TECHNOLOGY` 这条线：Python 和 Docker 标的是 proficiency：advanced（熟练度：高），TypeScript 标的是 intermediate（中等）。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZWJkNThkOWYzMTZlNzEwYzEyZDI4YjdmOTU4MTllYjBfNjgzYjE0NWEzNThjZTc5OTYzZWRmNmQ1N2NiZTc2MDJfSUQ6NzY0NDAwMTQyODMzMTMzNDg4MF8xNzc5NzU3NzkxOjE3Nzk4NDQxOTFfVjM)

到这一步，你就能按状态挑项目、按类别挑技术了。再问一句「哪些还在做的项目用到了 PostgreSQL」，回来的也是一个干脆利落的答案，不再是一团浆糊。

## 上下文模板：把这些料端到模型面前

最后还差一块拼图，叫上下文模板。它的活儿，是把前面那些带类型的事实，拼成一段能直接塞进提示词的现成内容。

你来定：要带上哪几类关系、哪几类事物。Zep 就帮你把它们连同时间标注一起，理成一整段文字，注入到 agent 的提示词里。

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

拼出来，大概就是下面这个样子：

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGZlYTllOGZkYjFlMjRhM2Y1YmZhYjY2NDVmMjk3NWZfYTUyMjc4ZmU3MTUyMTM5ZDEwMjNmNzZkZDdhYzFlNWRfSUQ6NzY0NDAwMTQzNzYyMTU4NzEzMF8xNzc5NzU3NzkxOjE3Nzk4NDQxOTFfVjM)

你看，这段上下文里的每一条，都是带类型、带时间标注的，身上还挂着定义好的那些信息。模板存一次就够了，往后在 agent 调用里报个 ID 就能用。

## 10/10/10 这条线，其实是在给「该记什么」划边界

Zep 卡了一条挺硬的限制：自定义事物类型最多 10 种，自定义关系类型最多 10 种，每种类型下面最多 10 个字段。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YmM0ZjIyOTQ3MGE0NmU5ZTc5MmY5NDg5YzAxZjgwZTJfNTI2ZjBjM2RkMWVmNGMwOWFhN2EyNzA4NmVhNjQ0NTBfSUQ6NzY0NDAwMTQ0ODQzMDMwODU1Ml8xNzc5NzU3NzkxOjE3Nzk4NDQxOTFfVjM)

这不是抠门，是故意的。它就是要逼着开发者先停下来想一想：在我这个行当里，到底什么才真正要紧——而不是稀里糊涂地，想把天底下的一切都建模进去。

而前面那些「从哪头连到哪头」的约束，还顺带干了另一件事：它们像一圈护栏，圈出了 agent 被允许记住的范围。打个比方，要是你的 schema 里压根没设一条从 Project 连到 Competitor（竞品）的关系，那哪怕一段对话里把这俩一块儿提了，抽取模型也绝不会自作主张去建这层关系。

换句话说，schema 替你划清了一条线：什么样的记忆才算数。

这背后的道理，跟带类型的函数调用其实是同一个：在那边，我们框住模型能吐出的东西，让它没法塞给你一个不合法的参数。记忆的 schema，无非是把同一套框法，挪来管住「agent 该往脑子里存什么」。

真要上手，建议别贪多。先挑 3 到 4 种事物类型、3 到 4 种关系类型，把你行当里八成的门道先盖住，剩下的再一点一点往上加。

说到底，一个不讲 schema 规矩的 agent 记忆，本质上就是一张「用起来跟向量库没两样」的图。

这就有点亏了——搭图的力气你一分没省，结构化检索的甜头你却一点没尝到。

而 schema，就是把这份甜头给挣回来的法子。又因为它底子就是 Pydantic，所以也谈不上要你学什么新东西。

这一点，在那些「行当味」特别重的应用里尤其管用。LLM 抽取通用常识还算凑合，可你这行当一旦有自己的内部黑话、有跟常用词撞名的产品名、或者有训练时它压根没见过的术语，那种没人带路的抽取，就只会给你一堆不知所云的东西。schema 正好补上这道缝——它把行当里的词，直接喂进抽取那一步。于是模型哪怕从没见过你这套说法也不打紧，它要的，无非是你亲手写下的那几句定义而已。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjNkN2Q3YTExODcwZmUxOGFkOGI5Njg1MWVkNDRhYjJfMmFkYWUyMGVkOTA1NzQ3YTc4NjRiYTAxZjJhMTgxOTVfSUQ6NzY0NDAwMTQ1NTEzNzUyNDkzNl8xNzc5NzU3NzkxOjE3Nzk4NDQxOTFfVjM)

Zep 的 GitHub 仓库就在这儿 →（看完顺手点个 star 🌟）

谢谢你读到这儿！
