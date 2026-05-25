# 如何用 10 个步骤搭建一支 Claude 智能体团队：从一个智能体到 20 个并行工作

**作者：** Codez ([@0xCodez](https://x.com/0xCodez))  
**日期：** 2026年5月24日  
**来源：** [How to build a team of Claude agents in 10 steps](https://x.com/0xCodez/status/2058513716509913581)

我把所有在 Claude 上真正管用的多智能体编排经验——官方文档、cookbook、来自 Netflix 和 Spiral 的真实配置——汇成了这一篇完整教程。

收藏起来，存好。读完之后，你就知道怎么把一个不堪重负的智能体，变成一支最多 20 人、并行作战的协同团队。

关注我的 Substack，获取新鲜的 AI alpha：movez.substack.com

这不是夸张。在 2026 年 4 月之前，这得花上好几个月做基础设施工程。现在，一份 YAML 配置加 10 个步骤就够了。

## 为什么一个智能体会撞墙

你做了一个智能体，它跑得挺好，于是你给它派了更多活。

加一个研究能力，加报告撰写，加数据分析，再加一道评审。每加一样，系统提示就更长、工具列表就更大、上下文窗口就更挤。

直到某天你发现，它变慢了、变糊涂了，连过去最拿手的事都做不好了。这不是模型的问题，是架构的问题。

单个智能体只有一个上下文窗口，你硬塞进去的每个能力，都在抢同样有限的注意力。复杂度一旦过线，一个身兼十职的通才，反而不如十个各管一摊的专才。

解法是组一支团队。不是把提示写得更长，而是分工。

![](images/img-01.jpg)

文档里有三个事实定义了这套架构：一个名册里最多放 20 个不同的智能体，每个都待在自己隔离的上下文窗口里，但全都共用一个文件系统。各想各的，活儿摊在一起——这正是一支团队能并行干活又不乱套的原因。

## 决策与设计

### 01. 先确认你真的需要一支团队

别因为"多智能体"听着唬人就上。它更费 token，还多出一层协调成本。下面三件事，满足其一再考虑：

- **并行。** 工作能拆成互不相干的子任务——各自的日志文件、各自的代码模块。一个智能体只能挨个做，一支团队能同时做。
- **专精。** 不同的问题要不同的专长——一个管安全评审，一个写文档，一个做定价建模——让一个通才在它们之间来回切换，结果是哪样都做不好。
- **升级。** 大多数活很简单，但偶尔有几个子任务出奇地难。一支团队可以把难的那几个交给更强的模型，而不必每一步都为它付钱。

### 02. 动手写代码之前，先把角色理清楚

设计多智能体，本质上就是设计一个组织。写任何代码之前，先在纸上把团队画出来：一个协调者，外加一份专才清单，每个专才一项明确的活。

找个真实的范例来对照。Anthropic 文档里有个事件响应的例子：一个主智能体负责调查全局，几个子智能体同时铺开，分别去查部署历史、错误日志、监控指标和支持工单。

四个专才，一个协调者，本来一个智能体得挨个做的事，现在并行地完成了。

给每个角色起个名、写一句话的职责、标注它用什么模型和工具。两个角色要是重叠了，就合并。专才宁可少而精，也别多而含糊。

### 03. 给每个角色挑一个模型——省钱就省在这

很多人没注意到的一招：团队里每个智能体都可以跑不同的模型，你并没有被绑死在一个上。

Spiral by Every 的生产实践就证明了这点——他们用 Haiku 当协调者，用 Opus 当负责撰写的子智能体。

![](images/img-02.jpg)

协调者干的只是分派和排序，一个又快又便宜的模型完全够用。真正吃力的重活，只交给需要它的那些专才。

让模型对上活。按角色搭配不同档位，是影响成本和速度最大的一个抓手。

## 搭建团队

### 04. 配好 Managed Agents

每个多智能体请求都跑在 Claude Managed Agents 上，需要带上 beta 头 `managed-agents-2026-04-01`。SDK 会自动加上。

为什么用 Managed Agents，而不是自己搭一套？因为一旦团队要远程运行、要服务很多用户、要共享文件系统、还要保存状态，你就撞上了一堆基础设施问题——会话、内存、安全、沙箱。

这些 Managed Agents 都替你包了，你只管设计团队。装上 Anthropic SDK，从 Console 里配好 API key，就可以开干了。

![](images/img-03.jpg)

### 05. 把每个专才都做成一个独立的智能体

先自下而上把专才搭出来。每个都是独立的智能体，有自己的模型、提示和限定好的工具集。建好之后记下它们的智能体 ID——协调者后面要引用。

这里最该守住的一条：把每个专才的工具范围卡得很紧。在 cookbook 的销售提案例子里，研究者只拿到网页搜索，图书管理员只能读文件，定价建模者只看得到规则文件和席位数。

每个智能体只碰它干活需要的那点东西，多一样都不碰——这样它能专注，整个系统也查得清。

### 06. 创建协调者，并声明名册

接下来是主智能体。你通过设置 `multiagent` 字段，把一个智能体标成协调者，并列出它能委派的子智能体 ID。这份配置故意写得很精简：

```yaml
name: Engineering Lead
model: claude-opus-4-7
system: >
  You coordinate engineering work. Delegate code review
  to the reviewer agent and test writing to the test agent.
tools:
  - type: agent_toolset_20260401
multiagent:
  type: coordinator
  agents:
    - type: agent
      id: $REVIEWER_AGENT_ID
    - type: agent
      id: $TEST_WRITER_AGENT_ID
```

正是那个 `agent_toolset_20260401` 工具，才让协调者有了委派的能力。这份名册最多能放 20 项。

![](images/img-04.jpg)

你可以锁定某个具体的智能体版本，也可以引用最新的，或者用 `{"type": "self"}` 让协调者派生出自己的副本，实现递归式的并行。

### 07. 协调者的提示，要写成一个管理者，而不是干活的人

团队的成败就在这里。协调者的系统提示，不该自己去干活，而该说清楚怎么把活派出去。

一份好的协调者提示会讲：这是你手下的专才，每个是干什么的，怎么决定谁接什么活，怎么把他们的结果拼到一起。它想的是排序和汇总，而不是具体的领域细节——那些都放在专才里。

如果你发现自己正往协调者里写领域指令，那部分内容就该挪进某个子智能体。

下面是一份真实的事件响应团队的协调者提示——注意它自己从不去查任何东西，只负责分派和汇总：

```text
You are the incident-response coordinator. You do NOT
investigate anything yourself. Your only job is to delegate
to your specialists and synthesize what they return.

Your specialists:
- deploy_agent  → reviews recent deploy history for changes
- logs_agent    → searches error logs for anomalies
- metrics_agent → checks dashboards for abnormal patterns
- tickets_agent → scans support tickets for user reports

How to work:
1. When an incident arrives, delegate to ALL FOUR
   specialists in parallel — do not wait for one before
   starting the next.
2. Give each specialist only the incident description and
   the time window. Nothing else.
3. When results return, look for correlation across them
   (e.g. a deploy that lines up with a log spike and ticket
   surge points to a root cause).
4. If one specialist's finding is unclear, send it a
   follow-up — it remembers its previous turn.

Output format:
- ROOT CAUSE: one sentence, or "unconfirmed"
- EVIDENCE: one bullet per specialist that contributed
- RECOMMENDED ACTION: one clear next step

Never include raw logs or full ticket text in your final
answer — synthesize, do not dump.
```

每一行讲的都是分派、关联和输出格式。真正搜日志、读指标的活，都在专才那里——那才是它们该在的地方。

## 运行、观察、改进

### 08. 搞清楚团队是怎么沟通的

当你运行协调者时，它的运作机制很具体，值得了解：

协调者每委派给一个子智能体，就会派生出一条它自己的会话线程——一条上下文隔离、各有各历史的事件流。协调者在主线程里汇报，新线程会在它委派时实时冒出来。

关键是：这些线程是持久的。协调者可以给一个之前调用过的智能体再发一条后续消息，而那个智能体还记得它前几轮的全部内容。

![](images/img-05.jpg)

有一条硬约束你得绕着它设计：协调者只能往下委派一层，超过一层的深度会被直接忽略。

专才不能再带自己的小团队。这是故意这么设计的——好让整个系统可预测、可追踪。

### 09. 在 Claude Console 里盯着整件事

一套能上生产的多智能体系统，和一套还停在实验阶段的系统，区别就在能不能看得见。

每次运行都会在 Claude Console 里留下一份完整的 trace：哪个智能体做了什么、按什么顺序、为什么。你能看到每一个委派决定，能查看每个子智能体的推理，能从头到尾跟着这条链走一遍。

![](images/img-06.jpg)

结果出错时，trace 会告诉你是哪个专才出了岔子，问题出在委派上还是专才本身。别蒙着眼睛跑一支团队——把 trace 读一读。

### 10. 扩展到 20 个，再加上共享记忆

小团队跑通之后，就把它做大。把专才加到 20 个的名册上限，让协调者一口气并行铺开到所有人身上。

然后用共享记忆把闭环补上。当很多子智能体在同一个领域干活时，Dreaming 功能能把它们集体学到的东西汇总起来，把共享的洞见写进一个团队级的记忆库——这是任何单个智能体会话都做不到的。

这支团队不光能并行干活，还能作为一个整体越用越聪明。

Netflix 的平台团队在生产里跑的就是这套：用多智能体编排处理上百个同时进行的构建产生的日志，并行的子智能体在成千上万个应用里翻出反复出现的问题——这些活换成单智能体，根本没法挨个做完。

## 哪些坑会把智能体团队搞垮

- **一个智能体就够用，你却非要组团队。** 多智能体更费钱、协调更慢。如果工作既不能并行、也不需要专精或升级，你就是白白添了一堆复杂度。
- **协调者自己下场干活。** 如果主智能体装的是领域指令而不是委派逻辑，那你做出来的，不过是个披着团队外衣的臃肿单智能体。
- **工具范围放得太松。** 当每个专才什么都能碰，专注就垮了，trace 也读不下去。把每个智能体卡死在它该干的活上。
- **跟"只能一层"的限制较劲。** 协调者只往下委派一层。你费劲搭一套藏起来的子协调者层级，纯属白忙——那个深度会被忽略。
- **蒙着眼睛跑。** Console 的 trace 就是为了让你看清哪个智能体做了什么。跳过它，你就没法给一个环节这么多的系统排错。

## 结语

大多数人会继续往一个智能体里塞更多能力，看着它变慢、变差，然后断定智能体还不够成熟。

而那些组建团队的人，手里拿到的是另一样东西：一个负责委派的协调者，一群各带自己上下文、并行干活的专才，一个供他们协作的共享文件系统，还有一个让整个团队越来越敏锐的记忆库。

挑一个能拆成几块并行去做的任务，规划三个专才加一个协调者，先把这支小团队搭起来。光是这一步，就会改变你的智能体能扛多少活。
