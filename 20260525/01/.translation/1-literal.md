# 如何用 10 个步骤搭建一支 Claude 智能体团队：从一个智能体到 20 个并行工作

**作者：** Codez ([@0xCodez](https://x.com/0xCodez))  
**日期：** 2026年5月24日  
**来源：** [How to build a team of Claude agents in 10 steps](https://x.com/0xCodez/status/2058513716509913581)

我把所有在 Claude 上行之有效的多智能体编排经验——官方文档、cookbook、来自 Netflix 和 Spiral 的真实配置——合并成了这一篇完整教程。

把它收藏起来。保存好。读完之后，你将知道如何把一个不堪重负的智能体，变成一支最多 20 个、并行工作的协同团队。

关注我的 Substack 获取新鲜的 AI alpha：movez.substack.com

这不是夸张。直到 2026 年 4 月之前，这都需要数月的基础设施工程。现在它只是一份 YAML 配置和 10 个步骤。

## 为什么一个智能体会撞墙

你搭建了一个智能体。它有效。所以你给它安排了更多工作。

加一个研究能力。加报告撰写。加数据分析。加一个评审步骤。每一次添加都让系统提示更长、工具列表更大、上下文窗口更拥挤。

然后某一天你注意到这个智能体变得更慢、更困惑，在它过去擅长的事情上表现更差了。这不是模型问题。这是架构问题。

单个智能体只有一个上下文窗口，你拴上去的每一项能力都在争夺同样有限的注意力。超过某个复杂度，一个身兼十职的通才，表现会比十个各做一件事的专才更差。

解决办法是一支团队。不是一个更大的提示——而是分工。

![](images/img-01.jpg)

三个事实定义了这套架构，直接来自文档：一个 roster 中最多 20 个独特的智能体，每个都在自己隔离的上下文窗口里，全都共享一个文件系统。隔离的思考、共享的工作区——这就是让一支团队并行工作而不混乱的原因。

## 决策与设计

### 01. 确认你真的需要一支团队

不要因为多智能体听起来很厉害就去用它。它消耗更多 token，并增加协调开销。当以下三件事之一成立时，再去用它：

- **并行化。** 工作能拆分成独立的子任务——分开的日志文件、分开的代码模块。单个智能体按顺序做这些；一支团队同时做。
- **专业化。** 不同的问题需要不同的专长——一个安全评审员、一个文档撰写者、一个定价建模者——而一个通才在它们之间切换上下文会让所有这些都退化。
- **升级。** 大多数工作很简单，但有些子任务出乎意料地难。一支团队把难的那些路由到更强大的模型，而不是在每一步都为它付费。

### 02. 在写任何东西之前先规划角色

多智能体设计就是组织设计。在任何代码之前，在纸上勾勒出团队：一个协调者，和一份每个都有一项明确工作的专才清单。

把它锚定在一个真实的模式上。Anthropic 记录的事件响应案例：一个 lead 智能体运行调查，而子智能体们扇出穿过部署历史、错误日志、指标和支持工单——全都同时进行。

四个专才，一个协调者，对单个智能体来说本会是顺序的工作，并行地发生着。

给每个角色命名，给它一句话的工作，标注它的模型和工具。如果两个角色重叠，就合并它们。更少、更锋利的专才胜过许多模糊的专才。

### 03. 为每个角色挑一个模型——节省就在这里

大多数人错过的一招：团队里的每一个智能体都能运行不同的模型。你没有被锁定在一个上。

Spiral by Every 的生产模式证明了这一点——他们用 Haiku 作为协调者，用 Opus 作为撰写子智能体。

![](images/img-02.jpg)

协调者只是路由和排序，一个又快又便宜的模型做这个就够了。昂贵的重活只发生在需要它的那些专才里。

把模型匹配到工作上。按角色混搭层级是对成本和速度的单一最大杠杆。

## 搭建团队

### 04. 设置 Managed Agents

每一个多智能体请求都运行在 Claude Managed Agents 上，并需要 beta 头 `managed-agents-2026-04-01`。SDK 会自动设置它。

为什么用 Managed Agents 而不是你自己的设置？因为一旦一支团队需要远程运行、扩展到许多用户、共享一个文件系统并持久化状态，你就面对一个基础设施问题——会话、内存、安全、沙箱化。

Managed Agents 处理所有这些，所以你只需设计团队。安装 Anthropic SDK，从 Console 设置你的 API key，你就准备好了。

![](images/img-03.jpg)

### 05. 把每个专才创建为它自己的智能体

先自下而上地搭建专才。每个都是一个独立的智能体，有自己的模型、提示和限定范围的工具集。创建它们并保留它们的智能体 ID——协调者会引用它们。

要紧的纪律：把每个专才的工具范围限定得很紧。在 cookbook 的销售提案案例里，研究者拿到网页搜索，图书管理员只拿到文件读取，定价建模者只看到规则文件和席位数。

每个智能体只接触它的工作所需的东西，别无其他——这让它保持专注，让整个系统可审计。

### 06. 创建协调者并声明 roster

现在是 lead 智能体。你通过设置 `multiagent` 字段把一个智能体标记为协调者，列出它可以委派到的子智能体 ID。这份配置刻意地简洁：

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

那个 `agent_toolset_20260401` 工具是给协调者委派能力的根本。这个 roster 最多容纳 20 条条目。

![](images/img-04.jpg)

你可以固定一个特定的智能体版本，引用最新的，或者用 `{"type": "self"}` 让协调者派生自己的副本以实现递归并行化。

### 07. 把协调者的提示写成一个管理者，而不是一个执行者

这是团队成功或失败的地方。协调者的系统提示不应该试图做这个工作——它应该描述如何委派这个工作。

一个好的协调者提示说：这是你的专才们，这是每个的用途，这是如何决定谁拿到什么，这是如何组合它们的输出。它推理的是排序和综合，不是领域细节——那些活在专才里。

如果你正在把领域指令写进协调者，那部分内容应该改放进一个子智能体。

这是一个真实的事件响应团队协调者提示——注意它从不自己调查任何东西，它只路由和综合：

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

每一行都是关于委派、关联和输出形态。真正的日志搜索和指标读取活在专才里，那是它该在的地方。

## 运行、观察、改进

### 08. 理解团队如何沟通

当你运行协调者时，机制是具体的、值得了解：

协调者委派到的每一个子智能体都派生出它自己的会话线程——一个上下文隔离的事件流，有它自己的历史。协调者在主线程里汇报；新的线程在它委派时于运行时出现。

关键地，线程是持久的：协调者可以给一个它先前调用过的智能体发一个后续，而那个智能体保留它先前轮次的一切。

![](images/img-05.jpg)

一个要围绕它设计的硬约束：协调者只能委派一层深。大于 1 的深度会被忽略。

专才们不能运行它们自己的子团队。这是刻意的——它让系统可预测、可追踪。

### 09. 在 Claude Console 里观看整个过程

一个生产级多智能体系统和一个实验性系统之间的区别是可观测性。

每一次运行都在 Claude Console 里产生一份完整的 trace：哪个智能体做了什么、按什么顺序、为什么。你可以看到每一个委派决策，检查每一个子智能体的推理，从头到尾跟随这个序列。

![](images/img-06.jpg)

当一个结果是错的，trace 告诉你哪个专才失败了，以及问题是出在委派还是专才本身。不要盲目地运行一支团队——读 trace。

### 10. 扩展到 20 并加上共享记忆

一旦小团队有效，就扩展它。把专才加到 20 个智能体的 roster 上限，让协调者并行地扇出穿过它们全部。

然后用共享记忆闭合这个循环。当许多子智能体在同一个领域工作时，Dreaming 功能可以聚合它们集体学到的东西，并把共享的洞见发布到一个团队范围的记忆库——某种没有单个智能体会话能独自产出的东西。

这支团队不只是并行工作；它作为一个整体随时间变得更聪明。

这就是 Netflix 平台团队在生产中运行的：多智能体编排处理来自数百个同时构建的日志，并行子智能体在数千个应用之间浮现出反复出现的问题——在单智能体设置里这本会是无可救药地顺序的工作。

## 那些会搞垮智能体团队的错误

- **在一个智能体就够用时搭建一支团队。** 多智能体花费更多，协调更慢。如果工作不能并行化、专业化或升级，你就白白添加了复杂度。
- **一个自己做工作的协调者。** 如果 lead 智能体有的是领域指令而不是委派逻辑，你搭建的就是一个穿着团队戏服的臃肿单一智能体。
- **松散的工具范围。** 当每个专才都能接触一切时，专注崩塌，trace 变得无法阅读。把每个智能体的范围限定到恰好它的工作。
- **对抗深度 1 的限制。** 协调者委派一层深。设计一个隐藏的子协调者层级是浪费时间——那个深度会被忽略。
- **盲目运行。** Console 的 trace 存在就是为了让你看到哪个智能体做了什么。跳过它，你就无法调试一个有运动部件的系统。

## 结论

大多数人会继续往一个智能体里塞更多能力，看着它变慢、退化，然后得出结论说智能体就是还没准备好。

那些搭建团队的人将拥有不同的东西：一个委派的协调者、用自己的上下文并行工作的专才、一个他们协作于其上的共享文件系统，和一个让整个团队随时间更敏锐的记忆库。

挑一个能拆分成并行片段的任务。规划三个专才和一个协调者。先搭建那支小团队。仅这一点就会改变你的智能体能处理多少。
