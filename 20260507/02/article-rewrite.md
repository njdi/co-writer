# 2026年，怎么成为一个真正的 AI 工程师

**作者：** Avid ([@Av1dlive](https://x.com/Av1dlive))  
**日期：** 2026年5月7日  
**来源：** [How to Become an AI Engineer in 2026 (Builder's Roadmap)](https://x.com/Zephyr_hg/status/2052063154423898603)

先说一个让很多人感到意外的事实。

2026年，一个会搭 Agent 系统的工程师，一个周末能做出价值十亿的产品原型。不是说说而已，是真的在发生。

但有意思的地方在这里：让 Agent 系统变厉害的，不是模型本身。

Anthropic 做过一个测量。同样的 Opus 4.5，在 Claude Code 内部跑，CORE 评分78%；换到 Smolagents 里跑，42%。同一个模型，两套不同的运行框架，差了36个百分点。

这36个百分点，叫做 **harness engineering**——运行框架工程。这份路线图，讲的就是这件事。

> 如果你不想读7862字，直接把这个链接交给你的 Agent，让它给你生成个性化版本：➡️ https://raw.githubusercontent.com/codejunkie99/agent-roadmap-2026/main/AGENT.md

---

## 大多数工程师卡在哪里

有人去学 CrewAI，因为 Twitter 上的演示看起来很酷。有人追着每一个新框架跑，永远做不完一件真实的东西。还有人直接跳进多 Agent 系统，连什么是上下文管理、什么是工具设计都还没搞清楚。

结果都一样：刷了一堆框架，没有一个能上生产。

问题不是他们学的东西太少，而是学的方向不对。

你不需要学12个框架。你需要的是：能把 Agent 系统从零做到生产、能测量、能持续运行的那套完整能力。

这包括：

- 在 LangGraph 这样的编排运行时上构建 Agent
- 把 Claude Agent SDK 当参考运行框架来研究
- 用 Write、Select、Compress、Isolate 四个原语做好上下文工程
- 写出模型能正确调用的工具
- 为生产流量加上内存、持久化和沙箱
- 建立 eval、轨迹检查和 CI 回归门控
- 让 Agent 真正扛得住真实用户和真实成本

这份路线图分六个阶段，来自2025年底到2026年初的一手资料，超过7000字。它的价值在于：每个阶段都有具体项目、精选阅读清单和你真正需要的资源。

专注工作约**17周**，你就能做到独立负责一个生产 AI 功能。

这份路线图背后，是**60多小时**阅读工程博客、论文和一线工程师调查的积累。

---

## 2026年，一个 Agent 工程师在做什么

说到 AI Agent 工程师，很多人脑子里出现的画面是：有人把几个 CrewAI 角色拼在一起，然后宣布"搞定了"。

实际情况要务实得多。现代 Agent 工程师在前沿模型之上构建、配置和运营 Agent 系统。

这通常包括：

- 设计 Agent 循环和工具调度机制
- 用 Write、Select、Compress、Isolate 做上下文工程
- 写出模型能正确选择的工具
- 用隔离上下文窗口编排子 Agent
- 加上 Skill、内存、持久化和沙箱
- 接入 eval、追踪和 CI 门控，让"改进"变得可以度量

Anthropic 的多 Agent 研究系统，用的就是这套模式。在广度优先研究任务上，比单 Agent Opus 4 提升了 **90.2%**，代价是烧了约15倍的 token。

2026年，真正值得深入学的技术栈只有两个：**LangGraph 1.0 + Deep Agents** 和 **Claude Agent SDK**。其他的要么在退场，要么只是这两个在生产环境下的劣化版本。

上下文工程有四个核心原语，每个 Agent 构建者都要掌握：

- **Write** ——草稿本、内存文件，把信息写下来留给下一步用
- **Select** ——在需要时检索，而不是一开始就把所有东西塞进上下文
- **Compress** ——在上下文占用85-95%时做摘要，腾出空间
- **Isolate** ——让子 Agent 拥有独立的上下文窗口，互相隔离

---

## 免费资源：选一个，先跟起来

下面是一些持续输出高质量内容的免费资源。重点是：在第0阶段先选定一个博客、一份通讯、一个播客、一个社区，专注跟进。别一下子追40+个。等现有的不再给你带来惊喜，再加新的。

这份清单的意义是给你选择依据，不是让你全部完成的待办事项。

### 工程博客

- **Anthropic 工程博客**（免费，官方）——只读一个的话就选这个。上下文工程、运行框架设计、多 Agent 研究、eval，全是一手资料
- **LangChain 博客**（免费）——Lance Martin、Vivek Trivedy 和 Harrison Chase 的文章都值得读，运行框架规范在这里成型
- **OpenAI Cookbook**（免费，GitHub）——可运行的 Notebook，跟着敲代码，不要只看
- **Hamel Husain 的博客**（免费）——eval 领域最常被引用的文章作者，如果你做 eval，读两遍
- **Eugene Yan 的博客**（免费）——实战视角，"构建基于 LLM 的系统和产品的模式"是每个从业者都引用的文章
- **Lilian Weng 的博客**（免费）——关于 Agent、Prompt 工程、幻觉、对齐的长篇深度文章，综合写作最清晰的之一
- **Simon Willison 的博客**（免费）——在一线发布产品的工程师的每日笔记，适合拆穿炒作
- **Chip Huyen 的博客**（免费）——第5阶段前的必读，"为生产环境构建 LLM 应用"
- **Phil Schmid 的博客**（免费）——HuggingFace、Gemini、微调、部署的实战指南，总配代码
- **Cameron Wolfe 的 Deep (Learning) Focus**（免费）——一篇文章帮你跟上一个研究方向

### 免费课程

- **DeepLearning.AI 短期课程**（免费）——第0阶段完成两门：LangGraph 课程和 Andrew Ng 的"Agentic AI"课程
- **LangChain Academy：LangGraph 入门**（免费）——官方课程，第2阶段完成
- **Anthropic 交互式 Prompt 工程教程**（免费，GitHub）——九章 Notebook 对着 Claude API 做，建立 Prompt 直觉最快的方式
- **HuggingFace Agent 课程**（免费）——从头到尾覆盖 Agent、smolagents、MCP 和评估，有免费证书
- **HuggingFace LLM 课程**（免费）——tokenization、Transformer、微调的基础背景
- **FreeAcademy MCP 基础课程**（免费）——最快入门 MCP 的路径

### YouTube 频道

- **Andrej Karpathy**（免费）——2026年在 Sequoia AI Ascent 的演讲"Vibe Coding to Agentic Engineering"，目前解释 harness 工程为何重要最清晰的一次
- **AI Engineer**（免费）——AI Engineer Summit 和 World's Fair 的所有演讲，重点看 Hamel Husain、swyx、Anthropic 工程师
- **LangChain**（免费）——新功能通常最先以视频形式在这里出现
- **Anthropic**（免费）——多 Agent 研究演示、Claude Code 内部原理
- **Yannic Kilcher**（免费）——论文解析，省去啃 arXiv 的时间
- **Lex Fridman 播客**（免费）——和 Karpathy、Schulman、Amodei 等人的长篇对话

### 通讯

- **Latent Space（swyx & Alessio）**（免费）——只订一个就选这个，AI 工程师的技术通讯
- **The Batch（Andrew Ng）**（免费）——每周广谱覆盖
- **Import AI（Jack Clark）**（免费）——政策加研究摘要，战略视角
- **Ben's Bites**（免费）——五分钟每日资讯，快速扫
- **TLDR AI**（免费）——低噪音每日摘要

### 社区

- **LangChain Discord**（免费）——LangGraph 和 Deep Agents 核心团队在这里
- **HuggingFace Discord**（免费）——最大的开放权重和 ML 社区
- **r/LocalLLaMA**（免费）——开放权重模型新闻，通常比官方渠道快
- **AI Engineer World's Fair**（免费注册）——职位发布、招聘频道、工作组
- **Anthropic Discord**（免费）——Claude 开发者社区

### 开源项目

- **Anthropic Cookbook**（免费，GitHub）——每个工作流模式的参考实现，每个阶段结束后重读
- **OpenAI Cookbook**（免费，GitHub）——同类内容，OpenAI 视角
- **LangChain 的 deepagents**（免费，GitHub）——参考 harness，第3阶段重点看中间件文件
- **LangGraph 示例**（免费，GitHub）——可运行的 LangGraph 模式
- **inspect_evals**（免费，GitHub）——200+ 标准 eval 打包成 Python 包
- **awesome-agentic-engineering-resources**（免费，GitHub）——社区维护的资源索引

### 通勤播客

- **Latent Space**（免费）——和推动这个领域的人的长篇对话
- **Dwarkesh Podcast**（免费）——AI 战略和能力的长篇访谈
- **TWIML AI Podcast**（免费）——每周技术访谈
- **Practical AI**（免费）——工程导向，少炒作
- **The MAD Podcast（Matt Turck）**（免费）——谁在真正出货、谁在圈钱的好视角

---

## 第0阶段：先把基础想清楚（1-2周）

**这个阶段的目标：** 建立正确的心智模型。除了随手试验的脚本，先不要写任何 Agent 代码。

大多数人跳过这一步，直接扎进框架教程。然后代码一出问题，就不知道该往哪里看。别跳过。

### 搞清楚"工作流"和"Agent"的区别

在动手写任何框架之前，先搞清楚这件事：工作流和 Agent 根本上的区别是什么。

Anthropic 归纳了五种工作流模式：提示链、路由、并行化、编排者-工作者、评估者-优化者。

工作流和 Agent 的核心区别很简单：

- **工作流**：控制流是你写死的
- **Agent**：在循环内自己决定下一步干什么

搞清楚这个，能帮你避免一个很常见的错误：把本该是链式流程的东西，做成了 Agent。

**看什么：**

- *Building Effective Agents*（Anthropic，Erik Schluntz & Barry Zhang，2024年12月，免费官方）——五种工作流模式，这个领域人手必读，先读这篇
- *Anthropic Cookbook*（patterns/agents 文件夹，免费 GitHub）——跟着敲，别只看
- *Simon Willison 对 Building Effective Agents 的注解*（免费）——老工程师视角，帮你识别里面的炒作成分

### 上下文工程：Prompt 工程的接班人

2026年，"Prompt 工程"作为独立技能基本过时了。

取而代之的是**上下文工程**：在 Agent 循环的每一步，决定模型面前放什么 token。

这里有一个核心框架：Write、Select、Compress、Isolate。一旦你真正理解这四个原语，很多 Agent 设计问题就有了答案。

**看什么：**

- *Effective context engineering for AI agents*（Anthropic，2025年9月29日，免费官方）——读两遍
- *Context Engineering for Agents*（Lance Martin，LangChain，免费）——Write/Select/Compress/Isolate 框架，你需要的核心心智模型
- *How we built our multi-agent research system*（Anthropic，2025年6月，免费官方）——90.2% 的提升和15倍 token 的代价，都在这里

### 像理解操作系统一样理解 Harness

Harness 是什么？简单说：把模型包起来、控制它怎么运行的那一层。

有人用过 CPU、RAM、操作系统这个类比来解释它。模型是 CPU，上下文窗口是 RAM，harness 是操作系统。同一颗 CPU，在不同操作系统上跑，性能天差地别。

**看什么：**

- *Inside the Claude Agents SDK*（ML6，免费）——CPU/RAM/OS/App 类比，以及78% vs 42% 这两个数字
- *The Complete Guide to Harness Engineering*（ClaudeCodeLab，免费）——三级 harness 升级，带可运行代码
- *Building agents with the Claude Agent SDK*（Anthropic，免费官方）
- *Effective harnesses for long-running agents*（Anthropic，2025年11月26日，免费官方）
- *How to think about agent frameworks*（Harrison Chase，LangChain，免费）——选框架前必读

### 2026年行业是什么状态

几个值得记住的数字，来自 LangChain 对1340人的调研（2025年11-12月）：

- 57% 的团队 Agent 已上生产
- 89% 有可观测性
- 52% 有 eval
- 质量（32%）是头号障碍

**看什么：**

- *State of Agent Engineering*（LangChain，免费）
- *How to Build an Agent*（LangChain，免费）——"聪明实习生"框架，帮你想清楚 Agent 的边界
- *Continual learning for AI agents*（Harrison Chase，LangChain，免费）——在你想到微调之前先把这个框架搞清楚

**第0阶段的实践项目：** 手写一份2页文档，用自己的话定义：工作流 vs Agent、增强型LLM、四个上下文工程原语、编排者-工作者模式、harness/模型/框架的区别，以及你预计自己代码里会出现的前三个失败模式。

写不出来，就说明还没真正看进去。

### 第0阶段里程碑

阶段结束时，你应该能：

- 不用框架术语，解释清楚 Agent 是什么，跟工作流有什么区别
- 说出四个上下文工程原语，并给出每个的代码级示例
- 解释为什么2026年 harness 的贡献比模型本身更大
- 讲清楚编排者-工作者模式和15倍 token 代价
- 在架构层面选框架，而不是跟着感觉走

---

## 第1阶段：做出第一个简单的 Agent（2-3周）

**这个阶段的目标：** 把同一个使用工具的 Agent 做两遍。第一遍用 Anthropic 的原始 SDK 手搓，第二遍用 Claude Agent SDK。亲身感受两者的区别。

这是理解 harness 到底给你带来什么的成本最低的方式。

### 从头写 Agent 循环

循环本身不复杂。用消息和工具调用模型，解析出 `tool_use` 块，执行工具，追加 `tool_result`，重复，直到 `stop_reason` 等于 `end_turn`。

自己用100行写一遍，之后每个框架都能看懂。

**看什么：**

- *Tutorial: Build a tool-using agent*（Anthropic 文档，免费官方）——`tool_use`、`tool_result`、并行工具调用的参考
- *Writing tools for agents*（Anthropic，免费官方）——工具和参数的描述就是给 LLM 看的使用说明书
- *Equipping agents for the real world with Agent Skills*（Anthropic，免费官方）——渐进式披露模式

**实践：** 用 `anthropic.messages.create` 加工具规范，100行内做一个完整的 Agent。三个工具：`web_search`（通过 Tavily 或 Firecrawl）、`read_file`、`write_file`，不用任何框架。拿一个研究任务跑一遍，把追踪的每一步都读一遍。

### 把 Claude Agent SDK 当标准参考

Claude Agent SDK 就是为 Claude Code 提供动力的那个 harness。把它当参考研究，第一天就开始用。

**看什么：**

- *Claude Agent SDK 文档*（免费官方）——Python 和 TypeScript SDK、Hook、子 Agent、Skill 和 Task 工具
- *Claude Agent SDK Skill 参考*（免费官方）——SKILL.md 的工作方式、渐进加载
- *claude-code-best-practices*（Muhammad Usman GM，免费 GitHub）——浏览用，看看真实用户怎么用
- *Evaluating Skills*（LangChain，免费）——写完第一个 Skill 后看这篇

**实践：** 用 `claude-agent-sdk` 重建上面那个 Agent。加一个带项目规范的 CLAUDE.md。加一个定义"研究摘要"输出格式的 Skill。加一个 PostToolUse Hook，自动格式化 Agent 写出的文件。用 Task 工具生成一个子 Agent 处理子任务。

### 做一个真实运行的小东西

教程不算数。你需要一个真正在跑、你会看它输出的东西。

**实践项目：** 做一个每日简报 Agent，读取本地 Markdown 笔记和几个 RSS 源，生成带引用的摘要，写入磁盘。用 launchd 或 systemd 定时跑。跑一周，看它怎么出错，修好它。

### 第1阶段里程碑

阶段结束时，你应该能：

- 不用框架，100行内写出一个完整的工具调用 Agent 循环
- 解释 `stop_reason` 各个值的含义，以及并行工具调用的工作方式
- 用 Claude Agent SDK 构建同一个 Agent，带 Skill、Hook 和子 Agent
- 用200字说清楚：harness 免费给了你哪些你在手搓版里要自己写的东西

---

## 第2阶段：用正确的架构做一个真正的 Agent（3-4周）

**这个阶段的目标：** 在 LangGraph 1.0 + LangChain `create_agent` + Deep Agents 上构建一个多步、可持久化、有状态的 Agent。

这是你在生产中很可能用到的技术栈。它的核心概念——节点+边的状态机、中间件、检查点器——到哪儿都能用。

为什么选这个栈，而不是 Pydantic AI、OpenAI Agents SDK 或 CrewAI：

- LangGraph 是目前唯一同时具备持久执行、检查点、人在回路、一流可观测性和中间件的框架
- `create_agent`（LangChain 1.0，2025年10月）是新默认，`create_react_agent` 已弃用
- Deep Agents（LangChain，2025年8月发布）是其上完整的 harness：规划、虚拟文件系统、子 Agent、摘要、Skill，是最接近 Claude Code harness 的开源类比，且不绑定特定模型

### LangGraph 运行时

节点和边构成的状态图，加上让你可以恢复、回退、分叉的检查点器。

**看什么：**

- *LangGraph 文档*（免费官方）——从概念页开始，再看快速入门
- *Doubling down on Deep Agents*（LangChain，免费）——把 harness、框架、运行时三者的区别讲得很清楚
- *Context Management for Deep Agents*（LangChain，免费）——20K token 卸载模式和85%压缩触发机制
- *Deep Agents v0.5*（LangChain，免费）——2026年4月发布说明，锁版本前先读

### 中间件：不 Fork 代码也能定制 Agent

中间件是你在不动原有代码的情况下修改 Agent 行为的方式。

**看什么：**

- *How Middleware Lets You Customize Your Agent Harness*（LangChain，2026年3月26日，免费）——四个核心 Hook：`before_agent`、`wrap_model_call`、`before_tools`、`after_tools`，必读
- *Introducing ambient agents*（LangChain，免费）——后台 Agent 的 UX 模式

### 工具、MCP 和代码执行

"把所有 MCP 工具全塞进上下文"这种用法是错的。正确的做法是：代码执行 + MCP。

**看什么：**

- *Code execution with MCP*（Anthropic，2025年11月，免费官方）——150K → 2K token 的压缩，接 MCP 前必读
- *Introducing advanced tool use*（Anthropic，免费官方）——`defer_loading: true`，工具 token 减少85%
- *Scaling Managed Agents*（Anthropic，免费官方）——即使不用 Managed Agents 也值得读
- *Composio 文档*（免费层）——200+ SaaS 集成，凭证在代理层处理
- *Arcade 文档*（免费层）——需要每用户独立身份时用

### 内存选型：不一定要向量数据库

**看什么：**

- *Letta MemFS benchmark on LoCoMo*（免费）——文件系统内存在 LoCoMo 上达到74%，超过专用内存工具
- *Mem0 文档*（免费）——跨 Session 存用户信息时选这个

在实际测出召回问题之前，别急着搭向量库。文件系统是正确的默认选择。

**实践项目：构建一个"研究分析师" Deep Agent**

- 输入一个研究问题
- 主 Agent 规划，把 TODO 写入虚拟文件系统，并行生成3个搜索子 Agent，每个有独立上下文
- 子 Agent 调用 Tavily 或 Firecrawl，结果写入文件，向父 Agent 返回简短摘要——原始搜索结果不进父 Agent 上下文
- 引用验证子 Agent 负责核实结论
- 写作 Agent 生成带内联引用的最终 Markdown 报告
- 所有状态通过 PostgresSaver 持久化，进程中途终止后可以从中断处恢复
- token 消耗超过1美元前必须请求用户确认
- 用一个 `make demo` 命令跑通完整流程
- README 说清楚：用了哪个中间件、为什么，哪些子 Agent 有独立上下文，上下文压缩策略，进程被杀死时的持久化方案
- 提交一次完整运行的 LangSmith 追踪 URL

### 第2阶段里程碑

阶段结束时，你应该能：

- 做一个有 PostgresSaver 持久化和人在回路中断的多步 LangGraph Agent
- 把 Deep Agents 中间件当打包好的 harness 用
- 生成隔离上下文的子 Agent，把压缩摘要返回给父 Agent
- 说清楚上下文压缩策略和进程被杀死时的持久化方案
- 提交一个显示完整多步轨迹的 LangSmith 追踪 URL

---

## 第3阶段：自己搭一遍 Harness（3-4周）

**这个阶段的目标：** 停止用打包好的 harness，自己搭一个轻量版。在你动手搭过一次之前，无法在生产中做出正确的 harness 权衡。

这是整个路线图里投入产出比最高的阶段。

### 一个 Harness 拆开来是什么

综合 Deep Agents 中间件清单、Claude Agent SDK 架构和相关工程文章，一个完整的 harness 包含十个部分：

- **循环控制** ——驱动"模型→工具→模型"的 while 循环
- **工具调度** ——注册、Schema 验证、并行调用、错误恢复、重试
- **上下文管理** ——系统提示组装，在窗口占85-95%时压缩历史，在约20K token 时卸载工具响应，提示缓存
- **持久化** ——每个节点后检查点，保证可恢复、可回退、可分叉
- **子 Agent 编排** ——生成隔离上下文的子进程，把压缩摘要路由回来
- **Skill 与渐进式披露** ——只在相关时加载能力
- **Hook** ——PreToolUse、PostToolUse、PreCompact、Stop、SessionStart
- **可观测性** ——每次模型调用、工具调用、子 Agent 调用的 OTEL span
- **沙箱** ——代码执行和 MCP 工具调用在模型没有直接凭证的容器里跑
- **认证与秘密代理** ——凭证不进模型上下文

功能优先级顺序：先做循环和工具调度，再做子 Agent，再做持久化，最后做可观测性。

**看什么：**

- *The Anatomy of an Agent Harness*（LangChain，免费）——最清晰的 harness 组件拆解，写代码前先读
- *Improving Deep Agents with harness engineering*（Vivek Trivedy，LangChain，2026年2月17日，免费）——模型不动，只改 harness，Terminal-Bench 2.0 从第30名到第5名
- *Better Harness: A Recipe for Harness Hill-Climbing with Evals*（Vivek Trivedy，LangChain，2026年4月29日，免费）——读完上篇接着读这篇
- *everything-claude-code*（Cerebral Valley × Anthropic 黑客马拉松获奖，免费 GitHub）——在哪里停止加功能
- *deepagents 源码*（免费 GitHub）——和你自己的 harness 对照着读

### 持久执行：作为独立模块插入

**看什么：**

- *Inngest 文档*（免费）——2025年12月 GA，Python harness 加持久化的最简路径
- *Temporal Python SDK*（免费）——把每个工具调用当一个持久步骤

**实践项目：用约1500行 Python 写一个迷你 harness**

- 包装 `anthropic.messages.create` 或 LiteLLM 的循环
- 基于 `@tool` 装饰器的工具注册，自动生成 JSON Schema
- CLAUDE.md 风格的系统提示加载器，读 `./harness/rules/*.md`，支持通配符
- SKILL.md 渐进式披露加载器，每个 Skill 元数据不超过50个 token
- 带隔离上下文的子 Agent 生成原语
- 文件系统卸载：工具输出超过20K token 时写入文件，上下文里替换成路径+10行预览
- 85%上下文占用时自动压缩：对最近10轮以前的消息做摘要
- 可插拔 Hook 系统（`pre_tool`、`post_tool`、`stop`）
- 通过 `opentelemetry-sdk` 的 OTEL 追踪，导出到 LangSmith 或 Phoenix
- 持久恢复：每步后把消息历史写入 SQLite，按 run ID 重新加载
- 可选：接入 Inngest 或 Temporal，让每个工具调用成为持久步骤

### 第3阶段里程碑

阶段结束时，你应该能：

- 列出现代 harness 的十个组件，说清楚每个在什么时候值得做
- 写出一个1500行的 Python harness，包含循环、工具调度、上下文压缩、子 Agent、Hook 和 OTEL 追踪
- 通过 Inngest 或 Temporal 接入持久执行
- 写一份1000字的复盘，对比你的迷你 harness 与 Claude Agent SDK 和 Deep Agents

复盘才是真正的交付物，代码只是证明你做过。

---

## 第4阶段：搭起 Eval 和回归体系（3-4周）

**这个阶段的目标：** 让你的 Agent 可以被测量。没有这个，每一次"改进"都只是感觉。

大多数工程师在这里卡住。他们能做出不错的 Agent，但判断不了下一个改动是在变好还是变差。

### 只选一个可观测性平台

不要同时跑两个。五个真正的选择：

- **LangSmith** ——在 LangGraph 或 LangChain 生态里就选这个
- **Braintrust** ——要做框架无关、能拦 PR 合并的 CI 质量门控就选这个
- **Arize Phoenix**（开源）+ **Arize AX**（托管）——要原生 OTEL 和漂移检测就选这个
- **W&B Weave** ——已经在用 Weights & Biases 就选这个
- **Inspect（英国 AISI）** ——要基准级别的 eval 精度就选这个，Anthropic、DeepMind、Grok 内部都在用

**看什么：**

- *LangSmith 文档*（免费层，官方）
- *Inspect AI 注解笔记*（Hamel Husain，免费）——安装 Inspect 前先读
- *Braintrust 文档*（免费层）
- *Agent Evaluation Readiness Checklist*（LangChain，免费）——打印出来贴在显示器旁边
- *Quantifying infrastructure noise in agentic coding evals*（Anthropic，2026年2月5日，免费官方）——不稳定沙箱和网络抖动单独就能让分数波动好几个点

### 四种必须实现的 Eval 类型

来自 Anthropic 的《Demystifying evals for AI agents》：

1. **单轮 eval** ——给这个输入，输出对不对？最便宜，尽可能用确定性评分器，持续跑
2. **轨迹 eval** ——Agent 是否用了正确的参数、按正确顺序调用了工具？覆盖单步、完整轮次和多轮三种变体
3. **LLM 作评判者** ——用于开放性输出（研究报告、代码审查）。每周对照人工评分样本校准
4. **最终状态 eval** ——用于有状态 Agent（写数据库、改文件），把环境最终状态和标准答案比对

**看什么：**

- *Demystifying evals for AI agents*（Anthropic，免费官方）
- *Evaluating Deep Agents: Our Learnings*（LangChain，免费）
- *How we build evals for Deep Agents*（LangChain，免费）——配合上篇一起读
- *Eval awareness in Claude Opus 4.6's BrowseComp performance*（Anthropic，2026年3月6日，免费官方）——设计 eval 前读这篇，别把偏差设计进去
- *Designing AI-resistant technical evaluations*（Anthropic，2026年1月21日，免费官方）——自己搭基准测试时必读

**实践项目：围绕第2阶段的研究 Agent 建立回归体系**

- 30-50题的手工评分黄金测试集，覆盖三个难度级别
- 能确定性评分的用精确匹配，开放性问题用5维度 LLM 评判者
- 轨迹 eval：Agent 是否做了规划、生成了2个以上子 Agent、引用了来源、在预算内完成
- 接入 GitHub Actions：黄金集通过率下降3个百分点或任何 pass^4 指标下降就拦住 PR
- 1% 的线上追踪每晚自动打分，漂移时告警
- 用 Inspect 跑至少一个公开基准（GAIA Level 1 或 τ²-bench retail），和公开排行榜比较
- `make eval` 命令输出三个产物：CI 通过/失败摘要、LangSmith 实验 URL、带基准分数的 Inspect 日志

### 第4阶段里程碑

阶段结束时，你应该能：

- 选定一个可观测性平台并从架构层面说清楚理由
- 实现全部四种 eval 类型
- 维护一个从生产失败中生长的黄金测试集，而不是用合成数据
- eval 分数回归时在 CI 中拦住 PR
- 写下你在自己 Agent 里找到的失败模式——那份文档才是真正的产出

---

## 第5阶段：生产加固（持续进行）

**这个阶段的目标：** 让你构建的一切，能扛住真实用户、真实成本和真实故障。

这不是一个能"完成"的阶段，它一直在持续。

### 成本纪律

- 积极用提示缓存。Anthropic 的缓存在重复前缀上能省下90%，把 CLAUDE.md、系统提示和工具定义都缓存起来
- 按难度路由：简单轮次用 Haiku 4.5 或 Sonnet 4.6，规划和难推理用 Opus 4.7
- 注意 Opus 4.7 的分词器：标价和4.6一样，但同样文本计费 token 可能多1到1.35倍，迁移后重新测每任务成本
- 非实时任务用批处理 API，便宜50%
- 多 Agent 预计消耗约是单 Agent 的15倍 token，只在答案价值足够高时才开

**看什么：**

- *Open Models have crossed a threshold*（LangChain，免费）——GLM-5 和 MiniMax M2.7 在核心 Agent 任务上已追平闭源前沿模型，锁定模型选型前先读

### 延迟优化

- 并行工具调用。Anthropic 研究系统提示里白纸黑字：创建多个子 Agent 时必须使用并行工具调用
- 通过 LangGraph 的 `stream_mode="updates"` 把部分输出流式传给 UI
- 子 Agent 扇出是最大的延迟杠杆：60步顺序 Agent → 10步主 Agent + 5个并行10步子 Agent

### 安全和沙箱

- 所有代码执行放沙箱：Modal、E2B、Daytona 或 LangSmith Sandboxes，绝不在主进程里 `exec()` 模型输出
- 凭证在模型上下文外代理（SaaS 认证用 Composio 处理）
- PreToolUse Hook 拦截破坏性 Bash 命令，正则过滤敏感信息，验证文件写入路径
- 不可逆操作加人在回路中断

**看什么：**

- *Modal 文档*（免费层）
- *E2B 文档*（免费层）
- *Beyond permission prompts: making Claude Code more secure and autonomous*（Anthropic，2025年10月20日，免费官方）——沙箱基础文章，你的 harness 应该复制这个模式
- *Claude Code auto mode: a safer way to skip permissions*（Anthropic，2026年3月25日，免费官方）——关任何"跳过确认"标志前把这两篇都读完

### 监控和漂移检测

- 低规模时100%追踪采样；高规模降到1-10%，对错误做分层采样
- 监控这几项：每次请求的 token 成本、工具调用失败率、LLM 评判者均分（每晚）、p95 延迟、eval 回归
- 每次模型升级后重新跑基准
- 注意 harness 僵化：随着模型变强，harness 里对模型能力的假设会过时

### 韧性

- 运行超过60秒的 Agent，持久执行是底线（Inngest、Temporal 或 LangGraph PostgresSaver）
- 每个节点后检查点，保证可回退可分叉

**看什么：**

- *How My Agents Self-Heal in Production*（LangChain，免费）——在每次部署后自动检测回归、定位原因、开修复 PR 的工作管道，把这个模式学过来

### 第5阶段里程碑

这个阶段没有终点。但你应该有：

- 提示缓存接入系统提示、CLAUDE.md 和工具定义
- 带硬性每任务成本上限和告警的模型路由层
- 所有代码执行的沙箱和凭证代理
- 拦截破坏性操作、强制不可逆操作人工审批的 Hook
- 追踪采样、漂移告警，以及每次模型升级后的重新基准
- 让进程中止变成小事的持久执行层

---

## 推荐

直接可以行动的建议。

**如果只学一个框架：** LangGraph 1.0 + Deep Agents。它是最通用的，运行时体系最成熟（PostgresSaver、时间旅行调试、持久执行、LangSmith 可观测性），不绑定特定模型，而且它的抽象（状态图+中间件）本身就是可迁移的心智模型。就这个，没有其他选择。

**如果只学一个参考 harness：** Claude Agent SDK + Claude Code。它就是参考实现。CLAUDE.md、Skill、子 Agent、Hook、Plan 模式、文件系统作内存——2026年其他 harness 都在向这些原语靠拢。每天用 Claude Code，读它的文档。

**如果只读一篇上下文工程文章：** Anthropic 的《Effective context engineering for AI agents》（2025年9月）。读两篇的话：加上 LangChain 的《Context Engineering for Agents》，补上 Write/Select/Compress/Isolate 框架。

**如果只学一个可观测性工具：** 待在 LangGraph 就选 LangSmith；要框架无关的 CI 门控就选 Braintrust；要基准级别的严格性就选 Inspect。

### 2026年直接跳过的东西

- AutoGen v0.4 和 AG2：都不是强推选项
- OpenAI Swarm：官方已宣布淘汰，不适合生产
- Assistants API：2026年中停用
- 在实际测出召回问题之前自己搭向量库
- "无代码" Agent 平台，除非你在做一次性项目

### 有特定理由才用的东西

- **CrewAI** ——想法到原型最快，生产脆弱，用于黑客马拉松和演示
- **OpenAI Agents SDK** ——绑在 OpenAI 生态就用这个
- **Pydantic AI / Pydantic Deep Agents** ——严格类型的 FastAPI 团队
- **Mastra** ——团队是 TypeScript 且不能用 Python 时
- **Smolagents** ——学习代码 Agent 模式用，生产能力弱
- **DSPy 3.0 + GEPA** ——有了可度量指标、想自动优化 Prompt 和 Agent 拓扑时用
- **Letta / MemGPT** ——跨 Session 需要操作系统级别内存时用，否则文件系统 + Mem0 更简单

### 基准收藏（2026年5月数据）

- **SWE-bench Verified：** Claude Opus 4.7 ≈ 87.6%，GPT-5.5 ≈ 88.7%，Gemini 3.1 Pro ≈ 78.8%
- **Terminal-Bench 2.0：** GPT-5.5 82.7%，Opus 4.7 ~70%，Gemini 3.1 Pro ~68%
- **τ-bench：** Claude Mythos Preview 89.2% 领先
- **BrowseComp：** GPT-5.5 90.1%，Gemini 3.1 Pro 85.9%，Opus 4.7 79.3%（比4.6的83.7%有退步，网络研究任务路由到 GPT-5.5）
- **GAIA / Princeton HAL：** Sonnet 4.5 以74.6%领先

### 时间里程碑

对有技术基础的 Agent 新手：

- **第2周：** 第0阶段完成，能用大白话讲清楚什么是 harness
- **第5周：** 第1阶段完成，带 Skill、Hook 和子 Agent 的 Claude Agent SDK Agent 上线
- **第9周：** 第2阶段完成，LangGraph 研究分析师 Agent 跑通，带 PostgresSaver 和 LangSmith 追踪
- **第13周：** 第3阶段完成，1500行迷你 harness 写完，能力和精简版 Claude Agent SDK 相当
- **第17周：** 第4阶段完成，黄金测试集建好，CI 门控接好，跑过一次 Inspect 基准
- **永久：** 第5阶段

兼职（每周10-15小时）的话，时间乘以约2.5倍。

两个调整计划的信号：第1阶段3周内跑不通，说明工具设计有问题——回去重读《Writing tools for agents》。第2阶段超过5周，说明你也在试图搭 harness——降到 Deep Agents，别跟它对抗。

---

## 注意事项

提前看到这些，能帮你少踩坑。

**基准是移动靶，部分已被套路。** SWE-bench Verified 两年内从1.96%涨到80%+。任何"X 模型得了Y%"的声明，都要理解为：模型+harness+脚手架+重试预算+系统提示的联合成绩，不是模型单独的。

**多 Agent 对大多数场景被过度炒作。** Anthropic 报告的90.2%提升，针对的是广度优先研究这个特定场景。对于编码和紧耦合任务，多 Agent 往往比单 Agent 更差，还多烧15倍 token。默认用单 Agent + 子 Agent，只有任务能自然分解时才动用完整多 Agent。

值得收藏的反例：Anthropic 的《Building a C compiler with a team of parallel Claudes》（2026年2月5日）——并行子 Agent 在编码任务上确实有效，但需要对的分解方式。

**框架格局随时可能再变。** LangChain 自己的定位18个月内换了两次。把赌注押在抽象上——循环、工具、上下文、子 Agent、持久化、追踪——这些才是可以带走的东西。

**MCP 的生产粗糙边缘是真实存在的。** 负载均衡器后的 HTTP 流式传输、多租户认证、限流、审计日志，这些都在2026年 MCP 路线图上，意味着还没解决。别深度耦合当前的 Session 模型。

**模型行为在小版本间会变化。** Opus 4.7 更严格的指令遵循和新分词器，意味着 Opus 4.6 的 Prompt 可能行为不同，同样文本的 token 成本高达35%。每次模型升级都重新跑一遍流量测试。

**你的 Eval 套件会腐化。** 今天建的黄金测试集，几个月后会随模型进步而饱和。计划每季度用生产故障（而不是合成数据）扩充10-20%。LLM 评判者的人工校准要一直跑下去。

**路线图里的一些来源有商业立场。** 尽量依赖一手来源（Anthropic 工程博客、LangChain 博客、OpenAI 公告、arXiv）。多个来源互相印证时，把那个共识当可靠的。

---

## 最后想跟你说的

跟你说实话，不加糖。

这份路线图不会在17周内让你成为首席 AI 工程师。但它会让你成为一个能做出 Agent 系统、发布它、让它在生产流量下真正跑起来的工程师。

而这恰好是公司现在愿意付钱买的东西。

对 Agent 工程师的需求不会放缓。57% 的团队 Agent 已上生产，89% 有可观测性，但头号障碍是质量（32%）。整个行业的瓶颈不是会调 LLM API 的人，而是能做好 eval 和 harness 的工程师。

Anthropic 的数字说明了真正的机会：同一个模型，不同的 harness，**CORE 评分78% vs 42%**。那个差距，就是你的工作。

公司还在挂"Prompt 工程师"职位。他们真正需要的，是能拿起一个前沿模型，把它变成一个可测量、可持续运行的生产系统的工程师。

这里是我想让你带走的三件事：

**第一，从每个阶段选一个项目，做出来。** 不是读它，是做出来，搞坏它，修好它，部署它，然后把 LangSmith 追踪和基准分数放进 README。被雇用的是能展示追踪记录的工程师，不是能背出框架对比表的工程师。

**第二，开始分享你学到的东西。** 写 harness 复盘，发布测试集发现，把基准数字连同 harness 配置一起发出去。教别人是最快的学习方式，同时在建立你的声誉。最好的机会找到的是可见的工程师，不是投了500份简历的工程师。

**第三，别等到"感觉准备好了"再开始。** 你永远不会感觉准备好。"我在读 LangChain 博客"和"我在发布一个有 PostgresSaver 持久化的 Deep Agent"之间的这段距离，是大多数工程师永远卡在里面的地方。

手上有一个跑起来的 Agent，就开始申请，开始公开构建，开始发布。哪怕它很小。市场不奖励完美，它奖励能让模型做出真实的东西、并且证明它没有退步的工程师。

17周，专注工作，足够改变一切。

做，做出来，然后测量你做出来的。

---

*本文由作者根据2到3个月积累的内部笔记和手写记录写成，经 Minimax 2.7 编辑。作者在 Obsidian 上有一套内容生产管道，按他的写作风格，由手写和手打笔记生成文章。*
