# 如何构建一个真正能协同工作的 AI 智能体团队（完整课程）

**作者：** Kanika ([@KanikaBK](https://x.com/KanikaBK))  
**日期：** 2026年5月25日  
**来源：** [How to build a team of AI Agents that actually work together (Full Course)](https://x.com/KanikaBK/status/2058817146411692358)

大多数人构建一个 AI 智能体，看着它在复杂任务上失败，然后得出结论：AI 智能体还没准备好。真正的问题在于架构。这门完整课程展示了构建多智能体系统的确切心智模型、团队结构、工具和生产模式，这些系统能产出可靠、高质量的输出。

给单个智能体一个复杂任务，就像雇一个人同时去做研究、写作、设计、编码和发布，还要记住每一步的每个细节。

它在复杂性面前会崩溃。解决方案是人类团队几个世纪前就想明白的：专业分工、清晰的角色，以及一个负责协调的管理者。

这是关于构建一个真正能协同工作的 AI 智能体团队的完整课程——从心智模型到工具再到可用于生产的模式。

我尝试把我构建 AI 智能体经验中能想到的每一个要点都包含进来。希望你准备好了！

## 核心的思维转变

在你写下一条提示词之前，你需要改变你思考智能体的方式。

### 用任务来思考，而不是角色

构建多智能体系统时最常见的错误，是复制人类的组织架构图。你创建一个"研究智能体"、一个"写作智能体"和一个"营销智能体"——然后纳闷为什么输出不一致且难以调试。

那个改变一切的转变：用任务来思考，而不是角色。

AI 智能体在拥有一个明确目标、一组有限的特定工具，以及针对单个离散任务的精确指令时表现最佳。一个职责宽泛的智能体会做出模糊的决策。一个任务狭窄的智能体会产出一致、可靠的输出。

不要构建一个"内容智能体"，而要构建：

- 一个研究任务智能体——接收一个主题，返回结构化的研究笔记。
- 一个简报撰写智能体——接收研究笔记，返回一份内容简报。
- 一个草稿撰写智能体——接收一份简报，返回一份完整草稿。
- 一个编辑智能体——接收一份草稿，返回一份带批注的编辑版本。
- 一个发布智能体——接收最终文稿，进行格式化并发布。

每个智能体都简单、可测试、可替换。整个系统作为一个整体是强大的。

### 为什么多智能体系统胜过单个智能体

MIT 和 Google Brain 的研究发现，当智能体相互辩论和批评彼此的输出时，推理质量和事实准确性都会显著提升——即使一个智能体一开始给出了错误答案，来自其他智能体的批评也会纠正其轨迹。

多智能体系统不仅仅关乎并行。它们关乎通过专业分工和验证带来的质量。

## 第 1 部分：四个核心智能体角色

每个有效的多智能体团队都有处于四个功能类别的智能体。你不需要每个类别一个智能体，但每个生产团队都需要覆盖全部四个功能。

### 角色 1：编排者（管理者智能体）

编排者接收顶层任务，将其拆解为子任务，把每个子任务分配给合适的专家智能体，收集输出，并综合出最终结果。它从不做实际工作，它只做协调。

它需要：

- 对它可用的每个专家智能体以及各自做什么的清晰描述。
- 何时委派、何时综合的规则。
- 一个质量关卡，即判断一个子任务输出何时足够好可以传递下去的标准。

编排者的系统提示词示例：

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

研究者唯一的工作是查找、检索和组织信息。它不写作、不分析、不创作，它只收集。

它需要：

- 网络搜索工具（Perplexity API、Serper、Brave Search API）
- 一个用于读取完整页面的 URL 抓取器
- 一种结构化的输出格式，使其结果总是便于下游智能体使用

要强制执行的输出格式示例：

```
Topic: [topic]
Key Facts: [bulleted list]
Statistics: [with sources]
Competing Perspectives: [brief list]
Sources: [URLs]
```

### 角色 3：专家生产者

这些是干活的工人，每个生产任务一个智能体。常见的专家智能体包括：

- 写作智能体：接收一份简报并写出一份草稿。
- 编码智能体：接收需求并编写代码。
- 数据分析智能体：接收原始数据并返回洞察。
- 设计简报智能体：接收一个概念并返回一份视觉设计简报。
- 外联智能体：接收线索数据并撰写个性化消息。

每个专家智能体都应该有：

- 一个范围严格收窄的系统提示词（只干一件事）。
- 完成那件工作所需的最少工具。
- 一个明确的输出格式，下游智能体能可靠地解析。

### 角色 4：批评者 / 审阅者

这是大多数智能体系统中最少被构建的角色——也是对质量最重要的角色。批评者接收任何智能体的输出，根据既定标准评估它，并返回具体、可执行的反馈。

一个设计良好的批评者不会说"这很糟糕"。它会说：

- "引言把主要论点埋在了第三段。把它移到第一句。"
- "第二段的论点没有依据。加一个来源或删掉它。"
- "语气不一致——第 1–3 段是正式的，第 4–6 段是随意的。统一起来。"

批评者智能体正是把一个产出平庸输出的多智能体系统，和一个产出你引以为豪的作品的系统区分开来的东西。

## 第 2 部分：三种架构

多智能体团队遵循三种结构之一。理解该用哪一种，决定了你如何构建的一切。

### 架构 1：顺序式（流水线）

智能体一个接一个地运行。智能体 A 的输出成为智能体 B 的输入。

```
输入 → 研究智能体 → 简报智能体 → 写作智能体 → 编辑智能体 → 输出
```

何时使用：任务有清晰的线性流程。每一步都依赖于上一步正确完成。

最适合：内容创作、研究报告、提案生成、数据处理流水线。

风险：如果智能体 2 产出糟糕的输出，后续每个智能体都会继承那个错误。在每一步之间加一个质量关卡。

### 架构 2：并行式（扇出）

一个编排者把一个任务拆分，同时发给多个智能体。所有智能体同时工作。编排者收集并综合结果。

```
                       ┌→ 研究智能体 A → ┐
输入 → 编排者          ├→ 研究智能体 B → ├→ 综合智能体 → 输出
                       └→ 研究智能体 C → ┘
```

何时使用：任务可以被分成独立的并行工作流。能大幅减少总运行时间。

最适合：多来源研究、跨多家公司的竞争分析、处理大批量项目。

风险：综合很难。编排者需要明确的规则，来处理可能相互冲突的并行输出如何组合。

### 架构 3：分层式（多层）

多层编排。一个顶层编排者管理多个中层编排者，每个中层编排者又管理专家智能体。

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

何时使用：任务复杂到需要协调多条流水线，而不只是多个智能体。

最适合：端到端的业务流程自动化、复杂的研究与发布工作流、完整的营销活动自动化。

风险：复杂性会迅速叠加。每一层都会增加延迟、成本和潜在的故障点。只有当顺序式和并行式确实无法解决你的问题时，才采用分层式。

## 第 3 部分：工具栈

### 无代码 / 低代码（从这里开始）

**Make（前身为 Integromat）**

构建多智能体工作流最好的可视化构建器。通过 API 连接 Claude、OpenAI 或任何 LLM。可视化地构建顺序流水线。无需代码即可添加条件分支、错误处理器和并行路由。

**n8n**

Make 的开源替代品。可自托管，更灵活，更适合有自定义逻辑的复杂工作流。有原生的 AI 智能体节点，支持工具调用。

**Relevance AI**

专门为多智能体系统构建。让你创建有工具访问权限的智能体，把它们连接成团队，并可视化地定义智能体之间的交接规则。在业务工作流自动化方面很强。

### 基于代码的框架（追求完全掌控）

**Claude API 配合工具使用**

直接用 Anthropic Claude API 构建智能体。每个智能体是一个系统提示词 + 一组工具（它可以调用的函数）。编排者用一个任务调用 Claude，Claude 调用工具，工具返回结果，Claude 进行综合。

**LangGraph**

一个基于图的框架，用于构建多智能体工作流，其中节点是智能体，边定义交接。非常适合复杂的条件流程，即下一个智能体取决于当前的输出。

**Agno（前身为 Phidata）**

一个专门为构建带分层编排的智能体团队而设计的框架。内置对团队记忆、智能体间通信和并行执行的支持。

**AutoGen（微软）**

一个多智能体对话框架，其中智能体直接相互发消息。非常适合需要在对话循环中辩论、批评和修改的智能体。

## 第 4 部分：一步步构建你的第一个智能体团队

我们将构建一个内容研究与写作团队——一个三智能体系统，接收一个主题并产出一份打磨过的、有研究支撑的文章草稿。这是最实用的起点，而且这个架构可以迁移到几十种其他用例。

![](images/img-03.jpg)

### 第 1 步：构建研究智能体

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

### 第 2 步：构建写作智能体

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

要给它的工具：无。它只需要研究笔记作为输入。

### 第 3 步：构建编辑智能体

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

### 第 4 步：构建编排者

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

### 第 5 步：连接并测试

在 Make 或 n8n 中：

- 创建一个触发器（webhook 或手动表单）。
- 把它连接到研究智能体（带研究系统提示词 + 网络搜索工具的 Claude API 调用）。
- 把输出传给写作智能体（带写作系统提示词的 Claude API 调用）。
- 把草稿传给编辑智能体（带编辑系统提示词的 Claude API 调用）。
- 把最终输出返回到 Slack、Notion 或邮件。

用五个不同的主题测试。注意流水线在哪里出问题，并收紧那一步的提示词。

## 第 5 部分：让智能体团队可靠的五个模式

### 模式 1：强制结构化输出

你团队中的每个智能体都应该以一种确定的格式返回输出——而不是自由形式的散文。这让交接变得可靠。如果研究智能体可以用任何它想要的格式返回笔记，写作智能体就必须去解释它们。那种解释会引入不一致。

在每个系统提示词中使用明确的输出模板。团队中的每个智能体都应该确切知道它接收什么格式，以及它必须返回什么格式。

### 模式 2：智能体之间的质量关卡

不要自动把每个输出传给下一个智能体。加一个简单的评估步骤——要么是编排者审阅，要么是一个专门的批评者智能体——在输出向下游移动之前检查它。

一个质量关卡会问：这个输出是否达到了下一步成功所需的最低标准？如果没有，它就带着具体反馈被退回。这就是防止单个薄弱智能体拖垮整条流水线的东西。

### 模式 3：给智能体最少的工具

一个可用 15 个工具的智能体会不一致地使用它们。一个有 2–3 个工具的智能体会可靠地使用它们。把工具匹配到智能体确切要做的工作上。研究智能体得到搜索和抓取。写作智能体什么都不得到——它不需要外部信息，只需要它的上下文。

发布智能体得到平台 API。

### 模式 4：内建一个重试循环

每个生产级智能体团队都需要一个重试机制。当一个智能体的输出没通过质量关卡时，它应该带着具体反馈获得第二次机会——而不只是再跑一遍。反馈才是重要的部分。"你的研究笔记缺少统计数据——找至少两个带来源的数据点并修订"会产出比再跑一遍相同提示词更好的第二次尝试。

把每个任务的重试限制在 2–3 次。如果一个智能体在同一个任务上失败三次，就上报给人类或记录下来以供审查。

### 模式 5：记录一切

在生产中，每次智能体调用都应该记录：它接收的输入、它产出的输出、它调用的工具，以及它花的时间。这就是让调试成为可能的东西。当流水线产出一个糟糕的输出时，日志会告诉你哪个智能体引入了错误——以及那个智能体确切接收到了什么作为输入。

## 第 6 部分：真实世界的团队示例

### 团队 1：线索生成与外联

智能体：

- 勘探智能体——在 LinkedIn 和公司网站上搜索匹配你 ICP 的目标线索。
- 研究智能体——查找关于每条线索的具体近期新闻、帖子或背景。
- 个性化智能体——用研究为每条外联消息撰写一个个性化的首句。
- 序列智能体——为每条线索构建完整的三次触达外联序列。

输出：一份可直接录入 CRM 的线索列表，配有个性化的多次触达外联序列，随时可发送。

### 团队 2：竞争情报监控器

智能体：

- 监控智能体（按计划运行）——检查竞争对手的网站、产品页、定价和社交渠道的变化。
- 变化检测智能体——把当前状态与上周的快照比较，标记出有什么变化。
- 分析智能体——解读每个变化的意义，并提出影响。
- 报告智能体——汇编一份每周简报，并发送到 Slack 或邮件。

输出：一份自动化的每周竞争情报简报，无需手动研究。

### 团队 3：客户支持分流系统

智能体：

- 分类智能体——读取每条进来的支持消息，按类型（账单、技术、一般、紧急）和情绪分类。
- 知识智能体——在公司的知识库中搜索最相关的答案。
- 草稿智能体——用知识库答案和原始消息的语气写一份回复。
- 路由智能体——根据分类把草稿发到正确的人工队列，或在置信度高时自动发送。

输出：每条支持消息都被自动分类、回答和路由。人类只审查被标记的或复杂的案例。

### 团队 4：通讯研究与写作流水线

智能体：

- 选题侦察智能体——找出某个细分领域过去 7 天里最热门的 5 个进展。
- 深度研究智能体——为每个主题查找来源、统计数据和专家观点。
- 段落撰写智能体——为每个主题写一段 150 字的通讯段落。
- 编辑智能体——审阅所有段落的一致性、语气和质量。
- 组装智能体——把各段落组合成一份带开头和结尾的完整通讯草稿。

输出：一份完整的每周通讯草稿，含研究，随时可审阅和发送。

## 第 7 部分：扼杀智能体团队的错误

### 错误 1：构建一个巨型智能体而不是一个团队

如果你的系统提示词超过 500 个词，并给智能体六个不同的工作去做，你就构建了一个假装成团队的困惑智能体。把它拆开。每个不同的任务都得到它自己的智能体。

### 错误 2：没有确定的输出格式

没有结构化的输出格式，每个智能体都会返回略有不同的东西。下一个智能体无法可靠地解析它。给每个系统提示词加一个明确的输出模板并强制执行。

### 错误 3：跳过批评者

大多数人构建"研究 → 写作 → 发布"，并完全跳过审阅步骤。

批评者智能体正是把好到可以发布的作品，和让你尴尬的作品区分开来的东西。把它构建进每条流水线。

### 错误 4：给智能体它们无法处理的记忆

智能体的上下文窗口是有限的。

一个试图在一个上下文窗口里同时容纳完整研究数据库、对话历史、它的指令和它当前任务的智能体会退化。使用结构化的交接——只传递下一个智能体需要的东西，而不是上一个智能体产出的一切。

### 错误 5：投入生产前没有人类监督

先在监控模式下运行每个新的智能体团队——其中由一个人在它采取任何外部行动（发邮件、发社交、调 API）之前审查每个输出。只有在流水线产出了 20 次以上你乐意手动发送的连续输出之后，才转为自动化。

## 快速开始：48 小时内搭起你的第一个智能体团队

- **第 1 小时：** 在你的业务中挑一个需要三步或更多的工作流，其中每一步都可以由不同的人来做。
- **第 2 小时：** 为每一步写一个系统提示词，就像你在给一个新员工做交接：这是你唯一的工作，这是你接收的东西，这是你必须返回的确切内容。
- **第 3 小时：** 在 Make 或 n8n 中构建流水线。把智能体顺序连接起来。
- **第 4–6 小时：** 跑五个测试用例。找出流水线在哪里出问题。收紧最薄弱的提示词。
- **第 2 天：** 在最重要的那一步之后加一个批评者智能体。再跑五个测试。比较输出质量。
- **第 2 天晚上：** 把它放到一个真实任务面前。审查输出。迭代。

一个智能体跑一个任务。一个智能体团队跑一门生意。

原则很简单：每个智能体只干一件事、结构化的交接、步骤之间的质量关卡，以及一个让整个系统保持诚实的批评者。

把这四件事构建进任何工作流，你就拥有了一个真正有效的团队。
