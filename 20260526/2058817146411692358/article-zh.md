# 如何构建一个真正能协同工作的 AI 智能体团队（完整课程）

**作者：** Kanika ([@KanikaBK](https://x.com/KanikaBK))  
**日期：** 2026年5月25日  
**来源：** [How to build a team of AI Agents that actually work together (Full Course)](https://x.com/KanikaBK/status/2058817146411692358)

大多数人构建一个 AI 智能体，看着它在复杂任务上栽跟头，于是断定 AI 智能体还不成熟。但真正的问题出在架构上。这门完整课程会讲清楚：要构建产出可靠、高质量的多智能体系统，你需要怎样的心智模型、团队结构、工具和生产模式。

把一个复杂任务交给单个智能体，就像雇一个人同时做研究、写作、设计、编码和发布，还得记住每一步的每个细节。

任务一复杂，它就垮了。解决办法，是人类团队几百年前就想明白的：专业分工、清晰的角色，再加一个负责协调的管理者。

这是一门完整的课程，教你构建一个真正能协同工作的 AI 智能体团队——从心智模型，到工具，再到可直接用于生产的模式。

我尽量把自己构建 AI 智能体过程中能想到的每个要点都写了进来。希望你准备好了！

## 核心的思维转变

在你写下第一条提示词之前，得先改变你看待智能体的方式。

### 用任务来思考，而不是角色

构建多智能体系统时，最常见的错误是照搬人类的组织架构图。你建一个"研究智能体"、一个"写作智能体"、一个"营销智能体"，然后纳闷：为什么输出忽好忽坏，还特别难调试。

真正能扭转局面的，是这个转变：用任务来思考，而不是角色。

AI 智能体表现最好的时候，是它有一个明确目标、一组有限的特定工具，以及针对单个具体任务的精确指令。一个什么都管的智能体，决策就会含糊。一个任务很窄的智能体，输出才会稳定、可靠。

所以别建一个"内容智能体"，而是拆成：

- 研究任务智能体——接收一个主题，返回结构化的研究笔记。
- 简报撰写智能体——接收研究笔记，返回一份内容简报。
- 草稿撰写智能体——接收简报，返回一份完整草稿。
- 编辑智能体——接收草稿，返回带批注的修改版。
- 发布智能体——接收最终文稿，做好格式并发布。

每个智能体都简单、好测试、可替换。但合起来，整个系统就很强大。

### 为什么多智能体系统胜过单个智能体

MIT 和 Google Brain 的研究发现，当智能体相互辩论、相互挑刺时，推理质量和事实准确性都会明显提升——哪怕一开始有个智能体答错了，其他智能体的批评也会把方向拽回来。

多智能体系统的意义不只是并行干活，更在于靠专业分工和相互验证换来的质量。

## 第 1 部分：四个核心智能体角色

每个真正好用的多智能体团队，都有覆盖四类功能的智能体。你不必每类配一个智能体，但任何一个生产团队，这四项功能都得齐。

### 角色 1：编排者（管理者智能体）

编排者接到顶层任务后，把它拆成子任务，再把每个子任务派给合适的专家智能体，收集大家的输出，最后综合出结果。它从不亲自动手，只负责协调。

它需要：

- 一份清单，说清它手下每个专家智能体分别是谁、各自干什么。
- 一套规则，知道什么时候该派活、什么时候该综合。
- 一道质量关卡，用来判断一个子任务的输出够不够好，能不能往下传。

下面是编排者的系统提示词示例：

![](images/img-01.jpg)

```
Prompt 1
You are a project manager overseeing a team of specialist AI agents.

Your team:
- Research Agent: searches the web and returns structured summaries
- Writer Agent: takes a brief and writes long-form content
- Editor Agent: critiques drafts and returns specific improvements
- Publisher Agent: formats content and posts to the target platform

When given a task:
1. Break it into discrete subtasks
2. Assign each subtask to the appropriate agent
3. Review each output before passing it to the next agent
4. Return the final synthesized result

If an agent's output does not meet the quality criteria, return it with specific feedback and request a revision.
```

### 角色 2：研究者

研究者唯一的工作，就是查找、检索、整理信息。它不写作、不分析、不创作，只负责收集。

它需要：

- 网络搜索工具（Perplexity API、Serper、Brave Search API）
- 一个能读取整页内容的 URL 抓取器
- 一套结构化的输出格式，让结果方便下游智能体直接用

要求它固定输出的格式示例：

```
Topic: [topic]
Key Facts: [bulleted list]
Statistics: [with sources]
Competing Perspectives: [brief list]
Sources: [URLs]
```

### 角色 3：专家生产者

这些才是真正干活的，一个生产任务配一个智能体。常见的专家智能体有：

- 写作智能体：拿到简报，写出草稿。
- 编码智能体：拿到需求，写出代码。
- 数据分析智能体：拿到原始数据，给出洞察。
- 设计简报智能体：拿到一个概念，给出一份视觉设计简报。
- 外联智能体：拿到线索数据，写出个性化的消息。

每个专家智能体都该有：

- 一个范围收得很紧的系统提示词（只干一件事）。
- 干这件事所需的最少工具。
- 一个明确的输出格式，让下游智能体能稳定地解析。

### 角色 4：批评者 / 审阅者

在大多数智能体系统里，这是最被忽视、却最影响质量的角色。批评者接收任何一个智能体的输出，对照既定标准评估，再返回具体、能落地的反馈。

一个设计得好的批评者，不会只说"这写得不行"，而是会说：

- "引言把核心观点埋在了第三段。挪到第一句。"
- "第二段的说法没依据。补个来源，或者删掉。"
- "语气前后不一致——第 1 到 3 段很正式，第 4 到 6 段又很随意。统一一下。"

一个多智能体系统是只能产出平庸货色，还是能产出让你愿意署名发布的东西，差别往往就在这个批评者智能体身上。

## 第 2 部分：三种架构

多智能体团队，结构无非三种。先想清楚该用哪一种，几乎就决定了你之后怎么搭。

### 架构 1：顺序式（流水线）

智能体一个接一个地跑。A 的输出，就是 B 的输入。

```
输入 → 研究智能体 → 简报智能体 → 写作智能体 → 编辑智能体 → 输出
```

什么时候用：任务有清晰的线性流程，每一步都得等上一步正确做完。

最适合：内容创作、研究报告、提案生成、数据处理流水线。

风险在于：万一第二个智能体输出得不好，后面每个智能体都会把这个错误接着传下去。所以每一步之间都加一道质量关卡。

### 架构 2：并行式（扇出）

编排者把任务一拆，同时发给好几个智能体。大家一起干，编排者再收集、综合结果。

```
                       ┌→ 研究智能体 A → ┐
输入 → 编排者          ├→ 研究智能体 B → ├→ 综合智能体 → 输出
                       └→ 研究智能体 C → ┘
```

什么时候用：任务能拆成几条互不依赖的并行支线。这样能大大缩短总耗时。

最适合：多来源研究、同时分析多家公司的竞争态势、批量处理大量条目。

风险在于：综合很难。对于可能互相打架的并行输出，编排者得有一套明确的规则，知道怎么把它们拼到一起。

### 架构 3：分层式（多层）

编排分好几层。一个顶层编排者，管着几个中层编排者，每个中层编排者底下又管着一批专家智能体。

![](images/img-02.jpg)

```
CEO 智能体
├── 内容编排者
│   ├── 研究智能体
│   ├── 写作智能体
│   └── 编辑智能体
└── 分发编排者
    ├── SEO 智能体
    ├── 社交智能体
    └── 邮件智能体
```

什么时候用：任务复杂到需要协调好几条流水线，而不只是几个智能体。

最适合：端到端的业务流程自动化、复杂的研究与发布工作流、整套营销活动自动化。

风险在于：复杂度会迅速叠起来。每多一层，就多一份延迟、成本和出错的可能。只有当顺序式和并行式确实搞不定时，再上分层式。

## 第 3 部分：工具栈

### 无代码 / 低代码（从这里起步）

**Make（前身是 Integromat）**

构建多智能体工作流，最好用的可视化工具。通过 API 接上 Claude、OpenAI 或任何 LLM，可视化地搭出顺序流水线，不用写代码就能加上条件分支、错误处理和并行路由。

**n8n**

Make 的开源替代品。可以自己部署，更灵活，更适合带自定义逻辑的复杂工作流。自带 AI 智能体节点，支持工具调用。

**Relevance AI**

专门为多智能体系统做的。你可以创建带工具权限的智能体，把它们连成团队，再可视化地定义智能体之间怎么交接。做业务工作流自动化很强。

### 基于代码的框架（想要完全掌控）

**Claude API 配合工具使用**

直接用 Anthropic 的 Claude API 来搭智能体。每个智能体就是一个系统提示词加一组工具（它能调用的函数）。编排者拿任务调用 Claude，Claude 调工具，工具返回结果，Claude 再综合。

**LangGraph**

一个基于图的框架，节点是智能体，边定义交接关系。特别适合复杂的条件流程——下一个该轮到谁，取决于当前的输出。

**Agno（前身是 Phidata）**

专门为搭建带分层编排的智能体团队而设计的框架。内置了团队记忆、智能体之间通信和并行执行的支持。

**AutoGen（微软）**

一个多智能体对话框架，智能体之间直接互发消息。很适合那种需要在对话里反复辩论、挑刺、修改的智能体。

## 第 4 部分：手把手搭出你的第一个智能体团队

我们来搭一个"内容研究与写作团队"——一个三智能体的系统，接收一个主题，产出一份打磨过、有研究支撑的文章草稿。这是最实用的起点，而且这套架构能迁移到几十种别的场景。

![](images/img-03.jpg)

### 第 1 步：搭研究智能体

系统提示词：

```
You are a research specialist. Your only job is to research a given topic and return structured notes.

When given a topic and angle:
1. Search for the most relevant, recent, and credible information
2. Find 3–5 key insights, each with supporting evidence
3. Identify 2–3 competing perspectives or counterarguments
4. Find 2–3 specific statistics or data points with sources
5. Note any expert voices or credible sources worth quoting

Return your output in this exact format:
---
TOPIC: [topic]
ANGLE: [angle]
KEY INSIGHTS:
- [insight 1] (Source: [URL])
- [insight 2] (Source: [URL])
STATISTICS:
- [stat 1] (Source: [URL])
COUNTERARGUMENTS:
- [counterargument 1]
NOTABLE SOURCES:
- [source name]: [URL]
---

Do not write prose. Do not add commentary. Return structured notes only.
```

要给它的工具：网络搜索（Perplexity API 或 Serper API）、URL 抓取器。

### 第 2 步：搭写作智能体

系统提示词：

```
You are a skilled long-form writer. Your only job is to write a clear, engaging article draft from research notes.

When given research notes and a brief:
1. Write a compelling opening that hooks the reader immediately
2. Develop the key insights into full sections with clear subheadings
3. Use the statistics and sources naturally within the prose — never in a list
4. Address counterarguments honestly — they build credibility
5. Close with a clear, actionable takeaway

Writing standards:
- Active voice throughout
- Sentences under 25 words on average
- No corporate jargon, no filler phrases
- Every section should make one clear point
- Target length: 800–1,200 words unless specified otherwise

Return only the article draft. No meta-commentary about the draft.
```

要给它的工具：无。它只要研究笔记作为输入就够了。

### 第 3 步：搭编辑智能体

系统提示词：

```
You are a senior editor. Your job is to critique a draft and return specific, actionable improvements.

When given an article draft:
1. Identify the three most important structural issues (if any)
2. Flag any claims that need stronger evidence or sourcing
3. Mark any sections where the logic is unclear or the point is buried
4. Highlight the two strongest parts of the draft (what to protect)
5. Rewrite the opening paragraph to make it stronger

Return your output in this format:
---
STRUCTURAL ISSUES:
1. [issue + specific fix]
2. [issue + specific fix]
EVIDENCE GAPS:
- [claim that needs support]
CLARITY ISSUES:
- [paragraph/section + what is unclear]
STRONGEST SECTIONS:
- [section + why it works]
REVISED OPENING:
[rewritten opening paragraph]
---
```

要给它的工具：无。

### 第 4 步：搭编排者

系统提示词：

```
You are a content project manager. You coordinate a team of specialist agents to produce polished articles.

Your team:
- Research Agent: searches and returns structured research notes
- Writer Agent: writes an article draft from research notes
- Editor Agent: critiques a draft and returns specific improvements

When given a topic and angle:
1. Send the topic to the Research Agent. Wait for structured notes.
2. Review the notes. If they seem thin or miss the angle, ask the Research Agent for a second pass focused on [gap].
3. Send the notes to the Writer Agent with the original angle as context.
4. Send the draft to the Editor Agent.
5. If the Editor flags more than 2 structural issues, send the draft back to the Writer with the critique.
6. When the Editor gives a clean review (0–1 structural issues), return the final draft.

Always explain which step you are on and why.
```

### 第 5 步：连起来，测一遍

在 Make 或 n8n 里：

- 创建一个触发器（webhook 或手动表单）。
- 把它接到研究智能体（一次 Claude API 调用，带研究系统提示词加网络搜索工具）。
- 把输出传给写作智能体（一次 Claude API 调用，带写作系统提示词）。
- 把草稿传给编辑智能体（一次 Claude API 调用，带编辑系统提示词）。
- 把最终结果发到 Slack、Notion 或邮件。

拿五个不同的主题试一遍。看看流水线在哪一步卡住，就去收紧那一步的提示词。

## 第 5 部分：让智能体团队靠谱的五个模式

### 模式 1：强制结构化输出

团队里的每个智能体，都该按固定格式返回结果——别让它写自由发挥的散文。这样交接才靠谱。要是研究智能体爱用什么格式就用什么格式，写作智能体就得去猜它的意思，一猜就乱了。

所以在每个系统提示词里都写好输出模板。团队里每个智能体都该清清楚楚知道：自己收到的是什么格式，必须交出去的又是什么格式。

### 模式 2：在智能体之间设质量关卡

别把每个输出都自动塞给下一个智能体。中间加一个简单的评估环节——可以是编排者来审，也可以是一个专门的批评者智能体——在结果往下游走之前先检查一遍。

质量关卡问的是：这个输出，够不够下一步顺利做下去的最低标准？不够，就带着具体反馈打回去。正是这一步，挡住了单个掉链子的智能体拖垮整条流水线。

### 模式 3：只给智能体最少的工具

一个手里攥着 15 个工具的智能体，用起来会乱七八糟。一个只有两三个工具的智能体，用起来反而稳。工具要精确对应智能体要干的活：研究智能体配搜索和抓取，写作智能体什么工具都不给——它不需要外部信息，有上下文就行。

发布智能体，给它平台 API。

### 模式 4：内建一个重试循环

每个上了生产的智能体团队，都得有重试机制。当一个智能体的输出没过质量关卡，它该带着具体反馈再来一次——而不是把原来的提示词原样再跑一遍。关键就在反馈这一句。"你的研究笔记缺统计数据——至少找两个带来源的数据点再改一版"，这样得到的第二版，会比原样重跑好得多。

每个任务最多重试两三次。要是一个智能体在同一个任务上栽了三回，就交给人，或者记下来留着复查。

### 模式 5：什么都记下来

在生产环境里，每次智能体调用都该记下来：它收到的输入、它产出的结果、它调了哪些工具、花了多长时间。靠这些，调试才有可能。等流水线哪天输出了个烂结果，日志会告诉你是哪个智能体出的错——以及那个智能体当时到底收到了什么。

## 第 6 部分：来自真实世界的团队示例

### 团队 1：线索生成与外联

智能体：

- 勘探智能体——在 LinkedIn 和公司官网上，找符合你目标客户画像（ICP）的线索。
- 研究智能体——为每条线索找具体的近期新闻、帖子或背景。
- 个性化智能体——用这些研究，给每条外联消息写一个量身定制的开头句。
- 序列智能体——为每条线索排出完整的三次触达序列。

输出：一份能直接录入 CRM 的线索清单，每条都配好了个性化的多次触达序列，随时能发。

### 团队 2：竞争情报监控

智能体：

- 监控智能体（定时跑）——盯着竞争对手的网站、产品页、定价和社交账号有没有动静。
- 变化检测智能体——拿当前状态和上周的快照对比，标出哪里变了。
- 分析智能体——解读每个变化意味着什么，可能带来哪些影响。
- 报告智能体——汇总成一份每周简报，发到 Slack 或邮件。

输出：一份自动生成的每周竞争情报简报，不用再手动去查。

### 团队 3：客户支持分流系统

智能体：

- 分类智能体——读每一条进来的支持消息，按类型（账单、技术、一般、紧急）和情绪分好类。
- 知识智能体——在公司知识库里搜最对得上的答案。
- 草稿智能体——参考知识库的答案和原消息的语气，写一份回复。
- 路由智能体——按分类把草稿发到对应的人工队列；要是置信度够高，就直接自动发出去。

输出：每条支持消息都被自动分类、回复、分发。人只需要看那些被标记的或者复杂的案例。

### 团队 4：通讯研究与写作流水线

智能体：

- 选题侦察智能体——在某个细分领域里，挑出过去 7 天最热的 5 个进展。
- 深度研究智能体——给每个主题找来源、统计数据和专家观点。
- 段落撰写智能体——为每个主题写一段 150 字的通讯内容。
- 编辑智能体——把所有段落过一遍，看一致性、语气和质量。
- 组装智能体——把各段拼成一份带开头和结尾的完整通讯草稿。

输出：一份完整的每周通讯草稿，研究都备好了，随时可以审和发。

## 第 7 部分：会害死智能体团队的几个错误

### 错误 1：搭一个巨型智能体，而不是一个团队

要是你的系统提示词超过 500 个词，还一口气交给智能体六件不同的活，那你搭的不是团队，是一个晕头转向、假装成团队的智能体。把它拆开。每件不同的任务，都给它自己的智能体。

### 错误 2：没定好输出格式

没有结构化的输出格式，每个智能体交出来的东西都会有点不一样。下一个智能体根本没法稳定地解析。给每个系统提示词都加一个明确的输出模板，并且严格执行。

### 错误 3：跳过批评者

大多数人搭的是"研究 → 写作 → 发布"，把审阅那一步整个跳过了。

一份作品是好到能发布，还是发出去会让你下不来台，差别常常就在这个批评者智能体身上。把它放进每一条流水线。

### 错误 4：给智能体它扛不住的记忆

智能体的上下文窗口是有限的。

要是一个智能体非要在一个窗口里同时塞下整个研究数据库、对话历史、它的指令和当前任务，它的表现就会变差。用结构化的交接——只把下一个智能体需要的东西传过去，而不是把上一个智能体产出的一切全倒过去。

### 错误 5：上生产之前没有人盯着

每个新的智能体团队，先在监控模式下跑——在它做任何对外动作（发邮件、发社交、调 API）之前，都由人先审一遍输出。等到流水线连续产出 20 多次、每一次你都乐意亲手发出去，再切到全自动。

## 快速开始：48 小时内搭起你的第一个智能体团队

- **第 1 小时：** 在你的业务里挑一个三步以上的工作流，其中每一步都能交给不同的人去做。
- **第 2 小时：** 给每一步写一个系统提示词，就当你在给新来的人交接：这是你唯一的活，这是你会收到的东西，这是你必须交出来的内容。
- **第 3 小时：** 在 Make 或 n8n 里把流水线搭起来，把智能体顺序连上。
- **第 4 到 6 小时：** 跑五个测试用例。找出流水线在哪儿卡住，把最弱的那条提示词收紧。
- **第 2 天：** 在最重要的那一步后面加一个批评者智能体。再跑五个测试，比比输出质量。
- **第 2 天晚上：** 拿一个真实任务试试。看看输出，再迭代。

一个智能体，跑的是一个任务。一个智能体团队，跑的是一门生意。

道理其实很简单：一个智能体只干一件事、交接要结构化、步骤之间设质量关卡，再加一个让整个系统不出岔子的批评者。

把这四件事放进任何一条工作流，你就有了一个真正能干活的团队。
