# 如何在2026年成为AI工程师（构建者路线图）

**作者：** Avid ([@Av1dlive](https://x.com/Av1dlive))  
**日期：** 2026年5月7日  
**来源：** [How to Become an AI Engineer in 2026 (Builder's Roadmap)](https://x.com/Zephyr_hg/status/2052063154423898603)

你可以在一个周末内使用AI构建下一个10亿美元的公司

而你唯一需要学习的技能是**智能体AI与线束工程**

> TLDR；如果你不想阅读7,862字的路线图，那么你可以简单地将这个链接给你的智能体来个性化路线图 ➡️ https://raw.githubusercontent.com/codejunkie99/agent-roadmap-2026/main/AGENT.md

问题在于大多数工程师对于应该学什么没有清晰的想法

有些人选择CrewAI，因为基于角色的演示在Twitter上看起来很光滑。有些人追逐每一个发布的新框架，永远无法完成任何真实的东西。其他人直接跳入多智能体系统，而不理解上下文、工具、线束或评估。

结果通常是相同的：大量的框架旅游，很少有生产就绪的技能。

如果你的目标是在2026年成为一名智能体工程师，你不需要学习12个框架。你需要学习如何构建、装配、评估和发布真正的生产智能体系统。

这意味着学习如何：

- 在真正的编排运行时（如LangGraph）上构建智能体
- 使用Claude Agent SDK作为参考线束
- 用Write、Select、Compress、Isolate正确地进行上下文工程
- 编写模型能正确选择的工具
- 为生产流量添加内存、持久性和沙箱
- 构建评估、轨迹检查和CI回归门控
- 发布能在真实用户和真实成本下存活的智能体

本指南是一个建立在2025年末和2026年初发布内容基础上的6阶段路线图。这篇文章超过7,000字，仅从主要来源引用。但其真正的价值在于每个阶段都有一个具体项目、一个规范阅读列表和你需要的确切资源。

这样，在大约**17周**的专注工作内，你就能达到可以端到端拥有一个生产AI功能的智能体工程师水平。

研究这些内容花了超过**60小时**阅读主要工程博客、论文和发布工程师调查。

现在让我们开始阅读路线图 ⬇️

---

## 2026年智能体工程师的工作内容

很多人听到"AI智能体工程师"，想象的是有人把CrewAI角色拼凑在一起就叫做完成了。

实际上，大多数现代智能体工程师做的事情要实际得多。他们在前沿模型之上构建、装配和运营智能体系统。

这通常包括：

- 设计智能体循环和工具调度
- 用Write、Select、Compress、Isolate进行上下文工程
- 编写模型能正确选择的工具
- 用隔离的上下文窗口编排子智能体
- 添加技能、内存、持久性和沙箱
- 连接评估、追踪和CI门控，使"更好"变得可测量

同样的模型，不同的线束，完全不同的结果。**Anthropic自己的测量结果：Opus 4.5在Claude Code内部的CORE评分为78%，在Smolagents内部为42%。同一个模型。句号。**

这个差距就是线束工程，这也是这份路线图的主题。

每个智能体构建者需要知道的四个上下文原语：**Write**（草稿本、内存文件）、**Select**（在使用时检索）、**Compress**（在上下文窗口85-95%时进行总结）、**Isolate**（拥有自己上下文窗口的子智能体）。

Anthropic的多智能体研究系统在广度优先研究中使用完全相同的模式击败了单智能体Opus 4，提升了**90.2%**，同时消耗了约15倍的令牌。

实际上，2026年只有两个值得深入学习的技术栈：**LangGraph 1.0 + Deep Agents**，以及**Claude Agent SDK**。其余的要么正在淡出，要么被吸收，要么是生产环境中这两者的更差版本。

---

## 整个路线图中的免费资源

这些是免费提供信号的博客、课程、频道和通讯。在第0阶段订阅它们，这样路线图的其余部分就会有源源不断的新帖子、案例研究和主要来源更新。

这些都没有付费墙，而且大多数更新速度比任何教科书都快。

### 可以订阅的工程博客

- **Anthropic工程博客**（免费，官方）——如果你只读一个博客，就读这个。上下文工程、线束设计、多智能体研究、高级工具使用、评估。所有主要来源，在整个路线图中都反复引用
- **LangChain博客**（免费）——线束、中间件和Deep Agents规范在这里公开形式化。读Lance Martin、Vivek Trivedy和Harrison Chase的所有文章
- **OpenAI Cookbook**（免费，GitHub）——每个API功能的工作笔记本。工具使用、结构化输出、评估、智能体。跟着打代码
- **Hamel Husain的博客**（免费）——"你的AI产品需要评估"是每个人都链接的评估文章。网站上的其他所有内容都在同一水平。如果你构建评估，读它两遍
- **Eugene Yan的博客**（免费）——"构建基于LLM的系统和产品的模式"是每个人都引用的从业者写作。有主见，并根据真实的发布经验进行了校准
- **Lilian Weng的博客**（免费）——关于智能体、提示工程、幻觉、对齐的长篇深度文章。该领域最清晰的综合写作
- **Simon Willison的博客**（免费）——一位发布工程师的每日笔记。适合对炒作进行理性检验，并首先发现奇怪的边缘情况
- **Chip Huyen的博客**（免费）——从第一原理出发的ML系统。她的"为生产环境构建LLM应用"一文是第5阶段之前的必读
- **Phil Schmid的博客**（免费）——关于HuggingFace、Gemini、微调、部署的实用端到端指南。总是展示代码
- **Cameron Wolfe的Deep (Learning) Focus**（免费）——长篇论文分解。在一次阅读中了解一个研究领域

### 值得完成的免费课程

- **DeepLearning.AI短期课程**（免费）——1-2小时的短期课程，几乎都是免费的。LangGraph课程（与LangChain合作构建）和Andrew Ng的"Agentic AI"课程（反思、工具使用、规划、多智能体设计模式）是在第0阶段要完成的两门课
- **LangChain学院：LangGraph介绍**（免费）——官方免费课程。状态、内存、人在回路、多智能体。在第2阶段完成这个
- **Anthropic交互式提示工程教程**（免费，GitHub）——作为Jupyter笔记本的九章内容，对应Claude API。建立提示肌肉的最快方式
- **HuggingFace智能体课程**（免费）——智能体、smolagents、MCP和评估的端到端覆盖。免费证书
- **HuggingFace LLM课程**（免费）——基础：令牌化、变换器、微调。即使你只在API上构建，也有用的背景
- **FreeAcademy上的MCP基础**（免费）——构建MCP服务器，将它们连接到Claude，编写自定义工具。实现MCP素养的最快路径

### YouTube频道和演讲

- **Andrej Karpathy**（免费）——神经网络：从零到英雄，用原始Python从头构建GPT。他在Sequoia AI Ascent的2026年"Vibe Coding to Agentic Engineering"演讲是关于为什么线束工程现在重要的最清晰阐述
- **AI Engineer**（免费）——所有AI Engineer Summit和World's Fair演讲。搜索Hamel Husain、swyx、Anthropic工程师和Erik Schluntz的演讲
- **LangChain**（免费）——关于LangGraph、Deep Agents、中间件和集成的每周教程。通常是新功能以视频形式最先落地的地方
- **Anthropic**（免费）——Anthropic工程师的演讲。多智能体研究演练、Claude Code内部原理、技能
- **Yannic Kilcher**（免费）——论文分解。省去你自己阅读每篇arXiv预印本
- **Lex Fridman播客**（免费）——与构建和研究AI的人的长篇访谈。Karpathy、Schulman、Sutskever、Amodei

### 值得订阅的通讯

- **Latent Space by swyx and Alessio**（免费）——AI工程师的技术通讯。AINews每日摘要、播客和年度"AI工程阅读清单"。如果你只订阅一个，就是这个
- **The Batch by Andrew Ng**（免费）——每周广谱覆盖。适合注意到新事物何时出现
- **Import AI by Jack Clark，Anthropic联合创始人**（免费）——政策加研究摘要。最接近该领域战略背景简报的东西
- **Ben's Bites**（免费）——五分钟内的每日AI新闻。只浏览。适合捕捉否则会错过的公告
- **TLDR AI**（免费）——每日摘要，低噪音。与上面一个更深的通讯配合
- **AI Engineer Pack by swyx**（免费）——为AI工程师策划的免费积分、工具和资源。持续更新

### 值得研究的开源代码库

- **Anthropic Cookbook**（免费，GitHub）——每个工作流模式的参考实现。已在第0阶段列表中。在每个阶段后重新阅读
- **OpenAI Cookbook**（免费，GitHub）——同样的想法，OpenAI这边。工具使用、结构化输出、评估、智能体
- **LangChain的deepagents**（免费，GitHub）——LangGraph之上的参考开源线束。在第3阶段构建自己的线束时阅读中间件文件
- **LangGraph示例**（免费，GitHub）——可运行的LangGraph模式。监督者、层次团队、规划、客户支持智能体
- **inspect_evals**（免费，GitHub）——200+标准评估作为Python包。GAIA、SWE-bench、Cybench、BFCL
- **awesome-agentic-engineering-resources**（免费，GitHub）——智能体工程资源的社区策划索引。用于填补本路线图未涵盖的空白

### 通勤播客

- **Latent Space**（免费）——与推动该领域发展的人的长篇访谈。Anthropic、OpenAI、LangChain、Modal、E2B都在嘉宾名单上
- **Dwarkesh Podcast**（免费）——关于AI战略、能力和政策的长篇访谈
- **Sam Charrington的TWIML AI播客**（免费）——与研究人员和工程师的每周技术访谈
- **Practical AI**（免费）——以工程为重点。少炒作，多实发
- **Matt Turck的MAD播客**（免费）——数据和AI生态系统的创始人加投资者视角。适合追踪谁在发布而不是融资

### 值得加入的社区

- **LangChain Discord**（免费）——你会在这里找到LangGraph和Deep Agents核心团队。活跃的#help频道
- **HuggingFace Discord**（免费）——最大的开放权重和ML社区
- **r/LocalLLaMA**（免费）——开放权重模型新闻、基准测试和工具。通常比官方渠道更快
- **AI Engineer World's Fair**（免费注册）——该领域的专业网络。职位发布、招聘渠道、工作组
- **Anthropic Discord**（免费）——Claude开发者社区。技能分享、钩子模式、MCP服务器

关注重点：在第0阶段选择一个博客、一个通讯、一个播客和一个社区。不要试图同时关注所有40+资源。只有当现有的不再给你惊喜时才添加更多。这份列表的目的是广度，让你可以选择，而不是要完成的清单。

---

## 第0阶段：基础（1-2周）

**本阶段目标：** 建立正确的思维模型。除了一次性脚本，暂时不要写一行智能体代码。

大多数初学者跳过这个阶段，直接进入框架教程，最终写出他们失败时无法推理的代码。不要跳过它。

### 1. 增强型LLM以及工作流与智能体的区别

在接触框架之前，你需要理解Anthropic识别出的五种工作流模式（提示链、路由、并行化、编排者-工作者、评估者-优化者），以及为什么工作流与智能体不同：

- 工作流有你编写的固定控制流
- 智能体在循环内自己做控制流决策

这个区别将帮助你避免构建本应是链的智能体。

**资源：**

- *Building Effective Agents* by Anthropic（Erik Schluntz和Barry Zhang）（2024年12月）（免费，官方）——五种工作流模式加上增强型LLM概念。该领域每个人都引用这个。首先读它
- *Anthropic Cookbook*（patterns/agents文件夹）（免费，GitHub）——每个工作流模式的参考实现，作为可运行的笔记本。跟着打，不要只是读
- *Simon Willison对Building Effective Agents的注释*（免费）——同一篇论文的资深工程师理性检验视角

关注重点：工作流和智能体之间的区别、增强型LLM思维模型、编排者-工作者模式、为什么并行化通常优于顺序推理，以及Anthropic明确警告的失败模式。

### 2. 作为一门学科的上下文工程

2026年提示工程作为独立技能已经死亡。替代品是上下文工程：决定在循环的每一步模型面前有什么令牌。

**资源：**

- *Effective context engineering for AI agents* by Anthropic（2025年9月29日）（免费，官方）——这个读两遍。记住框架
- *Context Engineering for Agents* by Lance Martin（LangChain）（免费）——Write、Select、Compress、Isolate框架。你需要的一个思维模型
- *How we built our multi-agent research system* by Anthropic（2025年6月）（免费，官方）——编排者-工作者参考架构、90.2%广度优先研究改进，以及15倍令牌的注意事项
- *Simon Willison对多智能体研究帖子的注释*（免费）——对架构和成本权衡的理性检验视角

关注重点：Write、Select、Compress和Isolate各自在代码中意味着什么，为什么子智能体是隔离原语（不是并行原语），以及何时使用压缩vs卸载vs摘要。

### 3. 作为操作系统的线束

**资源：**

- *The Complete Guide to Harness Engineering*（ClaudeCodeLab）（免费）——带有可运行代码的三级线束升级
- *Inside the Claude Agents SDK*（ML6）（免费）——CPU/RAM/OS/App类比以及激励整个路线图的78% vs 42% Opus 4.5数字
- *Building agents with the Claude Agent SDK*（Anthropic）（免费，官方）——SDK为什么存在，为什么从Claude Code SDK改名
- *Effective harnesses for long-running agents* by Anthropic（2025年11月26日）（免费，官方）——Anthropic自己的线束入门。与Vivek Trivedy的帖子一起读，从不同团队的角度验证同样的想法
- *Harness design for long-running application development* by Anthropic（2026年3月24日）（免费，官方）——后续。当会话延伸到数小时和数天时会发生什么变化。第3阶段必读
- *How to think about agent frameworks* by Harrison Chase（LangChain）（免费）——编排框架与抽象的区别。在你选择任何东西之前必读

关注重点：循环、工具调度、上下文策划、持久性、钩子、子智能体编排、可观测性——以及这些在你将遇到的任何线束中是如何实现的。

### 4. 2026年的领域现状

**资源：**

- *State of Agent Engineering*（LangChain）（免费）——1,340名受访者，2025年11-12月。把这些数字记在脑子里：57%的团队处于生产中，89%有可观测性，52%有评估，质量（32%）是#1障碍
- *How to Build an Agent*（LangChain）（免费）——"聪明实习生"框架，用于确定智能体应该和不应该拥有什么
- *Continual learning for AI agents* by Harrison Chase（LangChain）（免费）——智能体实际学习的三层：权重、提示、内存。在你接触任何微调之前需要的框架

关注重点：团队在生产中挣扎的地方（质量、成本、可靠性）、中位数技术栈的样子，以及边际小时的努力回报在哪里。

**实践项目：** 手写一份2页的个人文档，用你自己的话定义：工作流 vs 智能体、增强型LLM、四个上下文工程原语、编排者-工作者模式、线束/模型/框架之间的区别，以及你预计在自己代码中看到的前三个失败模式。这份文档就是实际的交付物。如果你不看就写不出来，说明你没有仔细阅读。

### 第0阶段里程碑

在本阶段结束时，你应该能够：

- 不使用框架术语解释什么是智能体以及它与工作流的区别
- 命名四个上下文工程原语并给出每个的代码级别示例
- 解释为什么2026年线束的贡献大于模型
- 描述编排者-工作者模式和15倍令牌成本权衡
- 在架构基础而非感觉上选择框架

---

## 第1阶段：构建你的第一个简单智能体（2-3周）

**本阶段目标：** 写一个使用工具的智能体两次。一次使用Anthropic的原始SDK，一次使用Claude Agent SDK线束。感受自己滚动循环与站在真正线束上的区别。

这是理解线束给你带来什么的最便宜方式。

### 1. 从头开始的智能体循环

循环不是魔法。你用消息和工具调用模型，解析出`tool_use`块，执行工具，追加`tool_result`，循环直到`stop_reason`等于`end_turn`。

一旦你自己用~100行写了这个，每个框架都变得可读了。

**资源：**

- *Tutorial: Build a tool-using agent*（Anthropic文档）（免费，官方）——`tool_use`、`tool_result`、并行工具调用和响应循环的参考
- *Writing tools for agents*（Anthropic）（免费，官方）——在你设计任何工具之前读这个。你的工具及其参数的描述是LLM的用户手册
- *Equipping agents for the real world with Agent Skills*（Anthropic）（免费，官方）——由编写规范的团队解释的渐进式披露模式

关注重点：请求/响应循环如何终止，`stop_reason`值意味着什么，如何编码并行工具调用，工具抛出时的错误恢复，以及如何设计工具描述让模型正确选择它。

**实践：** 使用带有工具规范的`anthropic.messages.create`在100行内构建一个"从头开始"的智能体。三个工具：通过Tavily或Firecrawl的`web_search`、`read_file`、`write_file`。没有框架。在研究任务上运行它，读取追踪的每一步。

### 2. Claude Agent SDK作为规范线束

Claude Agent SDK是为Claude Code提供动力的同一个线束。你将把它作为参考来研究，并作为你第一天的工具使用。

**资源：**

- *Claude Agent SDK文档*（免费，官方）——Python和TypeScript SDK、钩子、子智能体、技能和Task工具
- *Claude Agent SDK，技能参考*（免费，官方）——SKILL.md文件如何工作，元数据前置信息，渐进加载
- *claude-code-best-practices* by Muhammad Usman GM（免费，GitHub）——浏览，不要完全复制。适合看看真实用户做什么
- *claude-code-best-practice* by Shan Raisshan（免费，GitHub）——有不同策划视角的配套汇编
- *Evaluating Skills*（LangChain）（免费）——LangChain如何测量技能是否真正发挥作用。在本阶段写了你的第一个技能后，想知道它是否有帮助或有害时有用

关注重点：CLAUDE.md系统提示模式，技能如何渐进式加载，PreToolUse和PostToolUse钩子，通过Task工具生成子智能体，以及SDK如何处理权限提示。

**实践：** 使用`claude-agent-sdk`重建上一个主题中的同一个智能体。添加带有项目约定的CLAUDE.md。添加一个定义"研究摘要"输出格式的技能（带有SKILL.md的文件夹）。添加一个自动格式化智能体写入的任何文件的PostToolUse钩子。使用Task工具为子任务生成一个子智能体。

### 3. 发布一些小东西

教程不算。你需要一个按计划运行并阅读其输出的东西。

**实践项目：** 一个每日简报智能体，读取你本地的Markdown笔记和几个RSS源，生成带引用的摘要简报，并将其写入磁盘。通过launchd或systemd定时运行。运行一周。看它失败。修复它。

### 第1阶段里程碑

在本阶段结束时，你应该能够：

- 在没有框架的情况下在不到100行内写一个使用工具的智能体循环
- 解释`stop_reason`值意味着什么以及并行工具调用如何工作
- 在Claude Agent SDK上构建同样的智能体，带有技能、钩子和子智能体
- 用200字阐明线束在你自己从头编写的版本中免费给了你什么

---

## 第2阶段：用正确的架构构建真正的智能体（3-4周）

**本阶段目标：** 在LangGraph 1.0 + LangChain `create_agent` + Deep Agents上构建一个多步、持久、有状态的智能体。

这是你可能在生产中运行的技术栈。概念模型（节点和边的状态机，中间件，检查点器）在任何地方都能泛化。

为什么选这个技术栈而不是Pydantic AI、OpenAI Agents SDK或CrewAI：

- LangGraph是Alice Labs和Channel.tel"什么在实际发布"排名中唯一结合了持久执行、检查点、人在回路、通过LangSmith的一流可观测性和中间件的框架
- `create_agent`（LangChain 1.0，2025年10月）现在是建立在LangGraph运行时之上的默认智能体工厂。`create_react_agent`已被弃用
- Deep Agents（LangChain，2025年8月发布；2026年4月v0.5 alpha）是其上的一个自带电池的线束。规划、虚拟文件系统、子智能体、摘要、技能。它是与Claude Code线束最接近的开源类比，但模型无关

### 1. LangGraph运行时

节点和边的状态图，带有一个让你恢复、回退和分叉的检查点器。

**资源：**

- *LangGraph文档*（免费，官方）——运行时参考。从概念页开始，然后是快速入门
- *Doubling down on Deep Agents*（LangChain）（免费）——干净地定义线束 vs 框架 vs 运行时
- *Context Management for Deep Agents*（LangChain）（免费）——20K令牌工具响应卸载模式和85%上下文窗口压缩触发器
- *On Agent Frameworks and Agent Observability*（LangChain）（免费）——为什么LangSmith是OTEL友好的，不需要LangChain也能工作。即使你以后选择另一个平台也有用
- *Deep Agents v0.5*（LangChain）（免费）——2026年4月发布说明。异步（非阻塞）子智能体、扩展的多模态文件系统支持、异步TODOs。在项目中锁定deepagents版本之前读这个

关注重点：状态模式、节点、边、条件边、PostgresSaver检查点器、时间旅行调试、人在回路中断，以及中间件如何组合。

### 2. 中间件作为定制层

中间件是你在不分叉的情况下定制打包智能体的方式。

**资源：**

- *How Middleware Lets You Customize Your Agent Harness*（LangChain）（2026年3月26日）（免费）——`before_agent`、`wrap_model_call`、`before_tools`、`after_tools`钩子。必读
- *Introducing ambient agents*（LangChain）（免费）——后台智能体UX模式：通知、询问、审查

关注重点：每个钩子在智能体生命周期中触发的位置，SummarizationMiddleware和FilesystemMiddleware如何组合，如何在30行内写一个自定义中间件，以及何时中间件是正确答案而不是写一个新节点。

### 3. 工具、MCP和代码执行模式

天真的"将所有MCP工具加载到上下文中"模式是坏的。正确的模式是带MCP的代码执行。

**资源：**

- *Code execution with MCP*（Anthropic）（2025年11月）（免费，官方）——150K→2K令牌减少。在连接任何MCP服务器之前读这个
- *Introducing advanced tool use*（Anthropic）（免费，官方）——`defer_loading: true`将工具令牌减少了85%，并将Opus 4.5 MCP评估从79.5%提升到88.1%
- *Scaling Managed Agents*（Anthropic）（免费，官方）——会话、线束和沙箱分离。即使你不使用Managed Agents也要读
- *Composio文档*（免费层）——200+SaaS集成，内置MCP网关，代理凭证，使其永远不进入模型上下文
- *Arcade文档*（免费层）——当你需要细粒度的每用户身份而不是服务级别认证时使用

关注重点：`defer_loading`、代码执行作为工具表面、为什么通过模型往返JSON很昂贵，以及Composio或Arcade如何在不将凭证泄露到模型上下文中的情况下代理SaaS认证。

### 4. 不是向量数据库的内存选择

**资源：**

- *Letta MemFS benchmark on LoCoMo*（免费）——2026年4月结果：GPT-4o-mini上的基于文件系统的内存在LoCoMo上达到74%，击败了专用内存工具
- *Mem0文档*（免费）——用户范围的知识内存。为跨会话用户事实选择这个

关注重点：三个内存层（通过PostgresSaver的线程范围、通过Mem0/Zep的用户范围、通过Letta的自管理），为什么文件系统是正确的默认值，以及在实际测量到召回问题之前不要使用向量数据库。

**实践项目：构建一个"研究分析师"深度智能体**

- 输入：一个研究问题
- 主导智能体规划，将TODO列表写入虚拟文件系统，并并行生成3个搜索子智能体，每个都有隔离的上下文
- 子智能体调用Tavily或Firecrawl，将结果写入文件，并将简短摘要返回给父智能体。永远不要将原始搜索结果放入父智能体的上下文
- 一个引用子智能体根据检索到的来源验证声明
- 一个写作智能体生成带有内联引用的最终Markdown报告
- 所有状态通过PostgresSaver持久化。中途终止进程，从中断处恢复
- 人在回路中断：智能体在超过$1令牌前必须请求确认
- 将整个内容包装在一个运行完整管道端到端的`make demo`目标中
- README必须阐明：你使用了哪个中间件及原因，哪些子智能体有隔离的上下文，你的上下文压缩策略是什么，以及进程终止时的持久性方案
- 在README旁边提交一个完整运行的LangSmith追踪URL

### 第2阶段里程碑

在本阶段结束时，你应该能够：

- 构建带有PostgresSaver持久性和人在回路中断的多步LangGraph智能体
- 使用Deep Agents中间件（规划、文件系统、子智能体、摘要）作为打包线束
- 生成隔离上下文的子智能体，并将压缩摘要返回给父智能体
- 阐明你的上下文压缩策略和进程终止时的持久性方案
- 生成一个显示完整多步轨迹的LangSmith追踪URL

---

## 第3阶段：自己构建线束层（3-4周）

**本阶段目标：** 停止使用打包线束，构建一个薄的线束。在你自己构建过一次之前，你永远无法在生产中做出正确的线束权衡。

这是路线图中杠杆最高的阶段。

### 1. "线束"分解为什么

线束是以下内容的集合：

- **循环控制** ——驱动模型→工具→模型的while循环
- **工具调度** ——注册、模式验证、并行调用、错误恢复、重试
- **上下文管理** ——系统提示组装、在窗口85-95%时压缩消息历史、在~20K令牌时卸载工具响应、提示缓存
- **持久性** ——在每个节点检查点状态，以便你可以恢复、回退、分叉
- **子智能体编排** ——生成隔离上下文的子进程，将压缩摘要路由回来
- **技能和渐进式披露** ——仅在相关时加载能力
- **钩子** ——PreToolUse、PostToolUse、PreCompact、Stop、SessionStart（Claude Code列表是规范的）
- **可观测性** ——每次模型调用、工具调用、子智能体调用的OTEL跨度，带有令牌计数和延迟
- **沙箱** ——代码执行和MCP工具调用发生在模型永远没有直接凭证的容器中
- **认证和秘密代理** ——凭证永远不进入模型的上下文（Anthropic Managed Agents模式）

**资源：**

- *The Anatomy of an Agent Harness*（LangChain）（免费）——公开文献中线束组件最清晰的分解。整个阶段的参考文本。在写任何一行线束代码之前读这个
- *Improving Deep Agents with harness engineering* by Vivek Trivedy（LangChain）（2026年2月17日）（免费）——只通过改变线束，在Terminal-Bench 2.0上从第30名到第5名，模型固定为GPT-5.2-codex。配方在帖子里
- *Better Harness: A Recipe for Harness Hill-Climbing with Evals* by Vivek Trivedy（LangChain）（2026年4月29日）（免费）——直接续集。自我验证和追踪作为自主改进线束的配方。在2月17日帖子之后立即阅读这个
- *Inside the Claude Agents SDK*（ML6）（免费）——CPU/RAM/OS/App类比和78% vs 42%线束比较数字
- *everything-claude-code*（Cerebral Valley × Anthropic黑客马拉松获奖者）（免费，GitHub）——启发在哪里停止添加功能
- *deepagents源代码*（免费，GitHub）——将这个与你自己的线束一起作为参考读。中间件文件是线束模式的核心

关注重点：哪些线束组件值得自己写，哪些要导入，以及功能回报的顺序（循环和工具调度在子智能体之前，持久性之前，可观测性之前）。

### 2. 持久执行作为附加组件

**资源：**

- *Inngest文档*（免费）——持久步骤和检查点在2025年12月正式发布。Python线束的最简单持久性路径
- *Temporal Python SDK*（免费）——OpenAI Agents SDK和Temporal集成在2026年3月发布。将每个工具调用视为持久步骤

关注重点：每步的幂等性键、重试策略、进程终止时飞行中的工具调用会发生什么，以及你的线束检查点边界应该在哪里（每个节点，而不是每个令牌）。

**实践项目：用~1,500行Python写一个迷你线束**

- 一个包装`anthropic.messages.create`或LiteLLM的循环，用于模型无关性
- 来自Python装饰器（`@tool`）的工具注册，带有JSON模式生成
- 一个CLAUDE.md风格的系统提示加载器，读取`./harness/rules/*.md`，带路径通配符匹配
- 一个SKILL.md渐进式披露加载器（目标是上下文中每个技能元数据不超过50个令牌）
- 一个带有隔离上下文的子智能体生成原语，将摘要字符串返回给父智能体
- 文件系统卸载：任何超过20K令牌的工具结果写入`./workspace/<id>.txt`，并在上下文中替换为路径加10行预览
- 在上下文窗口85%时自动压缩：总结最后10轮之前的消息
- 一个可插拔钩子系统（`pre_tool`、`post_tool`、`stop`）
- 通过`opentelemetry-sdk`的OpenTelemetry追踪，导出到LangSmith或Phoenix（两者都支持OTEL）
- 持久恢复：在每步后将消息历史和状态持久化到SQLite，按运行ID重新加载
- 可选附加：将整个内容包装在Inngest或Temporal中，使每个工具调用成为持久步骤

### 第3阶段里程碑

在本阶段结束时，你应该能够：

- 列出现代线束的十个组件，并解释每个何时值得
- 用带有循环、工具调度、上下文压缩、子智能体、钩子和OTEL追踪的1,500行Python写一个线束
- 通过Inngest或Temporal连接持久执行，使进程终止可恢复
- 写一份1,000字的事后分析，比较你的迷你线束与Claude Agent SDK和Deep Agents。你做对了什么，你削减了什么，你会有什么不同的做法

事后分析才是真正的交付物。代码只是证据。

---

## 第4阶段：构建评估和回归线束（3-4周）

**本阶段目标：** 使你的智能体可测量。没有这个，每一个"改进"都是感觉。

这是大多数工程师停滞的地方。他们可以构建一个很棒的智能体，但无法判断他们的下一个改变是否使它更好或更差。

### 1. 精确选择一个可观测性平台

不要同时运行两个。五个真正的选择：

- **LangSmith** ——如果你住在LangGraph或LangChain中就选这个。原生追踪。2026年3月添加了沙箱、Polly调试助手、技能和Fleet（智能体身份/共享）
- **Braintrust** ——如果你想要阻止PR的框架无关CI质量门控就选这个。2026年2月8000万美元B轮。无限用户固定249美元/月，而LangSmith是39美元/座位
- **Arize Phoenix**（开源）和**Arize AX**（托管）——如果你想要OpenTelemetry原生、漂移检测和从OSS到托管的清晰迁移路径就选这个
- **W&B Weave** ——如果你已经在使用Weights & Biases做ML就选这个。现在有完整的智能体追踪视图、MCP自动日志记录和即将推出的A2A追踪
- **Inspect（英国AISI）** ——基准级别的评估选这个。GAIA、SWE-bench、Cybench、BFCL都作为`inspect_evals`包发布。由Anthropic、DeepMind和Grok内部使用

**资源：**

- *LangSmith文档*（免费层，官方）——生产追踪、在线评估、实验和新的Polly调试助手
- *Inspect AI annotated notes* by Hamel Husain（免费）——Hamel的注释是我依赖的从业者写作。在安装Inspect之前读这个
- *Inspect文档*（免费，官方）——框架参考
- *inspect_evals*（免费，GitHub）——200+标准评估作为Python包。GAIA、SWE-bench、Cybench、BFCL
- *Braintrust文档*（免费层）——框架无关实验、CI门控和黄金数据集
- *Agent Evaluation Readiness Checklist*（LangChain）（免费）——17分钟实践清单：错误分析、数据集构建、评分者设计、离线和在线评估、生产就绪性。打印这个，在整个阶段贴在你的显示器上
- *Quantifying infrastructure noise in agentic coding evals*（Anthropic）（2026年2月5日）（免费，官方）——单独的不稳定沙箱和网络抖动就可以使评估分数波动几个点。在你信任任何智能体基准数字（你的或别人的）之前，读这个

关注重点：追踪采样策略、在线vs离线评估、指标和护栏的区别，以及为什么CI门控是将评估从仪表板壁纸变成开发工具的模式。

### 2. 你必须实现的四种评估类型

根据Anthropic的"Demystifying evals for AI agents"：

1. **单轮评估：** 给定这个输入，输出对吗？最便宜，尽可能使用确定性评分者，持续运行
2. **轨迹评估：** 智能体是否用正确的参数调用了正确的工具序列？测试单步、全轮和多轮变体
3. **LLM作为评判者：** 用于开放性输出（研究报告、代码审查）。每周根据人工评分示例进行校准。Anthropic的研究智能体评分标准使用0.0-1.0，跨越事实准确性、引用质量、完整性、来源质量、工具效率
4. **最终状态评估：** 用于有状态智能体（数据库写入、文件编辑）。将环境的最终状态与基准真相进行比较。这是τ-bench的方法

**资源：**

- *Demystifying evals for AI agents*（Anthropic）（免费，官方）——Anthropic关于这个主题的最佳入门
- *Evaluating Deep Agents: Our Learnings*（LangChain）（免费）——单步、全轮和多轮轨迹评估模式。从业者指南
- *How we build evals for Deep Agents*（LangChain）（免费）——配套文章。他们如何实际获取数据、设计指标和运行范围合理的评估。与上面的帖子配合读
- *Eval awareness in Claude Opus 4.6's BrowseComp performance*（Anthropic）（2026年3月6日）（免费，官方）——模型可以检测到它们何时被评估并表现不同。在设计你的评估套件之前读这个，否则你会把偏见烘焙进去
- *Designing AI-resistant technical evaluations*（Anthropic）（2026年1月21日）（免费，官方）——如何设计不被你正在评分的模型欺骗的评估。如果你自己推出基准测试必读
- *τ²-bench仓库*（免费，GitHub）——带政策合规的多轮客户服务评估
- *Establishing Best Practices for Building Rigorous Agentic Benchmarks*（arXiv）（免费）——在设计任何原创内容之前读这个。SWE-bench、KernelBench和WebArena都高估了5-33%

关注重点：如何在可以的地方写确定性评分者，如何根据人类评分校准LLM评判者，何时pass^k比pass@1更重要，以及如何检测和丢弃受污染的基准。

**实践项目：围绕你的第2阶段研究智能体构建一个回归线束**

- 构建一个30-50个手工评分研究问题的黄金数据集，跨越三个难度级别（1/2/3级，GAIA风格）
- 在可能的情况下实现确定性评分者（事实性查询的精确匹配）和用于开放性评分者的具有5个标准评分标准的LLM作为评判者
- 构建轨迹评估：智能体是否规划了，生成了≥2个子智能体，引用了来源，在预算内完成了？
- 连接到GitHub Actions：每个PR运行完整套件。如果黄金集通过率下降≥3分或任何pass^4指标下降，则阻止合并
- 添加生产采样：1%的实时追踪每晚由LLM作为评判者自动评分。在漂移时发出警报
- 通过Inspect对至少一个已发布的基准重新运行智能体：GAIA第1级或τ²-bench零售。将你的数字与公开排行榜进行比较
- 提交一个`make eval`目标，生成三个工件：CI通过/失败摘要、LangSmith实验URL和带有一个规范基准分数的Inspect日志文件

### 第4阶段里程碑

在本阶段结束时，你应该能够：

- 选择一个可观测性平台并从架构基础辩护这个选择
- 实现所有四种评估类型：单轮、轨迹、LLM作为评判者、最终状态
- 维护一个从生产失败而不是合成数据中增长的黄金数据集
- 在CI中评估分数回归时阻止PR
- 生成一个`make eval`目标，发出CI通过/失败摘要、LangSmith实验URL和带有一个规范基准分数的Inspect日志文件
- 记录你在自己的智能体中发现的失败模式——那份文档才是真正的产品

---

## 第5阶段：生产强化（持续）

**本阶段目标：** 把你构建的一切都做到能在真实用户、真实成本和真实失败下存活。

这是永久性的，不是你完成的阶段。

### 1. 成本纪律

- 积极使用提示缓存。Anthropic的缓存在重复前缀上节省高达90%。缓存你的CLAUDE.md、系统提示和工具定义
- 按难度路由：简单轮次使用Haiku 4.5或Sonnet 4.6，规划和难推理使用Opus 4.7
- "advisor tool" beta（Anthropic，2026年3月）让你在生成中间将执行者与高IQ顾问配对
- 注意Opus 4.7分词器：与4.6价格标签相同，但同样文本的计费令牌约为1.0-1.35倍。迁移后重新测量每任务成本
- 非实时工作负载的批处理API减少50%
- 多智能体（Anthropic风格研究）：期望约为单智能体聊天令牌的15倍。只有当答案的价值超过那个门槛时才运行多智能体

**资源：**

- *Open Models have crossed a threshold*（LangChain）（免费）——GLM-5和MiniMax M2.7现在在核心智能体任务（文件操作、工具使用、指令遵循）上匹配封闭的前沿模型。在锁定你的模型选择和路由策略之前读这个

关注重点：提示缓存边界、模型路由规则、批处理vs实时决策，以及你监控的硬性每任务成本预算。

### 2. 延迟

- 并行工具调用。Anthropic的研究系统提示字面上说"创建多个子智能体时必须使用并行工具调用"。同样适用于你自己的智能体
- 通过LangGraph的`stream_mode="updates"`向UI流式传输部分输出
- 子智能体扇出是最大的单一延迟杠杆：一个60步顺序智能体变成一个10步主导加5个并行10步子智能体

关注重点：并行性在哪里是安全的，流式传输在哪里改变UX，以及扇出如何与成本交互。

### 3. 安全和沙箱

- 所有代码执行在沙箱中：Modal、E2B、Daytona或LangSmith沙箱（私人预览，2026年3月）。永远不要在你的主进程中`exec()`模型输出
- 凭证在模型上下文之外代理（Anthropic Managed Agents模式；Composio处理SaaS认证）
- 护栏钩子：阻止破坏性Bash的PreToolUse钩子、正则表达式阻止秘密、验证文件写入路径
- 任何不可逆动作的人在回路中断（LangGraph的`interrupt()`加HumanInTheLoopMiddleware，Claude Agent SDK的权限提示）

**资源：**

- *Modal文档*（免费层）——Python代码执行的默认沙箱
- *E2B文档*（免费层）——为AI智能体设计的代码执行沙箱
- *Beyond permission prompts: making Claude Code more secure and autonomous*（Anthropic）（2025年10月20日）（免费，官方）——基础沙箱帖子。Claude Code如何停止为安全操作请求权限并控制不安全的操作。你的线束应该复制的模式
- *Claude Code auto mode: a safer way to skip permissions*（Anthropic）（2026年3月25日）（免费，官方）——后续。当你让智能体无人值守运行时会发生什么变化。在生产中翻转任何"跳过确认"标志之前读两篇

关注重点：哪些动作是可逆的，哪些需要人工批准，以及如何确保模型永远看不到它使用的凭证。

### 4. 监控和漂移

- 低规模100%追踪采样；高规模降采样到1-10%，对错误进行分层采样
- 警报：每次请求的令牌成本、工具调用失败率、LLM作为评判者平均分数（每晚）、p95延迟、评估回归
- 每次模型升级后重新基准评估
- Anthropic自己的工程博客警告："线束对模型自己做不到的事情编码了假设；随着模型改进，这些假设会变得陈旧"（Sonnet 4.5 → Opus 4.5的"上下文焦虑"例子）

关注重点：什么值得警报vs什么值得日志，如何检测提示缓存失效，以及当模型超过它时如何发现线束僵化。

### 5. 弹性

- 持久执行（Inngest、Temporal或LangGraph PostgresSaver）对于运行超过60秒的任何智能体来说是不可谈判的
- 在每个节点后检查点。回退和分叉应该是可能的。Pydantic Deep Agents和LangGraph都支持这个。Claude Agent SDK的会话日志是等效的

**资源：**

- *How My Agents Self-Heal in Production*（LangChain）（免费）——一个在每次部署后检测回归、分类原因并在没有人在回路的情况下打开修复PR直到审查的工作管道。窃取这个模式

关注重点：哪种失败你可以自动恢复，哪些需要人工升级，以及如何在生产流量强制问题之前测试你的恢复路径。

### 第5阶段里程碑

这个阶段不会结束。但你应该有：

- 在系统提示、CLAUDE.md和工具定义中连接了提示缓存
- 带有硬性每任务成本预算和警报的模型路由层
- 所有代码执行的沙箱和将秘密保持在上下文之外的凭证代理
- 阻止破坏性动作并强制不可逆动作人工批准的钩子
- 追踪采样、漂移警报和每次模型升级的重新基准仪式
- 使进程终止成为非事件的持久执行层

---

## 推荐

今天你可以采取行动的决策性见解。

**如果你只学一个框架：** LangGraph 1.0 + Deep Agents。它是最通用的，其运行时故事今天是最成熟的（PostgresSaver、时间旅行调试、持久执行、通过LangSmith的OTEL友好可观测性），它是模型无关的，而且抽象（状态图加中间件）是可泛化的思维模型。句号。

**如果你只学一个线束作为参考：** Claude Agent SDK加Claude Code。它是参考示例。CLAUDE.md、技能、子智能体、钩子、计划模式、文件系统作为内存模式。2026年的每个其他线束都在向这些原语收敛。每天使用Claude Code，阅读其文档，研究开源线束汇编。

**如果你只读一件关于上下文的事：** Anthropic的"Effective context engineering for AI agents"（2025年9月）。如果你只读两件：加上LangChain的"Context Engineering for Agents"，以获得Write/Select/Compress/Isolate框架。

**如果你只学一个可观测性工具：** 如果你待在LangGraph，LangSmith。如果你想要框架无关CI门控，Braintrust。如果你想要基准级别的严格性，Inspect（你最终应该）。

### 2026年跳过的内容

- AutoGen v0.4（合并到Microsoft Agent Framework，社区血统是AG2。都不是强默认）
- OpenAI Swarm（官方被取代，根据OpenAI自己的README明确"不适合生产"）
- Assistants API（2026年中停用）
- 在实际测量到召回问题之前构建自己的向量存储或内存
- "无代码"智能体平台，除非你在构建一次性的东西

### 只有在有特定原因时才使用

- **CrewAI** ——最快的想法到原型，在生产中脆弱。用于黑客马拉松和演示
- **OpenAI Agents SDK** ——如果你被OpenAI锁定就可以。2026年4月更新添加了沙箱和线束，但你仍然绑定到OpenAI模型
- **Pydantic AI / Pydantic Deep Agents** ——如果你是严格类型的FastAPI商店就选这个
- **Mastra** ——只有当你的团队是TypeScript且不能使用Python时才选这个。2026年1月v1.0，YC W25，22k+星，由Gatsby团队构建
- **Smolagents** ——代码智能体模式最好的教学工具（其1,000行代码库可黑客）。生产能力弱
- **DSPy 3.0 + GEPA** ——当你有指标并想要以编程方式优化提示和智能体拓扑时。GEPA以35倍更少的rollout胜过RL 6%（ICLR 2026口头）
- **Letta / MemGPT** ——如果你需要跨会话的操作系统风格智能体自管理内存。否则文件系统加Mem0更简单

### 要收藏的基准（2026年5月数字）

- **SWE-bench Verified：** Claude Opus 4.7 ≈ 87.6%，GPT-5.5 ≈ 88.7%，Gemini 3.1 Pro ≈ 78.8%
- **Terminal-Bench 2.0：** GPT-5.5 82.7%，Opus 4.7 ~70%，Gemini 3.1 Pro ~68%
- **τ-bench：** Claude Mythos Preview 89.2%领先
- **BrowseComp：** GPT-5.5 90.1%，Gemini 3.1 Pro 85.9%，Opus 4.7 79.3%（4.6的83.7%的退步。将网络研究路由到GPT-5.5）
- **GAIA / Princeton HAL：** Sonnet 4.5以74.6%领先

### 对于技术能力强的新手智能体工程师的时间盒里程碑

- **第2周：** 第0阶段完成。你可以用简单英语解释线束
- **第5周：** 第1阶段完成。Claude Agent SDK智能体发布，带有一个技能、一个钩子、一个子智能体
- **第9周：** 第2阶段完成。带有PostgresSaver持久性和LangSmith追踪的LangGraph深度智能体研究分析师运行
- **第13周：** 第3阶段完成。1,500行迷你线束，编写和记录，与精简的Claude Agent SDK能力相当
- **第17周：** 第4阶段完成。黄金数据集、CI门控、通过Inspect运行一次已发布的基准
- **永久：** 第5阶段

如果你在10-15小时/周兼职，乘以约2.5倍。

改变计划的基准：如果你在3周内无法让第1阶段工作，你的工具设计是错误的（重读"Writing tools for agents"）。如果第2阶段花了超过5周，你也在试图构建线束。降到Deep Agents，停止对抗它。

---

## 注意事项

如果你没有提前看到这些，它们会让你绊倒。

### 基准是移动目标，部分被操纵

SWE-bench Verified分数在两年内从1.96%到80%+。τ-bench的pass^k一致性指标正是因为单次运行准确性不再有意义而被添加。将任何"X模型得了Y%"的声明视为与线束、脚手架、重试预算和系统提示联合的。不是模型单独的。

### 多智能体对大多数用例被过度炒作

Anthropic报告的90.2%改进是专门针对广度优先研究的。对于编码和紧密耦合的任务，多智能体通常表现比单智能体差，并消耗15倍的令牌。默认到单智能体加子智能体进行有限探索。只有在任务自然分解时才使用完整多智能体。

要收藏的反例：Anthropic的"Building a C compiler with a team of parallel Claudes"（2026年2月5日）展示了并行子智能体确实有回报的编码任务。多智能体对代码来说没有死，只是需要正确的分解。

### 2026年来源中的推测标志

几个"AI 2027"预测（OpenBrain 450亿美元收入等）明确是虚构的，但被引用为统计数据。忽略它们。发布周接待文章是轶事性的。将其视为开发者情绪信号，而不是基准。

### 框架格局可以再次改变

LangChain自己的框架在18个月内移动了两次（链→图→图上的线束）。Pydantic AI、Mastra或Deep Agents中的任何一个在12个月内都可能更大。在抽象上（循环、工具、上下文、子智能体、持久性、追踪）而不是任何一个库上下注。那些能延续。

### MCP的生产粗糙边缘是真实的

负载均衡器后面的可流式HTTP、多租户认证、速率限制、审计日志。所有这些明确在2026年MCP路线图上，意味着它们还没有解决。为2026年末登陆的下一代传输SEP做计划，不要深度耦合到当前会话模型。

### 模型特定行为在小版本之间变化

Opus 4.7更严格的指令跟随和新分词器意味着你的Opus 4.6提示可能表现不同，相同文本的令牌成本高达35%。在每次模型升级时重新重播流量。

### 你的评估套件会腐烂

今天构建的黄金数据集将在几个月内随模型改进而饱和。计划每季度从生产失败而不是合成数据中增长10-20%。无限期保持LLM作为评判者的人类校准运行。

### 本路线图中的一些来源是供应商推销的

在可能的情况下依靠主要来源（Anthropic工程博客、LangChain博客、OpenAI公告、arXiv）。排名风格的"2026年最佳"帖子（Alice Labs、Channel.tel、GuruSup、Morph、Vstorm）是有用的三角验证，但每个都有商业利益。在它们相互同意以及与主要工程来源同意的地方，将共识视为可靠的。

---

## 结论

我要对你诚实，不加任何糖。

这份路线图不会在17周内让你成为首席AI工程师。但它会让你成为可以构建和发布在生产流量下存活的智能体系统的人。这恰好是公司现在愿意支付的事情。

对可以发布生产智能体的工程师的需求没有放缓。LangChain智能体工程现状报告中57%的团队已经有了生产中的智能体，其中89%连接了可观测性。质量是#1障碍（32%），这意味着整个领域瓶颈在于能够构建评估和线束的工程师，而不是能够调用LLM API的工程师。

Anthropic自己的数字捕捉了真正的机会：同样的模型，不同的线束，**78% vs 42%的CORE**。那个差距就是你的工作。

线束工程转变是软件招聘中目前最大的错误定价。公司仍然发布"提示工程师"职位。他们需要的是能够取得前沿模型并将其变成可测量和持久的生产系统的工程师。

现在这里是我希望你从这一切中带走的：

**从每个阶段选择一个项目并构建它。** 不是读关于它的内容。构建它，打破它，修复它，部署它，然后在你的README中放一个LangSmith追踪和一个基准分数。被雇用的工程师是那些能展示追踪的人，而不是那些能背诵框架比较表的人。

**开始分享你所学的。** 写下你的迷你线束事后分析。发布你的黄金数据集发现。用产生它的线束配置发布你的基准数字。教学是最快的学习方式，它同时建立你的声誉。最好的机会来自于可见的工程师，而不是申请了500个职位的工程师。

**请不要等到你感觉准备好了。** 你永远不会感觉准备好。"我在读LangChain博客"和"我在发布带有PostgresSaver持久性的深度智能体"之间的差距是大多数工程师永远卡住的地方。

一旦你有了可工作的智能体就开始申请，开始公开构建，开始发布。即使它很小。市场不奖励完美。它奖励能使模型做真实的事情并证明它没有退步的工程师。

17周足以改变一切，如果你投入工作。我相信你们每个人都能做到。

只是继续构建并继续测量你构建的。

---

*这篇文章由作者根据他在2到3个月内积累的内部笔记和手记写成，并由Minimax 2.7编辑。作者在Obsidian上有一个内容管道，这些内容在该管道中根据他的手写和手打笔记按他的风格写作。*
