# 如何在2026年成为AI工程师（构建者路线图）

**作者：** Avid ([@Av1dlive](https://x.com/Av1dlive))  
**日期：** 2026年5月7日  
**来源：** [How to Become an AI Engineer in 2026 (Builder's Roadmap)](https://x.com/Zephyr_hg/status/2052063154423898603)

用AI，一个周末就能做出下一个十亿美元的产品。

你唯一需要学的，是**Agent 系统与运行框架工程（harness engineering）**。

> 懒得读7862字？直接把这个链接交给你的 Agent，让它帮你生成个性化路线图：➡️ https://raw.githubusercontent.com/codejunkie99/agent-roadmap-2026/main/AGENT.md

大多数工程师的问题不是能力不够，而是不知道该学什么。

有人选 CrewAI，因为它在 Twitter 上的演示看起来很酷。有人追着每一个新框架跑，永远做不完一件真正的东西。还有人直接跳进多 Agent 系统，连上下文管理、工具设计、运行框架是什么都还没搞清楚。

结果都一样：刷了很多框架，没有一个能上生产。

如果你的目标是在2026年成为一名 Agent 工程师，你不需要学12个框架。你需要学的是：如何构建、配置、评估、并把真正的 Agent 系统发布到生产环境。

具体来说，包括：

- 在 LangGraph 这样的编排运行时上构建 Agent
- 把 Claude Agent SDK 当作参考运行框架来研究
- 用 Write、Select、Compress、Isolate 四个原语做好上下文工程
- 写出模型能正确调用的工具
- 为生产流量加上内存、持久化和沙箱
- 建立 eval、轨迹检查和 CI 回归门控
- 让 Agent 真正扛得住真实用户和真实成本

这份指南是一个六阶段路线图，所有内容都来自2025年底到2026年初的一手资料，文章超过7000字。它的价值在于：每个阶段都有具体项目、精选阅读清单和你真正需要的资源。

按照这份路线图，专注工作约**17周**，你就能达到独立负责一个生产 AI 功能的水平。

写这份路线图，花了超过**60小时**阅读工程博客、论文和一线工程师调查。

好，开始读路线图 ⬇️

---

## 2026年的 Agent 工程师，在做什么

很多人听到"AI Agent 工程师"，脑子里出现的是：有人把几个 CrewAI 角色拼在一起，然后说"搞定了"。

实际上，大多数 Agent 工程师做的事情要务实得多。他们在前沿模型之上构建、配置和运营 Agent 系统。

这通常包括：

- 设计 Agent 循环和工具调度机制
- 用 Write、Select、Compress、Isolate 做上下文工程
- 写出模型能正确选择的工具
- 用隔离上下文窗口编排子 Agent
- 加上技能（Skill）、内存、持久化和沙箱
- 接入 eval、追踪和 CI 门控，让"改进"变得可以度量

同样的模型，不同的运行框架，结果可以天差地别。**Anthropic 自己的测量数据：同样的 Opus 4.5，在 Claude Code 内部跑，CORE 评分78%；在 Smolagents 里跑，42%。同一个模型，仅此而已。**

这36个百分点的差距，就是运行框架工程（harness engineering）。这份路线图讲的就是这件事。

每个 Agent 构建者都要掌握的四个上下文原语：**Write**（草稿本、内存文件）、**Select**（在需要时检索）、**Compress**（在上下文窗口占用85-95%时摘要）、**Isolate**（让子 Agent 拥有独立的上下文窗口）。

Anthropic 的多 Agent 研究系统，用的就是这套模式。在广度优先研究任务上，比单 Agent Opus 4 提升了 **90.2%**，代价是消耗了约15倍的 token。

2026年，真正值得深入学的技术栈只有两个：**LangGraph 1.0 + Deep Agents** 和 **Claude Agent SDK**。其他的要么在慢慢退出舞台，要么被吸收合并，要么只是这两个在生产环境下的劣化版本。

---

## 整个路线图中的免费资源

下面是一些持续输出高质量内容的博客、课程、频道和通讯，全部免费。在第0阶段就订阅好，后续路线图的内容就会跟着新的文章、案例和一手资料不断更新。

没有付费墙，大部分更新速度比任何教科书都快。

### 值得订阅的工程博客

- **Anthropic 工程博客**（免费，官方）——如果只读一个博客，就读这个。上下文工程、运行框架设计、多 Agent 研究、高级工具使用、eval——全是一手资料，整个路线图里反复引用
- **LangChain 博客**（免费）——运行框架、中间件和 Deep Agents 规范公开成型的地方。Lance Martin、Vivek Trivedy 和 Harrison Chase 的文章都值得读
- **OpenAI Cookbook**（免费，GitHub）——每个 API 功能的可运行 Notebook。工具使用、结构化输出、eval、Agent——跟着敲代码，不要只是看
- **Hamel Husain 的博客**（免费）——"你的 AI 产品需要 eval"是这个领域最常被引用的 eval 文章。网站上其他文章水平相当，如果你做 eval，读两遍
- **Eugene Yan 的博客**（免费）——"构建基于 LLM 的系统和产品的模式"，每个从业者都引用的文章，有观点，接地气
- **Lilian Weng 的博客**（免费）——关于 Agent、Prompt 工程、幻觉、对齐的长篇深度文章，这个领域综合写作最清晰的之一
- **Simon Willison 的博客**（免费）——一位在一线发布产品的工程师的每日笔记，适合拿来拆穿炒作，也常常第一个发现奇怪的边缘 case
- **Chip Huyen 的博客**（免费）——从基本原理出发的 ML 系统。她的"为生产环境构建 LLM 应用"是第5阶段之前的必读
- **Phil Schmid 的博客**（免费）——HuggingFace、Gemini、微调、部署的实战端到端指南，总是配上代码
- **Cameron Wolfe 的 Deep (Learning) Focus**（免费）——长篇论文解析，一篇文章帮你跟上一个研究方向

### 值得完成的免费课程

- **DeepLearning.AI 短期课程**（免费）——大部分1-2小时，几乎全免费。第0阶段要完成两门：LangGraph 课程（和 LangChain 联合出品）和 Andrew Ng 的"Agentic AI"课程（反思、工具使用、规划、多 Agent 设计模式）
- **LangChain Academy：LangGraph 入门**（免费）——官方免费课程，涵盖状态、内存、人在回路、多 Agent。第2阶段完成
- **Anthropic 交互式 Prompt 工程教程**（免费，GitHub）——九章 Jupyter Notebook，对着 Claude API 做。建立 Prompt 直觉最快的方式
- **HuggingFace Agent 课程**（免费）——从头到尾覆盖 Agent、smolagents、MCP 和评估，完成后有免费证书
- **HuggingFace LLM 课程**（免费）——基础：tokenization、Transformer、微调。即使你只在 API 层构建，也值得了解背景
- **FreeAcademy 的 MCP 基础课程**（免费）——构建 MCP 服务器、连接 Claude、写自定义工具，最快入门 MCP 的路径

### YouTube 频道和演讲

- **Andrej Karpathy**（免费）——《神经网络：从零到英雄》，用纯 Python 从头搭 GPT。他在 Sequoia AI Ascent 的2026年演讲"Vibe Coding to Agentic Engineering"，是目前解释运行框架工程为何重要最清晰的一次
- **AI Engineer**（免费）——所有 AI Engineer Summit 和 World's Fair 演讲。重点搜索 Hamel Husain、swyx、Anthropic 工程师和 Erik Schluntz 的内容
- **LangChain**（免费）——每周关于 LangGraph、Deep Agents、中间件和集成的教程，新功能通常最先以视频形式在这里发布
- **Anthropic**（免费）——Anthropic 工程师的演讲：多 Agent 研究演示、Claude Code 内部原理、Skills 功能
- **Yannic Kilcher**（免费）——论文解析，省去你自己啃 arXiv 预印本的时间
- **Lex Fridman 播客**（免费）——和 AI 领域核心人物的长篇对话：Karpathy、Schulman、Sutskever、Amodei

### 值得订阅的通讯

- **Latent Space（swyx & Alessio）**（免费）——AI 工程师的技术通讯，有 AINews 每日简报、播客和年度"AI 工程阅读清单"。只订一个的话就选这个
- **The Batch（Andrew Ng）**（免费）——每周广谱覆盖，适合发现哪些新东西正在崭露头角
- **Import AI（Jack Clark，Anthropic 联创）**（免费）——政策加研究摘要，最接近这个领域战略视角的内容
- **Ben's Bites**（免费）——五分钟每日 AI 资讯，快速浏览，适合不漏掉重要公告
- **TLDR AI**（免费）——每日摘要，低噪音，配合上面某个更深度的通讯一起用
- **AI Engineer Pack（swyx）**（免费）——为 AI 工程师整理的免费额度、工具和资源，持续更新

### 值得研究的开源项目

- **Anthropic Cookbook**（免费，GitHub）——每个工作流模式的参考实现。第0阶段就加入清单，每个阶段结束后重读一遍
- **OpenAI Cookbook**（免费，GitHub）——同类内容，OpenAI 视角。工具使用、结构化输出、eval、Agent
- **LangChain 的 deepagents**（免费，GitHub）——LangGraph 之上的参考开源运行框架，在第3阶段构建自己的框架层时，重点看中间件文件
- **LangGraph 示例**（免费，GitHub）——可运行的 LangGraph 模式：监督者、层级团队、规划、客服 Agent
- **inspect_evals**（免费，GitHub）——200+ 标准 eval 打包成 Python 包，GAIA、SWE-bench、Cybench、BFCL 都有
- **awesome-agentic-engineering-resources**（免费，GitHub）——社区维护的 Agent 工程资源索引，用来补全本路线图没覆盖的角落

### 通勤播客

- **Latent Space**（免费）——和推动这个领域发展的人的长篇对话：Anthropic、OpenAI、LangChain、Modal、E2B 都有嘉宾
- **Dwarkesh Podcast**（免费）——AI 战略、能力和政策的长篇访谈，重视一手来源
- **TWIML AI Podcast（Sam Charrington）**（免费）——每周与研究人员和工程师的技术访谈
- **Practical AI**（免费）——工程导向，少炒作，聚焦实际发布
- **The MAD Podcast（Matt Turck）**（免费）——数据和 AI 生态的创始人+投资人视角，适合追踪谁在真正出货、谁在圈钱

### 值得加入的社区

- **LangChain Discord**（免费）——LangGraph 和 Deep Agents 核心团队在这里，#help 频道很活跃
- **HuggingFace Discord**（免费）——最大的开放权重和 ML 社区
- **r/LocalLLaMA**（免费）——开放权重模型新闻、基准和工具，经常比官方渠道更快
- **AI Engineer World's Fair**（免费注册）——这个领域的专业网络，有职位发布、招聘频道和工作组
- **Anthropic Discord**（免费）——Claude 开发者社区，分享 Skill 方案、Hook 模式、MCP 服务器

第0阶段的策略：选一个博客、一份通讯、一个播客、一个社区，专注跟进。不要一下子追40+个资源。等现有的不再给你带来惊喜，再加新的。这份清单的意义是给你选择的依据，不是让你全部完成的待办清单。

---

## 第0阶段：打好基础（1-2周）

**本阶段目标：** 建立正确的心智模型。除了随手试验的脚本，先不要写任何 Agent 代码。

大多数人跳过这个阶段，直接扎进框架教程，然后代码一出问题就不知道该往哪里看。别跳过。

### 1. 增强型LLM，以及"工作流"和"Agent"的区别

在动手写框架之前，你需要先理解 Anthropic 归纳的五种工作流模式（提示链、路由、并行化、编排者-工作者、评估者-优化者），还要搞清楚工作流和 Agent 的根本区别：

- 工作流：控制流是你写死的
- Agent：在循环内自己决定下一步干什么

搞清楚这个区别，能帮你避免把本该是链式流程的东西做成 Agent。

**参考资料：**

- *Building Effective Agents*（Anthropic，Erik Schluntz & Barry Zhang，2024年12月，免费官方）——五种工作流模式加增强型LLM概念，这个领域人手必读，先读这篇
- *Anthropic Cookbook*（patterns/agents 文件夹，免费 GitHub）——每种工作流模式的参考实现，可运行的 Notebook。跟着敲，别只看
- *Simon Willison 对 Building Effective Agents 的注解*（免费）——老工程师视角，帮你拆穿里面的炒作成分

重点搞清楚：工作流和 Agent 的区别、增强型LLM的概念、编排者-工作者模式、为什么并行化通常比顺序推理强，以及 Anthropic 明确提醒的失败模式。

### 2. 上下文工程：一门独立的学科

2026年，"Prompt 工程"作为独立技能基本已经过时了。取而代之的是**上下文工程**：在循环的每一步，决定模型面前放什么 token。

**参考资料：**

- *Effective context engineering for AI agents*（Anthropic，2025年9月29日，免费官方）——这篇读两遍，把框架背下来
- *Context Engineering for Agents*（Lance Martin，LangChain，免费）——Write/Select/Compress/Isolate 框架，你需要掌握的核心心智模型
- *How we built our multi-agent research system*（Anthropic，2025年6月，免费官方）——编排者-工作者参考架构、90.2%广度优先提升、15倍 token 代价这几个数字都在这里
- *Simon Willison 对多 Agent 研究文章的注解*（免费）——对架构和成本权衡的理性检验

重点搞清楚：Write/Select/Compress/Isolate 各自在代码层面是什么，子 Agent 为什么是隔离原语而不是并行原语，以及什么时候该用压缩、什么时候该卸载、什么时候该摘要。

### 3. 运行框架（Harness）：像操作系统一样理解它

**参考资料：**

- *The Complete Guide to Harness Engineering*（ClaudeCodeLab，免费）——三级 harness 升级方案，带可运行代码
- *Inside the Claude Agents SDK*（ML6，免费）——CPU/RAM/OS/App 类比，以及支撑这整份路线图的 78% vs 42% 数字
- *Building agents with the Claude Agent SDK*（Anthropic，免费官方）——SDK 为何存在，为何从 Claude Code SDK 改名
- *Effective harnesses for long-running agents*（Anthropic，2025年11月26日，免费官方）——Anthropic 自己的 harness 入门。配合 Vivek Trivedy 的文章一起读，两个团队视角互相印证
- *Harness design for long-running application development*（Anthropic，2026年3月24日，免费官方）——续篇，Session 拉长到数小时甚至数天时有哪些变化，第3阶段也要读
- *How to think about agent frameworks*（Harrison Chase，LangChain，免费）——编排框架和抽象层的区别，在你选任何东西之前必读

重点搞清楚：循环、工具调度、上下文管理、持久化、Hook、子 Agent 编排、可观测性——以及这些在你将来遇到的每一个 harness 中是如何实现的。

### 4. 2026年的领域现状

**参考资料：**

- *State of Agent Engineering*（LangChain，免费）——1340份调研，2025年11-12月。把这些数字记住：57%的团队 Agent 已上生产，89%有可观测性，52%有 eval，质量（32%）是头号障碍
- *How to Build an Agent*（LangChain，免费）——"聪明实习生"框架，帮你想清楚 Agent 应该和不应该负责什么
- *Continual learning for AI agents*（Harrison Chase，LangChain，免费）——Agent 真正学习的三个层面：权重、Prompt、内存。在你想到微调之前，先把这个框架搞清楚

重点搞清楚：生产环境里团队在哪里卡住（质量、成本、可靠性），中位数技术栈长什么样，以及投入时间性价比最高的地方在哪。

**实践项目：** 手写一份2页的个人文档，用自己的话定义：工作流 vs Agent、增强型LLM、四个上下文工程原语、编排者-工作者模式、harness/模型/框架的区别，以及你预计自己代码里会出现的前三个失败模式。这份文档本身就是交付物。写不出来就说明还没真正看进去。

### 第0阶段里程碑

阶段结束时，你应该能：

- 不用框架术语，解释清楚 Agent 是什么，跟工作流有什么区别
- 说出四个上下文工程原语，并给出每个的代码级示例
- 解释为什么2026年 harness 的贡献比模型本身更大
- 讲清楚编排者-工作者模式和15倍 token 代价
- 在架构层面选择框架，而不是跟着感觉走

---

## 第1阶段：做出第一个简单的 Agent（2-3周）

**本阶段目标：** 把同一个使用工具的 Agent 做两遍。第一遍用 Anthropic 的原始 SDK，第二遍用 Claude Agent SDK。亲身感受自己手搓循环和站在真正 harness 上的区别。

这是理解 harness 到底给你带来什么的成本最低的方式。

### 1. 从头开始写 Agent 循环

循环本身不复杂。用消息和工具调用模型，解析出 `tool_use` 块，执行工具，追加 `tool_result`，重复，直到 `stop_reason` 等于 `end_turn`。

自己用100行写一遍，之后每个框架都能看懂。

**参考资料：**

- *Tutorial: Build a tool-using agent*（Anthropic 文档，免费官方）——`tool_use`、`tool_result`、并行工具调用和响应循环的参考
- *Writing tools for agents*（Anthropic，免费官方）——设计工具之前先读这篇。工具和参数的描述，就是给 LLM 看的使用说明书
- *Equipping agents for the real world with Agent Skills*（Anthropic，免费官方）——渐进式披露模式，由写规范的团队解释

重点搞清楚：请求/响应循环如何终止，`stop_reason` 各个值代表什么，并行工具调用的编码方式，工具报错时如何恢复，以及怎么写工具描述才能让模型正确选择它。

**实践：** 用 `anthropic.messages.create` 加工具规范，在100行内做一个"从头开始"的 Agent。三个工具：通过 Tavily 或 Firecrawl 的 `web_search`、`read_file`、`write_file`，不用任何框架。拿一个研究任务跑一遍，把追踪的每一步都读一遍。

### 2. Claude Agent SDK：把它当标准参考 harness

Claude Agent SDK 就是为 Claude Code 提供动力的那个 harness。把它当参考来研究，第一天就开始用。

**参考资料：**

- *Claude Agent SDK 文档*（免费官方）——Python 和 TypeScript SDK、Hook、子 Agent、Skill 和 Task 工具
- *Claude Agent SDK Skill 参考*（免费官方）——SKILL.md 文件的工作方式、元数据前置、渐进加载
- *claude-code-best-practices*（Muhammad Usman GM，免费 GitHub）——浏览用，不要照单全抄，看看真实用户怎么用
- *claude-code-best-practice*（Shan Raisshan，免费 GitHub）——不同策划角度的配套合集
- *Evaluating Skills*（LangChain，免费）——LangChain 如何评估一个 Skill 是否真的有用，写完第一个 Skill 后看这篇

重点搞清楚：CLAUDE.md 系统提示模式，Skill 如何渐进加载，PreToolUse 和 PostToolUse Hook，用 Task 工具生成子 Agent，以及 SDK 如何处理权限提示。

**实践：** 用 `claude-agent-sdk` 重建上面那个 Agent。加一个带项目规范的 CLAUDE.md。加一个定义"研究摘要"输出格式的 Skill（带 SKILL.md 的文件夹）。加一个 PostToolUse Hook，自动格式化 Agent 写出的文件。用 Task 工具生成一个子 Agent 处理一个子任务。

### 3. 发布一个真实运行的小东西

教程不算数。你需要一个真正在跑、你会看它输出的东西。

**实践项目：** 做一个每日简报 Agent，读取本地 Markdown 笔记和几个 RSS 源，生成带引用的摘要简报，写入磁盘。用 launchd 或 systemd 定时运行。跑一周，看它怎么出错，修好它。

### 第1阶段里程碑

阶段结束时，你应该能：

- 不用框架，100行内写出一个完整的工具调用 Agent 循环
- 解释 `stop_reason` 各个值的含义，以及并行工具调用的工作方式
- 用 Claude Agent SDK 构建同一个 Agent，带 Skill、Hook 和子 Agent
- 用200字说清楚：harness 免费给了你哪些你在手搓版里自己写的东西

---

## 第2阶段：用正确的架构做一个真正的 Agent（3-4周）

**本阶段目标：** 在 LangGraph 1.0 + LangChain `create_agent` + Deep Agents 上构建一个多步、可持久化、有状态的 Agent。

这是你在生产中很可能用到的技术栈。它的核心概念（节点+边的状态机、中间件、检查点器）到哪儿都能用。

为什么选这个栈，而不是 Pydantic AI、OpenAI Agents SDK 或 CrewAI：

- LangGraph 是 Alice Labs 和 Channel.tel"哪个东西真正在生产跑"排名中唯一同时具备：持久执行、检查点、人在回路、通过 LangSmith 的一流可观测性和中间件的框架
- `create_agent`（LangChain 1.0，2025年10月）是建立在 LangGraph 运行时上的新默认 Agent 工厂，`create_react_agent` 已弃用
- Deep Agents（LangChain，2025年8月发布；2026年4月 v0.5 alpha）是其上的完整 harness：规划、虚拟文件系统、子 Agent、摘要、Skill——是最接近 Claude Code harness 的开源类比，且不绑定特定模型

### 1. LangGraph 运行时

节点和边构成的状态图，加上让你可以恢复、回退、分叉的检查点器。

**参考资料：**

- *LangGraph 文档*（免费官方）——运行时参考文档，从概念页开始，再看快速入门
- *Doubling down on Deep Agents*（LangChain，免费）——把 harness、框架、运行时三者的区别说得很清楚
- *Context Management for Deep Agents*（LangChain，免费）——20K token 工具响应卸载模式和85%上下文窗口压缩触发机制
- *On Agent Frameworks and Agent Observability*（LangChain，免费）——LangSmith 为何支持 OTEL 且不绑定 LangChain，即使你后续换平台也值得读
- *Deep Agents v0.5*（LangChain，免费）——2026年4月发布说明：异步（非阻塞）子 Agent、扩展的多模态文件系统支持、异步 TODO。锁定 deepagents 版本前先读这篇

重点搞清楚：状态模式、节点、边、条件边、PostgresSaver 检查点器、时间旅行调试、人在回路中断，以及中间件如何组合使用。

### 2. 中间件：定制 Agent 而不用 Fork

中间件是你在不 fork 代码的情况下定制打包好的 Agent 的方式。

**参考资料：**

- *How Middleware Lets You Customize Your Agent Harness*（LangChain，2026年3月26日，免费）——`before_agent`、`wrap_model_call`、`before_tools`、`after_tools` 这四个 Hook，必读
- *Introducing ambient agents*（LangChain，免费）——后台 Agent 的 UX 模式：通知、询问、审查

重点搞清楚：每个 Hook 在 Agent 生命周期的哪个位置触发，SummarizationMiddleware 和 FilesystemMiddleware 如何组合，30行内怎么写一个自定义中间件，以及什么时候该用中间件、什么时候该加新节点。

### 3. 工具、MCP 和代码执行模式

"把所有 MCP 工具全塞进上下文"这种用法是错的。正确的做法是：代码执行 + MCP。

**参考资料：**

- *Code execution with MCP*（Anthropic，2025年11月，免费官方）——150K → 2K token 的压缩，接任何 MCP 服务器前先读这篇
- *Introducing advanced tool use*（Anthropic，免费官方）——`defer_loading: true` 把工具 token 减少了85%，Opus 4.5 MCP eval 从79.5%升到88.1%
- *Scaling Managed Agents*（Anthropic，免费官方）——Session、harness 和沙箱的分层，即使你不用 Managed Agents 也值得读
- *Composio 文档*（免费层）——200+ SaaS 集成，内置 MCP 网关，凭证在代理层处理，不会进入模型上下文
- *Arcade 文档*（免费层）——需要细粒度的每用户独立身份（而不是服务级别认证）时选这个

重点搞清楚：`defer_loading`，代码执行作为工具调用面，为什么把 JSON 经模型来回传很贵，以及 Composio 或 Arcade 如何在不把凭证暴露给模型的情况下处理 SaaS 认证。

### 4. 内存选型：不一定要向量数据库

**参考资料：**

- *Letta MemFS benchmark on LoCoMo*（免费）——2026年4月结果：GPT-4o-mini 上基于文件系统的内存在 LoCoMo 上达到74%，超过专用内存工具
- *Mem0 文档*（免费）——用户维度的知识内存，跨会话存用户信息时选这个

重点搞清楚：三个内存层（通过 PostgresSaver 的线程级、通过 Mem0/Zep 的用户级、通过 Letta 的自管理级），为什么文件系统是正确的默认选择，以及在实际测出召回问题之前不要搭向量库。

**实践项目：构建一个"研究分析师" Deep Agent**

- 输入：一个研究问题
- 主 Agent 规划，将 TODO 列表写入虚拟文件系统，并行生成3个搜索子 Agent，每个有独立上下文
- 子 Agent 调用 Tavily 或 Firecrawl，把结果写入文件，向父 Agent 返回简短摘要——原始搜索结果不进父 Agent 上下文
- 一个引用验证子 Agent，负责用检索到的来源核实结论
- 一个写作 Agent，生成带内联引用的最终 Markdown 报告
- 所有状态通过 PostgresSaver 持久化，进程中途终止后可以从中断处恢复
- 人在回路中断：token 消耗超过1美元前必须请求用户确认
- 用一个 `make demo` 命令跑通完整流程
- README 要说清楚：用了哪个中间件、为什么，哪些子 Agent 有独立上下文，上下文压缩策略是什么，进程被杀死时持久化方案是什么
- 一并提交一次完整运行的 LangSmith 追踪 URL

### 第2阶段里程碑

阶段结束时，你应该能：

- 做一个有 PostgresSaver 持久化和人在回路中断的多步 LangGraph Agent
- 把 Deep Agents 中间件（规划、文件系统、子 Agent、摘要）当打包好的 harness 用
- 生成隔离上下文的子 Agent，并把压缩摘要返回给父 Agent
- 说清楚上下文压缩策略，以及进程被杀死时的持久化方案
- 提交一个显示完整多步轨迹的 LangSmith 追踪 URL

---

## 第3阶段：自己搭一遍 Harness 层（3-4周）

**本阶段目标：** 停止使用打包好的 harness，自己搭一个轻量版。在你动手搭过一次之前，你无法在生产中做出正确的 harness 权衡。

这是整个路线图里投入产出比最高的阶段。

### 1. "Harness"拆开来是什么

综合 Deep Agents 中间件清单、Claude Agent SDK 架构和 Vivek Trivedy 的 harness 工程文章，一个 harness 包含：

- **循环控制** ——驱动"模型→工具→模型"的 while 循环
- **工具调度** ——注册、Schema 验证、并行调用、错误恢复、重试
- **上下文管理** ——系统提示组装，在窗口占85-95%时压缩消息历史，在约20K token 时卸载工具响应，提示缓存
- **持久化** ——每个节点后检查点，保证可恢复、可回退、可分叉
- **子 Agent 编排** ——生成隔离上下文的子进程，把压缩摘要路由回来
- **Skill 与渐进式披露** ——只在相关时加载能力
- **Hook** ——PreToolUse、PostToolUse、PreCompact、Stop、SessionStart（以 Claude Code 的列表为规范）
- **可观测性** ——每次模型调用、工具调用、子 Agent 调用的 OTEL span，带 token 计数和延迟
- **沙箱** ——代码执行和 MCP 工具调用在模型没有直接凭证的容器里跑
- **认证与秘密代理** ——凭证不进模型上下文（Anthropic Managed Agents 模式）

**参考资料：**

- *The Anatomy of an Agent Harness*（LangChain，免费）——公开文献中对 harness 组件最清晰的拆解，本阶段的参考文本，写任何 harness 代码前先读
- *Improving Deep Agents with harness engineering*（Vivek Trivedy，LangChain，2026年2月17日，免费）——模型固定不动（GPT-5.2-codex），只改 harness，Terminal-Bench 2.0 从第30名到第5名。方法都在文章里
- *Better Harness: A Recipe for Harness Hill-Climbing with Evals*（Vivek Trivedy，LangChain，2026年4月29日，免费）——直接续篇：用自我验证和追踪来自主改进 harness。读完2月17日那篇立刻接着读这篇
- *Inside the Claude Agents SDK*（ML6，免费）——CPU/RAM/OS/App 类比和78% vs 42%对比数字
- *everything-claude-code*（Cerebral Valley × Anthropic 黑客马拉松获奖项目，免费 GitHub）——给你灵感：在哪里停止加功能
- *deepagents 源码*（免费 GitHub）——和你自己的 harness 对照着读，中间件文件是 harness 模式的核心

重点搞清楚：哪些组件值得自己写、哪些直接引入，以及功能优先级顺序：先做循环和工具调度，再做子 Agent，再做持久化，再做可观测性。

### 2. 持久执行：作为独立模块插入

**参考资料：**

- *Inngest 文档*（免费）——持久步骤和检查点在2025年12月正式发布，是 Python harness 加持久化的最简路径
- *Temporal Python SDK*（免费）——OpenAI Agents SDK 和 Temporal 的集成在2026年3月发布，把每个工具调用当一个持久步骤

重点搞清楚：每步的幂等键，重试策略，进程中止时飞行中的工具调用会怎样，以及 harness 检查点边界应该划在哪里（每个节点，而不是每个 token）。

**实践项目：用约1500行 Python 写一个迷你 harness**

- 一个包装 `anthropic.messages.create` 或 LiteLLM（保持模型无关性）的循环
- 基于 Python 装饰器（`@tool`）的工具注册，自动生成 JSON Schema
- CLAUDE.md 风格的系统提示加载器，读取 `./harness/rules/*.md`，支持路径通配符匹配
- SKILL.md 渐进式披露加载器（目标：每个 Skill 的上下文元数据不超过50个 token）
- 带隔离上下文的子 Agent 生成原语，向父 Agent 返回摘要字符串
- 文件系统卸载：工具输出超过20K token 时写入 `./workspace/<id>.txt`，上下文里替换成路径 + 10行预览
- 85%上下文占用时自动压缩：对最近10轮以前的消息做摘要
- 可插拔 Hook 系统（`pre_tool`、`post_tool`、`stop`）
- 通过 `opentelemetry-sdk` 的 OTEL 追踪，导出到 LangSmith 或 Phoenix（两者都支持 OTEL）
- 持久恢复：每步后把消息历史和状态写入 SQLite，按 run ID 重新加载
- 可选：把整体包进 Inngest 或 Temporal，让每个工具调用成为持久步骤

### 第3阶段里程碑

阶段结束时，你应该能：

- 列出现代 harness 的十个组件，说清楚每个在什么时候值得做
- 写出一个1500行的 Python harness，包含循环、工具调度、上下文压缩、子 Agent、Hook 和 OTEL 追踪
- 通过 Inngest 或 Temporal 接入持久执行，让进程中止变得可恢复
- 写一份1000字的事后复盘，对比你的迷你 harness 与 Claude Agent SDK 和 Deep Agents：做对了什么、削减了什么、下次会怎么做

复盘才是真正的交付物，代码只是证明你做过。

---

## 第4阶段：搭起 Eval 和回归体系（3-4周）

**本阶段目标：** 让你的 Agent 可以被测量。没有这个，每一次"改进"都只是感觉。

大多数工程师在这里卡住。他们能做出不错的 Agent，但判断不了下一个改动是在变好还是变差。

### 1. 只选一个可观测性平台

不要同时跑两个。五个真正的选择：

- **LangSmith** ——在 LangGraph 或 LangChain 生态里就选这个。原生追踪，2026年3月新增了沙箱、Polly 调试助手、Skill 和 Fleet（Agent 身份/共享）
- **Braintrust** ——要做框架无关、能阻止 PR 合并的 CI 质量门控就选这个。2026年2月完成8000万美元B轮，无限用户固定249美元/月，对比 LangSmith 的39美元/席位
- **Arize Phoenix**（开源）+ **Arize AX**（托管）——要原生 OTEL、漂移检测和清晰的从开源到托管迁移路径就选这个
- **W&B Weave** ——已经在用 Weights & Biases 做 ML 就选这个，现在有完整 Agent 追踪视图、MCP 自动日志和即将到来的 A2A 追踪
- **Inspect（英国 AISI）** ——要基准级别的 eval 精度就选这个。GAIA、SWE-bench、Cybench、BFCL 都打包成了 `inspect_evals`，Anthropic、DeepMind 和 Grok 内部都在用

**参考资料：**

- *LangSmith 文档*（免费层，官方）——生产追踪、在线 eval、实验和新的 Polly 调试助手
- *Inspect AI 注解笔记*（Hamel Husain，免费）——Hamel 的笔记是我最依赖的从业者写作，安装 Inspect 前先读
- *Inspect 文档*（免费官方）——框架参考
- *inspect_evals*（免费 GitHub）——200+ 标准 eval，Python 包，GAIA、SWE-bench、Cybench、BFCL
- *Braintrust 文档*（免费层）——框架无关实验、CI 门控和黄金测试集
- *Agent Evaluation Readiness Checklist*（LangChain，免费）——17分钟实操清单：错误分析、数据集构建、评分器设计、离线和在线 eval、生产就绪性，打印出来贴在显示器旁边
- *Quantifying infrastructure noise in agentic coding evals*（Anthropic，2026年2月5日，免费官方）——不稳定的沙箱和网络抖动单独就能让 eval 分数波动好几个点，在信任任何 Agent 基准数字之前先读这篇

重点搞清楚：追踪采样策略，在线 vs 离线 eval，指标和护栏的区别，以及为什么 CI 门控是让 eval 从仪表板装饰变成开发工具的关键。

### 2. 你必须实现的四种 Eval 类型

来自 Anthropic 的《Demystifying evals for AI agents》：

1. **单轮 eval：** 给这个输入，输出对不对？最便宜，尽可能用确定性评分器，持续跑
2. **轨迹 eval：** Agent 是否用了正确的参数、按正确的顺序调用了工具？覆盖单步、完整轮次和多轮三种变体
3. **LLM 作评判者：** 用于开放性输出（研究报告、代码审查）。每周对照人工评分样本校准。Anthropic 研究 Agent 的评分标准是0到1分，覆盖：事实准确性、引用质量、完整性、来源质量、工具使用效率
4. **最终状态 eval：** 用于有状态 Agent（写数据库、改文件）。把环境最终状态和标准答案比对，这是 τ-bench 的做法

**参考资料：**

- *Demystifying evals for AI agents*（Anthropic，免费官方）——这个话题上 Anthropic 最好的入门文章
- *Evaluating Deep Agents: Our Learnings*（LangChain，免费）——单步、完整轮次、多轮轨迹 eval 模式，从业者指南
- *How we build evals for Deep Agents*（LangChain，免费）——配套文章：怎么取数据、设计指标、跑范围合理的 eval，配合上篇一起读
- *Eval awareness in Claude Opus 4.6's BrowseComp performance*（Anthropic，2026年3月6日，免费官方）——模型可以感知到自己在被评估时表现不同，设计 eval 前读这篇，别把偏差设计进去
- *Designing AI-resistant technical evaluations*（Anthropic，2026年1月21日，免费官方）——怎么设计不被你要评分的模型"套路"的 eval，自己搭基准测试时必读
- *τ²-bench 仓库*（免费 GitHub）——带政策合规的多轮客服 eval
- *Establishing Best Practices for Building Rigorous Agentic Benchmarks*（arXiv，免费）——自己设计 eval 前先读这篇：SWE-bench、KernelBench、WebArena 都高估了5-33%

重点搞清楚：能用确定性评分器的地方怎么写，怎么对照人工评分校准 LLM 评判者，什么时候 pass^k 比 pass@1 更重要，以及怎么识别和丢弃被污染的基准。

**实践项目：围绕第2阶段的研究 Agent 建立回归体系**

- 构建一个30-50题的手工评分黄金测试集，覆盖三个难度级别（1/2/3级，GAIA 风格）
- 能确定性评分的（事实性问题）就用精确匹配，开放性问题用 5个维度评分标准的 LLM 评判者
- 做轨迹 eval：Agent 是否做了规划、生成了2个以上子 Agent、引用了来源、在预算内完成？
- 接入 GitHub Actions：每个 PR 跑完整 eval 套件，黄金集通过率下降3个百分点或任何 pass^4 指标下降就阻止合并
- 加生产采样：1%的线上追踪每晚自动由 LLM 评判者打分，漂移时告警
- 用 Inspect 跑至少一个公开基准：GAIA Level 1 或 τ²-bench retail，和公开排行榜比较
- 提交一个 `make eval` 命令，输出三个产物：CI 通过/失败摘要、LangSmith 实验 URL、带一个规范基准分数的 Inspect 日志文件

### 第4阶段里程碑

阶段结束时，你应该能：

- 选定一个可观测性平台，并从架构层面说清楚选它的理由
- 实现全部四种 eval 类型：单轮、轨迹、LLM 作评判者、最终状态
- 维护一个从生产失败中生长的黄金测试集，而不是用合成数据
- eval 分数回归时在 CI 中拦住 PR
- 提交一个 `make eval` 命令，输出 CI 通过/失败摘要、LangSmith 实验 URL 和带规范基准分数的 Inspect 日志
- 写下你在自己 Agent 里找到的失败模式——那份文档才是真正的产出

---

## 第5阶段：生产加固（持续进行）

**本阶段目标：** 让你构建的一切，能扛住真实用户、真实成本和真实故障。

这不是一个你能"完成"的阶段，它一直在持续。

### 1. 成本纪律

- 积极用提示缓存。Anthropic 的缓存在重复前缀上能省下90%。把 CLAUDE.md、系统提示和工具定义都缓存起来
- 按难度路由：简单轮次用 Haiku 4.5 或 Sonnet 4.6，规划和难推理用 Opus 4.7
- "advisor tool" beta（Anthropic，2026年3月）：在生成过程中把执行者和高智能顾问配对
- 注意 Opus 4.7 的分词器：标价和4.6一样，但同样的文本计费 token 可能多1到1.35倍，迁移后重新测每任务成本
- 非实时任务用批处理 API，便宜50%
- 多 Agent（Anthropic 风格研究型）：预计 token 消耗是单 Agent 对话的约15倍，只在答案价值足够高时才开多 Agent

**参考资料：**

- *Open Models have crossed a threshold*（LangChain，免费）——GLM-5 和 MiniMax M2.7 在核心 Agent 任务上（文件操作、工具使用、指令遵循）已追平闭源前沿模型，锁定模型选型和路由策略前先读这篇

重点搞清楚：提示缓存边界，模型路由规则，批处理 vs 实时的决策，以及你要监控的硬性每任务成本上限。

### 2. 延迟优化

- 并行工具调用。Anthropic 研究系统的提示里白纸黑字写着"生成多个子 Agent 时必须使用并行工具调用"，你自己的 Agent 也一样
- 通过 LangGraph 的 `stream_mode="updates"` 把部分输出流式传给 UI
- 子 Agent 扇出是最大的延迟杠杆：一个60步顺序 Agent 变成"一个10步主 Agent + 5个并行10步子 Agent"

重点搞清楚：并行在哪里是安全的，流式输出在哪里改变用户体验，以及扇出和成本的关系。

### 3. 安全和沙箱

- 所有代码执行放沙箱：Modal、E2B、Daytona 或 LangSmith Sandboxes（2026年3月私人预览），绝不在主进程里 `exec()` 模型输出
- 凭证在模型上下文外代理（Anthropic Managed Agents 模式；SaaS 认证用 Composio 处理）
- 护栏 Hook：PreToolUse Hook 拦截破坏性 Bash 命令、正则过滤敏感信息、验证文件写入路径
- 不可逆操作加人在回路中断（LangGraph 的 `interrupt()` + HumanInTheLoopMiddleware，Claude Agent SDK 的权限提示）

**参考资料：**

- *Modal 文档*（免费层）——Python 代码执行的默认沙箱
- *E2B 文档*（免费层）——专为 AI Agent 设计的代码执行沙箱
- *Beyond permission prompts: making Claude Code more secure and autonomous*（Anthropic，2025年10月20日，免费官方）——沙箱基础文章：Claude Code 如何对安全操作不再询问权限，同时控制住不安全的操作，你的 harness 应该复制这个模式
- *Claude Code auto mode: a safer way to skip permissions*（Anthropic，2026年3月25日，免费官方）——续篇：Agent 无人值守时会出现哪些变化，在生产里关闭任何"跳过确认"前把这两篇都读完

重点搞清楚：哪些操作可逆、哪些需要人工审批，以及如何确保模型永远看不到它使用的那个凭证。

### 4. 监控和漂移检测

- 低规模时100%追踪采样；高规模时降到1-10%，对错误做分层采样
- 监控告警项：每次请求的 token 成本、工具调用失败率、LLM 评判者平均分（每晚）、p95 延迟、eval 回归
- 每次模型升级后重新跑基准
- Anthropic 工程博客警告过："harness 对模型目前做不到的事情做了假设，随着模型变强，这些假设会过时"（Sonnet 4.5 → Opus 4.5 的"上下文焦虑"案例）

重点搞清楚：什么值得告警 vs 什么只需记录，如何检测提示缓存失效，以及当模型能力超过 harness 设计时如何发现 harness 僵化。

### 5. 韧性

- 对任何运行超过60秒的 Agent，持久执行（Inngest、Temporal 或 LangGraph PostgresSaver）是底线
- 每个节点后检查点，保证可回退可分叉。Pydantic Deep Agents 和 LangGraph 都支持，Claude Agent SDK 的 Session 日志是等效物

**参考资料：**

- *How My Agents Self-Heal in Production*（LangChain，免费）——一个在每次部署后自动检测回归、定位原因、开修复 PR（无需人工介入直到 review）的工作管道，把这个模式偷过来用

重点搞清楚：哪些故障可以自动恢复，哪些需要人工介入，以及如何在生产流量来临前就测好恢复路径。

### 第5阶段里程碑

这个阶段没有终点。但你应该有：

- 提示缓存接入系统提示、CLAUDE.md 和工具定义
- 带硬性每任务成本上限和告警的模型路由层
- 所有代码执行的沙箱，以及把秘密隔离在上下文外的凭证代理
- 拦截破坏性操作、强制不可逆操作人工审批的 Hook
- 追踪采样、漂移告警，以及每次模型升级后的重新基准仪式
- 让进程中止变成小事的持久执行层

---

## 推荐

直接可以行动的建议。

**如果只学一个框架：** LangGraph 1.0 + Deep Agents。它是最通用的，运行时体系是目前最成熟的（PostgresSaver、时间旅行调试、持久执行、通过 LangSmith 的 OTEL 可观测性），不绑定特定模型，而且它的抽象（状态图+中间件）本身就是可迁移的心智模型。就这个，没有其他选择。

**如果只学一个参考 harness：** Claude Agent SDK + Claude Code。它就是参考实现。CLAUDE.md、Skill、子 Agent、Hook、Plan 模式、文件系统作内存——2026年其他所有 harness 都在向这些原语靠拢。每天用 Claude Code，读它的文档，研究开源 harness 合集。

**如果只读一篇上下文工程的文章：** Anthropic 的《Effective context engineering for AI agents》（2025年9月）。如果读两篇：加上 LangChain 的《Context Engineering for Agents》，补上 Write/Select/Compress/Isolate 框架。

**如果只学一个可观测性工具：** 待在 LangGraph 就选 LangSmith；要框架无关的 CI 门控就选 Braintrust；要基准级别的严格性就选 Inspect（你最终会需要的）。

### 2026年直接跳过的东西

- AutoGen v0.4（合并进了 Microsoft Agent Framework，社区分支是 AG2，两个都不是强推选项）
- OpenAI Swarm（官方已宣布淘汰，OpenAI 自己的 README 明确说"不适合生产"）
- Assistants API（2026年中停用）
- 在实际测出召回问题之前自己搭向量库
- "无代码"Agent 平台，除非你在做一次性项目

### 有特定理由才用的东西

- **CrewAI** ——想法到原型最快，生产环境脆弱。用于黑客马拉松和演示
- **OpenAI Agents SDK** ——绑在 OpenAI 生态就用这个，2026年4月更新加了沙箱和 harness，但还是绑定 OpenAI 模型
- **Pydantic AI / Pydantic Deep Agents** ——严格类型的 FastAPI 团队可以选
- **Mastra** ——团队是 TypeScript 且不能用 Python 时才选。2026年1月 v1.0，YC W25，22k+ 星，Gatsby 团队出品
- **Smolagents** ——学习代码 Agent 模式最好用的工具（1000行代码库可以随便改），生产能力弱
- **DSPy 3.0 + GEPA** ——有了可度量的指标、想用程序自动优化 Prompt 和 Agent 拓扑时用。GEPA 用35倍更少的 rollout 超过 RL 6%（ICLR 2026 口头报告）
- **Letta / MemGPT** ——跨 Session 需要操作系统级别的 Agent 自管理内存时用，否则文件系统 + Mem0 更简单

### 基准收藏（2026年5月数据）

- **SWE-bench Verified：** Claude Opus 4.7 ≈ 87.6%，GPT-5.5 ≈ 88.7%，Gemini 3.1 Pro ≈ 78.8%
- **Terminal-Bench 2.0：** GPT-5.5 82.7%，Opus 4.7 ~70%，Gemini 3.1 Pro ~68%
- **τ-bench：** Claude Mythos Preview 89.2% 领先
- **BrowseComp：** GPT-5.5 90.1%，Gemini 3.1 Pro 85.9%，Opus 4.7 79.3%（4.6 的83.7%有所退步，网络研究任务路由到 GPT-5.5）
- **GAIA / Princeton HAL：** Sonnet 4.5 以74.6%领先

### 对有技术基础的 Agent 新手的时间里程碑

- **第2周：** 第0阶段完成，能用大白话讲清楚什么是 harness
- **第5周：** 第1阶段完成，带 Skill、Hook 和子 Agent 的 Claude Agent SDK Agent 上线
- **第9周：** 第2阶段完成，LangGraph 研究分析师 Agent 跑通，带 PostgresSaver 持久化和 LangSmith 追踪
- **第13周：** 第3阶段完成，1500行迷你 harness 写完记录好，能力和精简版 Claude Agent SDK 相当
- **第17周：** 第4阶段完成，黄金测试集建好，CI 门控接好，跑过一次 Inspect 公开基准
- **永久：** 第5阶段

兼职（每周10-15小时）的话，时间乘以约2.5倍。

两个调整计划的信号：第1阶段3周内跑不通，说明工具设计有问题（回去重读《Writing tools for agents》）。第2阶段超过5周，说明你也在试图搭 harness——降到 Deep Agents，别跟它对抗。

---

## 注意事项

提前看到这些，能帮你少踩坑。

### 基准是移动靶，部分已被套路

SWE-bench Verified 分数两年内从1.96%涨到80%+。τ-bench 的 pass^k 一致性指标，正是因为单次准确率不再有意义才加进来的。任何"X 模型得了Y%"的声明，都要理解为：模型 + harness + 脚手架 + 重试预算 + 系统提示，不是模型单独的成绩。

### 多 Agent 对大多数场景被过度炒作

Anthropic 报告的90.2%提升，针对的是广度优先研究这个特定场景。对于编码和紧耦合任务，多 Agent 往往比单 Agent 更差，还多烧15倍 token。默认用单 Agent + 子 Agent 处理有边界的探索。只有任务能自然分解时，才动用完整的多 Agent 方案。

值得收藏的反例：Anthropic 的《Building a C compiler with a team of parallel Claudes》（2026年2月5日）展示了一个并行子 Agent 真正有效的编码任务。多 Agent 在代码上没死，只是需要对的分解方式。

### 2026年部分来源里的推测性内容

一些"AI 2027"预测（OpenBrain 450亿美元营收等）明确是虚构的，但会被当数据引用，忽略它们。发布周的评价文章是轶事，把它们当开发者情绪信号，而不是基准数据。

### 框架格局随时可能再变

LangChain 自己的定位18个月内换了两次（链→图→图上的 harness）。Pydantic AI、Mastra 或 Deep Agents 中任何一个在12个月内都可能更大。把赌注押在抽象上（循环、工具、上下文、子 Agent、持久化、追踪），而不是任何一个具体库，这些才是可以带走的东西。

### MCP 在生产环境的粗糙边缘是真实存在的

负载均衡器后的 HTTP 流式传输、多租户认证、限流、审计日志——这些都在2026年 MCP 路线图上，说明还没解决。为2026年底到来的下一代传输 SEP 做好准备，别深度耦合当前的 Session 模型。

### 模型行为在小版本间会变化

Opus 4.7 更严格的指令遵循和新分词器，意味着你的 Opus 4.6 Prompt 可能行为不同，同样文本的 token 成本高达35%。每次模型升级都重新跑一遍流量测试。

### 你的 Eval 套件会腐化

今天建的黄金测试集，几个月后就会随模型进步而饱和。计划每季度用生产故障（而不是合成数据）扩充10-20%。LLM 评判者的人工校准要一直跑下去。

### 路线图里的一些来源有商业立场

尽量依赖一手来源（Anthropic 工程博客、LangChain 博客、OpenAI 公告、arXiv）。那些排名风格的"2026年最佳"文章（Alice Labs、Channel.tel、GuruSup、Morph、Vstorm）是有用的三角验证，但各有商业动机。多个来源互相印证、且和一手工程来源一致时，把那个共识当可靠的。

---

## 结论

跟你说实话，不加糖。

这份路线图不会在17周内让你成为首席 AI 工程师。但它会让你成为一个能做出、发布、并让 Agent 系统在生产流量下真正跑起来的工程师。而这恰好是公司现在愿意付钱买的东西。

对能交付生产 Agent 的工程师的需求不会放缓。根据 LangChain 的智能体工程现状报告，57%的团队已经有了生产中的 Agent，其中89%有可观测性。质量是头号障碍（32%），这意味着整个行业的瓶颈不是会调 LLM API 的人，而是能做好 eval 和 harness 的工程师。

Anthropic 的数字说明了真正的机会在哪里：同一个模型，不同的 harness，**CORE 评分78% vs 42%**。那个差距，就是你的工作。

harness 工程这个转变，是当前软件招聘市场里最大的定价错误。公司还在挂"Prompt 工程师"职位。他们真正需要的，是能拿起一个前沿模型，把它变成一个可测量、可持续运行的生产系统的工程师。

我想让你从这一切中带走的是：

**从每个阶段选一个项目，做出来。** 不是读它，是做出来，搞坏它，修好它，部署它，然后把 LangSmith 追踪和基准分数放进 README。被雇用的是能展示追踪记录的工程师，不是能背出框架对比表的工程师。

**开始分享你学到的东西。** 写你的迷你 harness 复盘，发布你的测试集发现，把你的基准数字连同生成它的 harness 配置一起发出去。教别人是最快的学习方式，同时在建立你的声誉。最好的机会找到的是可见的工程师，不是投了500份简历的工程师。

**别等到"感觉准备好了"再开始。** 你永远不会感觉准备好。"我在读 LangChain 博客"和"我在发布一个有 PostgresSaver 持久化的 Deep Agent"之间的这段距离，是大多数工程师永远卡在里面的地方。

手上有一个跑起来的 Agent，就开始申请，开始公开构建，开始发布。哪怕它很小。市场不奖励完美，它奖励能让模型做出真实的东西、并且证明它没有退步的工程师。

17周，专注工作，足够改变一切。我相信每一个读到这里的人都能做到。

做，做出来，然后测量你做出来的。

---

*本文由作者根据2到3个月积累的内部笔记和手写记录写成，经 Minimax 2.7 编辑。作者在 Obsidian 上有一套内容生产管道，这些文章在管道中按他的写作风格，由他的手写和手打笔记生成。*
