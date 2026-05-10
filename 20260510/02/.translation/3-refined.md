# 如何用AI搭一套内容系统（顺便拿到500万次曝光）

**作者：** Shann³ ([@shannholmberg](https://x.com/shannholmberg))  
**日期：** 2026年5月8日  
**来源：** [How to Build Your Content System with AI](https://x.com/Zephyr_hg/status/2052780393326092407)

一套能找想法、用你的口吻起草、自动发布、还能从数据里学习的系统。它让我的账号两周内获得500万次曝光，两个月内收到10万次书签。

内容好不好，取决于背后的人和系统。想法没用心找、写作没用心做，出来的内容自然也不会好。

这篇文章帮你从零开始搭自己的内容护城河。

我做了一件事——把整个系统只对一件事优化：

> 让人想收藏的内容

就是那种让读者觉得"值"，忍不住点下书签、存进自己的知识库、以后还会翻出来看的帖子。

我的百万曝光帖子是这样的：

![](images/img-01.jpg)

![](images/img-02.jpg)

**这篇文章你能拿走什么**

每一节都可以直接复制、改一改，这周就用在自己的账号上。

- 完整的内容操作系统框架，对应你今天就能建好的实际文件夹
- 四个可直接粘贴进 Claude 或任何主流大模型的提示词
- V1 起步版本，前期花1-2小时，之后每周省下同样的时间
- 作者上下文包模板，把模糊的想法变成有方向的草稿

![](images/img-03.jpg)

## 先看结果，再聊方法

我运营自己的 X 账号。做这套系统之前，账号有名字、有几千粉丝，但我基本没怎么管它。

没有什么系统可言，就是偶尔发发帖子，数据也稀稀拉拉。

后来我坐下来，认真搭了这篇文章里讲的这套东西。

两周，500万曝光，从一个几乎沉寂的账号开始。之后每周迭代。到第二个月，同一个账号超过1100万次浏览、10万次书签。

![](images/img-04.jpg)

我是 @LunarStrategy 的联合创始人，我们也在为客户部署类似的内容操作系统。

## 有一条原则不能妥协

机制之前，先说这套系统运转的根本规则：

**草稿永远不能直接发，每一篇都要自己手动收尾。** 系统是加速器，不是自动驾驶。你要是让它全自动跑，它会慢慢变烂。

目标不是用提示词模仿一个声音。而是从你真实的写作里提炼出一套可以复用的资产。把这件事做一次，保持更新，之后模型生成的每一稿都会离你更近——你的时间可以用在真正需要打磨的地方。

## "值得收藏"到底是什么意思

收藏是读者对未来的自己许下的一个小承诺：这个以后还用得上。这比点赞的门槛高得多，算法对它的处理方式也不一样。

我不想过度解读排名的数学逻辑，但作为每周都在跑这套系统的人，这个规律是稳定的：书签是对"未来实用性"的投票，拿到书签的帖子，发布很久后还会持续出现在信息流里。

每次发帖之前，我都会问自己：这帖子长得像下面这些之一吗？

- 清单
- 蓝图
- 文件夹结构
- 模板
- 框架
- 分步工作流
- 带结论的截图证明
- 前后对比
- 可复用的心智模型

如果一篇草稿一个都不像，那通常不该发。

![](images/img-05.jpg)

## 整个系统，一张图说清楚

我既不用一个巨型提示词，也不是堆一堆通用文件夹。我用的是围绕一个核心思路构建的系统：每一条内容都是一个对象，从有想法那一刻起，到发布，它一直带着自己的状态走。

```
┌──────────────────────────┐   ┌──────────────────────────┐
│ 外部：信号层              │   │ 内部：知识图谱             │
│                          │   │                          │
│ X书签、文章、             │   │ 个人操作系统、笔记、        │
│ 转录文字、私信、           │   │ 日记、语音备忘录、          │
│ 回复、竞品帖子            │   │ 已发布的内容存档           │
│                          │   │                          │
│                          │   │                          │
│ 用途：改写、              │   │ 用途：原创、               │
│ 研究+构思                 │   │ 再加工                    │
└─────────────┬────────────┘   └─────────────┬────────────┘
              │                              │
              └──────────────┬───────────────┘
                             ▼
           ┌────────────────────────────────────┐
           │ 策略 + 声音 + 存储                  │
           │ 定位、声音档案、                    │
           │ 避免烂内容主文档、想法、钩子、        │
           │ 证明库、反馈日志                    │
           └────────────────┬───────────────────┘
                            │ 输入到
                            ▼
           ┌────────────────────────────────────┐
           │ 生产负责人                          │
           │ 打开运行文件夹，通过想法门路由，      │
           │ 执行门控                            │
           └────────────────┬───────────────────┘
                            │ 创建
                            ▼
           ┌────────────────────────────────────┐
           │ 运行文件夹（每个内容对象一个）        │
           │                                    │
           │  想法 ─► 简介 ─► 草稿 ─► 验证       │
           │  ─► shann审核 ─► 调度器             │
           │  ─► 反馈                            │
           └────────────────┬───────────────────┘
                            │ 输出时写回
                            ▼
           ┌────────────────────────────────────┐
           │ 存储                               │
           │ 赢家、输家、声音规则、               │
           │ 禁用模式、钩子、证明               │
           └────────────────────────────────────┘
```

上下文存在两个地方。

**信号层**是你从外部拿进来的所有东西：这周存下的书签、监控列表上创作者的内容、你觉得不错的一篇文章。

**知识图谱**是你自己本来就有的：个人操作系统、笔记、日记、语音备忘录，以及你已经发过的所有内容。

路由决定这次从哪个来源取素材；策略+声音+存储层夹在两者和作者之间，负责过滤整理，确保上下文是精选过的。

每一篇帖子、文章、推文串或活动，都作为一个新的运行文件夹打开。这个文件夹就是内容对象。它从系统的共享部分取数据，经过一道道门控走完生命周期，发布时把学到的东西写回存储。

**一个内容对象的完整生命周期：**

```
已捕获
  → 想法审核（路由：原创 / 再加工 / 改写 / 研究+构思）
  → 简介就绪
  → 起草中
  → 验证
  → shann草稿审核
  → 已批准
  → 调度器就绪
  → 已调度
  → 已发布
  → 24小时反馈
  → 72小时反馈
  → 已学习
```

**围绕运行文件夹的各个部分：**

- **策略。** 定位、受众、内容支柱、来源监控列表。整个系统里唯一我自己手动维护的部分。如果让AI来写你的定位，你得到的不是定位，只是均值。
- **声音。** 声音档案和避免烂内容主文档。每个代理动笔之前都要读一遍。
- **存储。** 原始输入的收件箱、待处理工作板、想法积压、钩子库、证明库、反馈日志。运行文件夹读取和写回的共享记忆。
- **模块。** 作者技能（SKILL.md、参考资料、模板）。生产代码。系统中每个角色对应一个模块。
- **工作流。** 把内容对象从一个状态推进到下一个状态的剧本：从想法到发布、验证清单、调度器交接、反馈循环。

![](images/img-06.jpg)

## 四条路线

内容对象进入起草之前，想法门会做一个判断：这是哪种类型的内容？

四条路线，各有对应的简介、参考资料和门控：

**原创。** 直接从你自己或你的第二大脑创作（个人操作系统、笔记、日记、语音备忘录、脑子里盘了好几周的想法）。简介依赖你的基础：定位、证明库、内容支柱。没有外部来源。这条路最考验你的审美和判断。

**再加工。** 把已有的内容延伸出去。从文章里拆出一个推文串、对一篇爆款帖子做自我引用回复、把某一段内容单独拎出来发帖。骨架还是你的，形式变了。

**改写。** 从信号层拿外部素材（值得回应的推文、值得拆解的文章、有用框架的转录文字），用你自己的视角和声音重新表达。简介里会明确写清楚：保留什么、标注出处在哪、哪些声音规则适用（参考避免烂内容主文档）。

**研究+构思。** 先探索一个话题，研究规律，生成候选角度，不急着起草。输出不是一篇帖子，而是一个打磨过的想法或一组角度，存进 stores/ideas/ 供后续生产用。

![](images/img-07.jpg)

每条路线依然产出一个运行文件夹，路线在 content-object.md 里声明：

```
runs/active/2026-05-bookmark-flywheel/
  content-object.md   # 路线、当前状态、下一步行动
  idea.md             # 想法门的决策
  brief.md            # 作者交接文件（原创、再加工、改写时使用）
  draft-package.md    # 渲染后的草稿、验证输出、审核笔记
  feedback.md         # 24小时 / 72小时学习记录
```

## 这之前我做了什么

在这套内容操作系统之前，我搭过一个四代理系统，跑的是同一个循环的早期版本：研究者、想法生成者、作者，加一个在它们之间路由的编排者。每个代理都有自己的记忆，跨会话持久化。

整套东西我在 Claude Code 里搭的，用 Markdown 提示词、数据库和 CLI 工具。

![](images/img-08.jpg)

它跑通了。但搭得太重了。四个代理，做的事情结构上只是三个生产步骤加一个反馈循环。跑过这套系统之后，我明白了大多数关于代理群的文章没说清楚的东西：

> 代理的数量不是关键。给作者提供信息的知识层，才是。

现在这套是更精简的版本。代理更少，工作流更多，循环一样，输出更清晰。

## 今天你就能建好的文件夹

不需要什么复杂基础设施才能开始。你需要的只是：一个放共享内容的目录，和一个每条内容发布之前暂住的地方。

我的结构长这样：

```
/content-os
  /strategy
      positioning.md
      audience.md
      pillars.md
      source-watchlist.md

  /voice
      voice-profile.md
      master-avoid-slop.md

  /stores
      inbox.md
      workboard.md
      ideas/
      hooks/
      proof/
      feedback/

  /runs
      /active
          /2026-05-bookmark-flywheel
              content-object.md
              idea.md
              brief.md
              draft-package.md
              feedback.md
      /archive

  /modules
      /writer
          SKILL.md
          references/
          templates/

  /workflows
      idea-to-published-post.md
      verifier-checklist.md
      scheduler-handoff.md
      feedback-loop.md
```

runs/active/ 是核心。里面每个文件夹是一个内容对象。一条内容对应一个运行文件夹，这个文件夹带着自己的状态，直到发布、存档。

Notion、Obsidian、git 仓库、共享云盘，用什么都行。形式比工具重要。

## 你的 V1 起步

预留1-2小时的前期投入。做完之后你不会觉得"搞定了"，但你会真正开始——这才是最重要的状态。这里花的时间，之后每周都会还给你：下一篇草稿从有上下文的地方开始，而不是从零。

**第一步。** 搭骨架。建六个顶级目录：strategy、voice、stores、runs、modules、workflows。在 runs 里加 active/ 和 archive/，其余先留空。

**第二步。** 填策略。打开 strategy/positioning.md、strategy/audience.md、strategy/pillars.md，各写三到五行。支柱是你真正有资格聊的三四个话题。受众是一个具体的人，不是某个用户群体。

**第三步。** 写声音锚点。放进 voice/voice-profile.md（你始终坚持的5条规则、从不用的5种写法、2-3篇你状态最好时写出来的参考帖子），再开一个 voice/avoid-slop.md（用下面那一节的8种模式作起始过滤，每次有风格漏洞溜过就往里加）。在 stores/proof/ 里放十条具体证明——数字、名字、你做过的项目、亲身经历的例子。

**第四步。** 往 stores/inbox.md 里放十个想法。其中一半应该来自你这个月在私信或通话里已经说过的事情，不要现场编。

**第五步。** 为一个想法建运行文件夹。创建 runs/active/2026-05-{你的标签}/，在里面写 content-object.md（id、状态、格式、支柱）和 brief.md（作者上下文包模板，见下文），然后把这份简介交给写作模型。

**第六步。** 读草稿，关闭循环。模型会在同一个运行文件夹里返回 draft-package.md。拿去对照验证清单和避免烂内容主文档检查一遍。通过就排期发布，不通过就带着一条具体意见发回去修。发布后，写 feedback.md，把文件夹移进 archive。

![](images/img-09.jpg)

## 作者上下文包

这里是大多数人踩坑的地方。他们把整份品牌文档、整个知识库、整条信息流都塞进一个提示词。

结果模型写出来的是安全的废话——因为上下文里没有任何一件事是真正承重的。一个精简的包，几乎永远比一个塞满的上下文窗口更有效。

包以 brief.md 的形式存在运行文件夹里。每个内容对象一份，在起草开始之前写好。

复制这个模板：

```
作者上下文包
─────────────────────
论点：        这篇帖子必须证明的那一句话
读者：        应该存下它的那个具体的人
证明：        我可以用的数字、截图、故事
角度：        意想不到的切入框架
约束：        格式、长度、语气、禁用词汇
声音锚点：    2-3行听起来像我的句子
风险：        什么会让这篇看起来像AI写的，或令人尴尬
未解决问题：  我还不知道的，作者应该标注出来的
```

## 书签评分标准

草稿进排期之前，先打分。每项0分、1分或2分：

- 为读者省掉了未来的一项任务
- 包含证明（数字、截图、具名案例）
- 提供可复用的收获（模板、清单、框架）
- 有具体的受众和它要解决的任务
- 没有我在场也能用
- 有强有力的截图或视觉内容

满分12分。我自己的门槛是8分。低于8分的草稿不是丢掉，而是退回去重新对照包来改。大多数"差"草稿，其实只是在某一项上偷了懒。修那一项，重新打分，再发。

这套标准也是带新协作者最省事的方式。你不用抽象地讲什么叫好内容——把标准给他们，指三篇爆款帖子，让分数说话。

## 避免烂内容主文档

评分标准告诉你这篇帖子值不值得发。避免烂内容文档告诉你这篇帖子听起来像不像一个人写的。

每一篇草稿发布之前，我都会跑一遍这份文档。里面有54种模式，分三个严重程度，每种都有具体的改写示例。它能抓住这些东西：

- 促销腔（"突破性的"、"颠覆性的"）
- 重要性膨胀（"关键时刻"、"有力证明"）
- 模糊归因（"专家认为"、"研究表明"）
- 假主体（"系统自我复利"、"数据告诉我们"）
- 修辞铺垫（"问题是你是否X"）
- 碎句堆砌（"没有X。没有Y。没有Z。"）
- 破折号泛滥（目标是零）
- 填充副词（"实际上"、"字面上"、"悄悄地"）

作者代理起草之前要读这份文档，验证者批准之前也要读。

这就是"AI写的"和"一个用了AI的人写的"——两者的区别就在这里。

## 四个你可以直接抄的提示词

简短、有边界、留着让你改的。把它们当起点，不是万能公式。

每个都对应系统的一个层。粘进 Claude、GPT 或你用的任何模型里都行。如果只能留一个，留最后那个事后分析的。

### 提示词1：品牌基础提取

对应：strategy/ + voice/

```
ROLE
You are helping me build the foundation layer of a personal-brand
content system. You will turn raw, half-formed notes about my
work, audience, and voice into a tight set of operating documents
my writer agent can use to draft in my voice.

INPUT
I will paste raw notes covering: what I do, who I help, what I
have shipped or built, how I sound when I write, the kinds of
people I want as readers, and anything I refuse to sound like.

PROCESS
1. Read the notes. Note any contradictions or gaps.
2. Ask me up to 5 clarifying questions. Do not skip this step.
3. Once I answer, produce the six artifacts in OUTPUT FORMAT.
4. Flag anything you had to invent or guess. Mark it "assumed".

OUTPUT FORMAT
1. positioning. one sentence. the line a stranger should be able
   to repeat back after one of my posts.
2. audience. one specific person, by role, situation, and stake.
   not a segment.
3. pillars. 3 to 4 topics I have earned the right to talk about,
   each with a one-line reason I am credible on it.
4. voice rules. 5 things I always do.
5. banned patterns. 5 things I never do.
6. proof bank. 10 concrete things I can reference (numbers,
   names, shipped projects, lived examples).

RULES
- If a section is generic, mark it "missing" and tell me what
  you need from me.
- Do not invent numbers, customers, or projects.
- Use my own words wherever possible. Lift phrases from the notes.
- The output should fit on one page. Tight is the point.
```

### 提示词2：书签评分

对应：stores/ideas/（想法门）

```
ROLE
You are a critic who has read 10,000 high-bookmark posts and
1,000,000 forgettable ones. You can tell, line for line, what
makes a reader save a post versus scroll past.

INPUT
A post idea or a draft. Could be a one-line thesis, a rough
sketch, or a full draft.

PROCESS
1. Read it once for the surface read.
2. Score it 0, 1, or 2 on each row of the rubric below.
3. Total it out of 12.
4. If under 8, name the single row that would lift the score
   most, and how.

RUBRIC
- saves the reader a future task
- includes proof (numbers, screenshot, named example)
- gives a reusable takeaway (template, checklist, frame)
- has a specific audience and job-to-be-done
- can be applied without me being in the room
- has a strong screenshot or visual

OUTPUT FORMAT
- Total score: X / 12
- Strongest row: [row] (why)
- Weakest row: [row] (specific fix, in one line)
- Verdict: ship / fix and re-score / kill

RULES
- Do not pad the score to be encouraging.
- Do not suggest "make it more engaging." Tell me what to add or cut.
- If the idea is well below 8, say "kill" and tell me why directly.
```

### 提示词3：作者上下文包

对应：runs/active/{标签}/brief.md

```
ROLE
You are the production lead for my content system. Your job is
to turn one approved idea into a writer context packet, which
is a tight, shaped brief that gives the writer enough to draft
sharply without flooding the model with my entire knowledge base.

INPUT
- One approved idea (thesis, format, target reader)
- Pointers to my foundation files (positioning, audience, pillars,
  voice rules, banned patterns, proof bank)
- Any source material specific to this post (screenshots,
  transcripts, conversation notes)

PROCESS
1. Restate the idea in one sentence to confirm you understood it.
2. Pull only the slices of my foundation files this post needs.
3. Fill in the packet template below.
4. For any field you can't fill, write "missing" and list exactly
   what you need from me.

OUTPUT FORMAT
thesis:        one sentence the post must prove
reader:        the specific person who should save it
proof:         numbers, screenshots, stories I am allowed to use
angle:         the unexpected framing
constraints:   format, length, tone, banned phrases
voice anchors: 2-3 lines that sound like me
risks:         what would make this read as slop or cringe
open loops:    what I do not yet know, that the writer should flag

RULES
- Smaller is better. Aim for 400-900 tokens.
- Do not paste my full foundation files. Pull only the slices
  this post needs.
- Refusal is allowed. If you do not have enough to write a sharp
  packet, say "I do not have enough context" and ask for the one
  missing piece you need.
```

### 提示词4：病毒式事后分析（重点用这个）

对应：runs/active/{标签}/draft-package.md，审核前最后一关

```
ROLE
You are reading a post that already crossed 1M views and 10K
bookmarks one week from now. You are not writing it. You are
explaining, after the fact, why it landed.

INPUT
A draft, ready for the final pass.

PROCESS
1. Read the draft.
2. Point at specific lines that did the work.
3. Name the hook move.
4. Name the proof that made it credible.
5. Name the line a reader would screenshot.
6. Name the line that made it save-worthy.
7. Name the line that made someone reply or send it to a friend.

OUTPUT FORMAT
- hook move: [exact line] (why it works)
- credibility: [exact line] (why a reader believes it)
- screenshottable line: [exact line]
- save-worthy line: [exact line]
- reply or share trigger: [exact line]
- weakest part: [exact line] (what to fix before shipping)

RULES
- Do not say "great post". Do not say "strong hook". Point at
  specific lines or admit you can't.
- If you cannot point at a line for any of the categories above,
  say so plainly. That is the row I need to fix before it ships.
- The whole point is the model cannot hide behind generic praise.
  Force it to point at mechanics.
```

最后这个是系统里杠杆最大的提示词。模型不能说"钩子很强"或"见解很好"，它必须指出具体的行。大多数通过验证者的草稿，用这个提示词跑还是会暴露问题——两者之间的差距，就是真正的编辑所在。

它跑在这篇文章上是这样的：

```
> /viral-postmortem on draft about content system with AI

hook move:
  "content is only as good as the person and the system behind it"
  names the cause directly, no setup, no preamble

credibility:
  "5M impressions in 2 weeks, from an account that had been near silent"
  specific timeline, honest starting state, anchors the proof

screenshottable line:
  "the unit of work is not 'another post.' it is something a
   reader wants to keep."

save-worthy line:
  "if you cannot fill the packet, you do not have a post yet.
   you have a vibe."

reply or share trigger:
  "the brain is the system."

weakest part:
  "two models, two roles" section
  the opus 4.7 + gpt-5.5 specificity will date fast
  generalize the principle, drop the model names
```

## 两个模型，两个角色

大量跑这套系统之后，我撞上了一件回头想想挺显而易见的事：

写作这件事，和运行系统这件事，是两种不同的工作，适合不同的模型。于是我不再用一个模型包打天下。

我目前的分工是这样的：

**作者（opus 4.7）负责：**
- 品味
- 节奏
- 信息密度
- 声音
- 真正的草稿

**编排者（gpt-5.5）负责：**
- 在各层之间路由
- 为作者打包合适的上下文
- 决定哪些内容传进去
- 跑验证者
- 向发布层交接

![](images/img-10.jpg)

## 在哪里跑这套系统

这种系统只有在编排者真正能干活的情况下才有效——它需要读写文件、调用工具、跑检查、按计划把批准的草稿交给发布层。所以真正的问题不是用哪个应用，而是系统住在哪里。

我见过两种跑得干净的方案。

**1. VPS + Claude Code。**

租一台小服务器，把 /content-os 文件夹放进 git 仓库，让 Claude Code 在上面跑工作流。你拿到完全控制权，一台自己的机器，定时任务跑每周复盘，脚本跑验证者，还有一个能接触同一批文件的 AI 编码助手。如果你喜欢自己掌控整套技术栈、对服务器不陌生，这条路适合你。

**2. Hermes 代理——我现在用的这个。**

它就是为这种形状的工作设计的：代理、技能、工具调用、文件和 git 操作、浏览器和搜索、定时任务，以及跨整个工作流持久化的上下文。把它指向你的基础文件、输入来源和包模板，编排层负责衔接各步骤之间的工作，我把时间留在写作和编辑上。草稿在发布之前还是会来到我这里。

两个都不是必须的。核心原则是：把系统放在一个编排者能读写你的文件、调用它需要的工具、跑验证者、把批准的帖子交给 Postiz 的地方。选哪个，看你习惯怎么工作。

![](images/img-11.jpg)

## Postiz：发布层

草稿批准之后，进 Postiz，排队。

一个地方，搞定 X、LinkedIn、Instagram、Threads、TikTok、YouTube、Bluesky、Reddit 等平台的发布调度。

开源、可自托管，仓库是 gitroomhq/postiz-app，作者是 @wickedguro。

Postiz 是我让代理接触社交平台的地方，也是我的代理跨多个渠道发布和排期内容的框架。

![](images/img-12.jpg)

## 反馈循环是护城河

大多数人在发布之后就停了。而系统真正开始产生价值，是从发布之后。

我每周看：

- 浏览量
- 书签数
- 书签率
- 回复数

> 我最关注书签率。它告诉我哪些帖子真正赢得了"以后还会用到"，而不只是被滑过去。

爆款帖子连带它的数据一起复制进输入，作为下次的参考案例。表现差的帖子用来更新声音规则、禁用模式或想法过滤器。

下一个包会更准——因为这周我又学到了什么。
