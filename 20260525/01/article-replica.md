# 怎么搭一支 Claude 智能体团队：从一个，到 20 个一起干活

**作者：** Codez ([@0xCodez](https://x.com/0xCodez))  
**日期：** 2026年5月24日  
**来源：** [How to build a team of Claude agents in 10 steps](https://x.com/0xCodez/status/2058513716509913581)

在 Claude 上做多智能体编排，到底什么招管用？官方文档、cookbook、Netflix 和 Spiral 的真实配置，我都翻了一遍，最后揉成了这一篇。

你先收藏起来。读完之后，你大概就明白怎么把一个累趴下的智能体，拆成一支最多 20 人、能一起开工的团队了。

想接着看新鲜的 AI 内幕，可以关注我的 Substack：movez.substack.com

别觉得我在吹。放在 2026 年 4 月之前，这事得搭好几个月的基础设施。现在呢，一份 YAML 配置，外加 10 个步骤，就成了。

## 一个智能体，是怎么一步步撞上墙的

事情通常是这样的。

你做了一个智能体，一上手，挺好用。既然好用，那就多交给它点事吧。

加个查资料的能力，再加上写报告，顺手把数据分析也塞进去，最后还想要它自己过一遍审查。每加一样，系统提示就长一截，工具列表就胖一圈，上下文窗口也跟着更挤。

然后某一天你忽然发现，它反应慢了，话也说不到点子上了，连以前闭着眼都能做对的事，现在也磕磕绊绊。

这时候很多人会怪模型不行。其实不是模型的事，是架子搭错了。

道理不难想。一个智能体就一个上下文窗口，你往上加的每样本事，都在跟别的本事抢那点有限的注意力。东西堆到一定程度，一个啥都管的"全才"，反而干不过十个各管一摊的"专才"。

所以真正的出路，不是把提示写得更长，而是把活分出去——组个团队。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGVhMjkzNjQwYTgwNmVjNjU4NzY3ZTYxNWU3ODJmMmNfZDJmNzcwNGQ2MWY3Y2NkNDAxMGYwMjMxYTdiYjE3NDVfSUQ6NzY0MzY2ODk4ODM5MzA4MjA1Nl8xNzc5NjgwMzk5OjE3Nzk3NjY3OTlfVjM)

这套团队的底子，文档里讲得很清楚，就三条：一个名册里最多能放 20 个不同的智能体；每个都待在自己单独的上下文窗口里，互不打扰；可它们又共用同一个文件系统。各想各的，活却摊在一块儿——一支团队能并行干活又不乱，靠的就是这个。

## 先想清楚：要不要组队，怎么组

### 01. 先掂量掂量，你是不是真需要一支团队

别一听"多智能体"觉得高级就往上冲。它更费 token，还凭空多出一层协调的麻烦。

下面三种情况，碰上一种，再考虑组队也不迟：

- **活儿能拆开同时干。** 比如几个互不相干的子任务，各管各的日志文件、各管各的代码模块。一个智能体只能一件一件来，一支团队能一起上。
- **不同的活儿要不同的行家。** 一个盯安全审查，一个写文档，一个算定价。这些事让同一个"全才"来回切换着做，结果往往是哪样都做不利索。
- **大部分简单，偶尔冒出个硬骨头。** 多数活很轻松，但总有几个子任务出奇地难。这时团队可以把难的单独拎出来，交给更强的模型，而不用每一步都花那份贵钱。

### 02. 别急着写代码，先把角色理顺

说白了，设计多智能体，跟设计一个团队是一回事。

所以动键盘之前，先拿张纸把团队画出来：一个协调者，再列一串专才，每个专才认领一件明确的活。

可以找个现成的样子照着来。Anthropic 文档里就有个事件响应的例子：一个主智能体管全局调查，底下几个子智能体同时铺开，分头去翻部署记录、错误日志、监控指标和用户工单。

四个专才加一个协调者，本来一个智能体得排着队做完的事，这下并排着就干完了。

每个角色，起个名，写一句话说清它干啥，标上用什么模型、给哪些工具。要是发现两个角色干的活重了，干脆并成一个。专才这东西，宁可少而准，也别多而虚。

### 03. 给每个角色单独挑模型——钱就省在这

这一招很多人没留意：团队里每个智能体，都能跑不一样的模型，你压根没被绑在一个上面。

Spiral by Every 的实际做法就是个现成例子——他们让 Haiku 当协调者，让 Opus 去当真正动笔写东西的子智能体。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjE5NDUyMzI2MTcwNTc5YjJiM2ZhYjM0MjY0ZmJiMDJfYjUwMzIzMDUwMTQ2ZDM3N2E1NTFjNTI0Mzk0MzA1ZmFfSUQ6NzY0MzY2ODk5OTUyMzg5NjUyMV8xNzc5NjgwMzk5OjE3Nzk3NjY3OTlfVjM)

想想也对，协调者无非是派活、排顺序，这种事一个又快又便宜的模型就办妥了。真正烧钱的重活，只留给那几个非它不可的专才。

模型对着活来挑。按角色配不同档位，这是省钱又提速最大的一个抓手。

## 动手搭团队

### 04. 先把 Managed Agents 配好

每个多智能体请求都跑在 Claude Managed Agents 上，得带一个 beta 头 `managed-agents-2026-04-01`。这个 SDK 会替你自动加上，不用操心。

那为啥非得用 Managed Agents，不自己搭一套？道理在这儿：团队一旦要远程跑、要扛很多用户、要共用文件系统、还要把状态存下来，你立马就撞上一堆基础设施的活——会话、内存、安全、沙箱，全得自己管。

这些 Managed Agents 都替你兜住了，你只管专心设计团队。装好 Anthropic SDK，去 Console 把 API key 填上，就能开工。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDQ1NWZhOGMwYjEzZDcxN2EwOWMxNDk4Y2MxMjE3MzZfYmU2NjI3YzliN2NkYzVhNWE1MzlmY2JjMzE4OGEwN2RfSUQ6NzY0MzY2OTAwODU4MTAwNDQ5N18xNzc5NjgwMzk5OjE3Nzk3NjY3OTlfVjM)

### 05. 一个专才，就做成一个独立的智能体

搭的时候，从底下往上来，先把专才一个个立起来。

每个专才都是独立的智能体，有自己的模型、自己的提示、还有一套卡得死死的工具。建好之后，把它们的智能体 ID 记下来——回头协调者要点名用。

这里有一条最该守住：每个专才的工具，范围一定要卡紧。cookbook 里那个写销售提案的例子就很说明问题——研究者只给网页搜索，图书管理员只能读文件，算定价的那位，眼里就只有规则文件和席位数。

每个智能体只碰自己干活用得着的那点东西，别的一概不沾。这样它干活专注，整个系统出了事你也查得清。

### 06. 立一个协调者，把名册报上

接下来轮到主智能体。你只要给它设上 `multiagent` 字段，把它能指挥的子智能体 ID 列出来，它就成了协调者。这份配置故意写得很短：

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

里头那个 `agent_toolset_20260401` 工具是关键，正是它，协调者才有了往外派活的本事。这份名册，最多能列 20 项。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTgyNTBjYTVhYWIzNGMwNDM3ZmQ1ZTliZDQxMTViNDVfNTEzMzM1ODg4ZGFhOWUxYzQyOTA2OTA3OWNiNjU3ZDBfSUQ6NzY0MzY2OTAxOTA3Mjk1NzYzMF8xNzc5NjgwMzk5OjE3Nzk3NjY3OTlfVjM)

你可以钉死某个具体版本的智能体，也可以总用最新的；还有个有意思的写法，`{"type": "self"}`，让协调者派生出自己的副本，自己指挥自己，绕着圈地并行。

### 07. 协调者的提示，要当个领导写，别当个干活的写

一支团队成不成，就看这一步。

协调者的系统提示，不该自己埋头干活，而该把"怎么把活分下去"讲明白。

一份好的协调者提示，大概是这么个意思：手下有哪几个专才，各管什么，活来了该派给谁，他们干完了又怎么把结果拼起来。它操心的是排顺序、做汇总，至于具体的领域细节——那些都该交给专才。

有个简单的自检：要是你发现自己正往协调者里写领域细节，那就说明这段话写错地方了，该挪进某个子智能体。

下面这份，是真实的事件响应团队用的协调者提示。你留意一下，它自己从头到尾不查任何东西，只管派活和汇总：

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

你看，每一行讲的都是派活、找关联、定输出格式。真正搜日志、读指标的脏活，全在专才那边——本来就该在那儿。

## 跑起来，盯着看，再慢慢改

### 08. 先弄明白这支团队是怎么互通消息的

真把协调者跑起来，里头的门道挺具体，值得你了解一下。

协调者每往一个子智能体派一次活，就会开出一条它专属的会话线程——一条单独的事件流，上下文互不串，各记各的历史。协调者在主线程里汇报进度，而新的线程，会在它派活的当口实时冒出来。

还有一点很要紧：这些线程是存得住的。协调者可以回头给一个之前用过的智能体再补一句，那个智能体还记得前几轮聊过的全部内容。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDZjMmNlYmJhMDZkYWZhZWZiOWM5ZjlmODZjYmZmYTJfMWFmYWJiZjZlNTYzN2RmYjE5NDUxMjEzZTU5MzUyODFfSUQ6NzY0MzY2OTAyNjgzMDEyNjI3MF8xNzc5NjgwMzk5OjE3Nzk3NjY3OTlfVjM)

这里有条硬规矩，你得绕着它来设计：协调者只能往下派一层，再往下的层级会被直接无视。

也就是说，专才不能再自己拉一支小队出来。这是故意的——这么一卡，整个系统才好预判、好追查。

### 09. 在 Claude Console 里盯着整件事

一套能真上生产的多智能体系统，跟一套还停在实验阶段的，差别就在一句话：你看不看得见里头发生了什么。

每跑一次，Claude Console 里都会留下一份完整的 trace：哪个智能体干了啥、按什么先后、为什么这么干。每一个派活的决定你都看得到，每个子智能体的推理你都能点开，整条链能从头跟到尾。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDg3ZGIyMTQ4MGVlNTNiMzMwOTUxNjFjNDBmMjg3MTdfOTQ3YjdkMWU0ZWM4NmJjNDU5NTM0NmExZjBlYjI5ZDZfSUQ6NzY0MzY2OTAzMzQ4MTM1ODUzOF8xNzc5NjgwMzk2OjE3Nzk3NjY3OTZfVjM)

哪次结果出岔了，trace 会直接告诉你是哪个专才掉链子，问题是出在派活上，还是专才自己。所以别蒙着眼睛跑一支团队——先把 trace 读一遍。

### 10. 扩到 20 个，再给它加上共享记忆

小团队一旦跑顺了，就把它做大。专才一直加，加到 20 个的名册上限，让协调者一口气把活铺到所有人头上。

然后，用共享记忆把这个圈给闭上。当一大群子智能体都在同一个领域里干活时，Dreaming 这个功能能把它们各自学到的东西汇到一起，再把共享的心得写进一个团队级的记忆库里——这种东西，单靠任何一个智能体的会话，自己是攒不出来的。

到这一步，团队就不只是能一起干活了，它还会作为一个整体，越用越聪明。

Netflix 的平台团队在生产里跑的就是这一套：用多智能体编排，去处理上百个同时进行的构建吐出来的日志，一群并行的子智能体在成千上万个应用里，把那些反复出现的问题一个个挑出来。这些活要是交给单个智能体一件件做，根本做不完。

## 哪几个坑，最容易把团队带沟里

事情讲到这儿，反过来说说几个常见的栽跟头的地方。

- **一个智能体就够，你偏要组队。** 多智能体更花钱、协调也更慢。要是这活既不能并行，也不挑专长、不用升级，那你组队就是白添麻烦。
- **协调者自己跳下去干活了。** 要是主智能体装的全是领域细节，而不是怎么派活，那你做出来的，无非是个套了层团队壳子的、又胖又乱的单智能体。
- **工具范围放得太宽。** 要是每个专才啥都能碰，那专注立马就散了，trace 也乱得没法看。把每个智能体死死框在它该干的活上。
- **跟"只能派一层"这条规矩较劲。** 协调者就只往下派一层。你费半天劲搭个藏起来的多层子协调者，纯属白忙——那个深度系统根本不认。
- **蒙着眼睛跑。** Console 的 trace 摆在那儿，就是让你看清谁干了啥的。你要是跳过它，这么多环节的系统出了问题，你连从哪查起都不知道。

## 说到底

大多数人，会接着往一个智能体里拼命塞能力，看着它越来越慢、越来越差，最后摇摇头：智能体啊，还是没到时候。

而那些动手组团队的人，手里攥着的是另一样东西：一个专心派活的协调者，一群各带各上下文、并排干活的专才，一个供大家一起协作的共享文件系统，还有一个让整支团队越来越敏锐的记忆库。

不用想太大。挑一件能拆成几块、同时去做的活，配上三个专才加一个协调者，先把这支小队搭起来。光是这一步，你就会发现，你的智能体能扛的，比原来多得多。
