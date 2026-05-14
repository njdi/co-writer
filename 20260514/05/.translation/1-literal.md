# Codex CLI 的记忆系统是如何工作的

**作者：** mem0 ([@mem0ai](https://x.com/mem0ai))  
**日期：** 2026年5月13日  
**来源：** [How Memory Works in Codex CLI](https://x.com/Zephyr_hg/status/2054580022049198513)

Codex CLI 内置了一个生成式、异步摘要化的记忆存储，位于 `~/.codex/memories/`

这是一个官方功能：

- 文档地址：[developers.openai.com/codex](https://developers.openai.com/codex)
- 完全开源：[github.com/openai/codex](https://github.com/openai/codex)

在这篇 *In Context* 文章中，我们将逐步讲解 Codex CLI 中记忆是如何被处理的。

Codex 是 OpenAI 的编程智能体，有三种形式：CLI、IDE 插件，以及 ChatGPT 内部的云端工作空间。

CLI 是文档最为完善的界面，其记忆内部机制也是开源的，因此我们重点分析它。以下大部分内容同样适用于 IDE 插件，因为两者共享相同的 `~/.codex/` 配置和记忆布局。

## 记忆架构

Codex 的记忆存储在一个目录中：`~/.codex/memories/`。该目录包含一组固定的 Markdown 文件。没有 SQLite，没有嵌入向量索引，也没有不透明的二进制数据。

关键文件：

- `memory_summary.md`：下次会话启动时首先读取的合并视图
- `MEMORY.md`：完整的长格式合并记忆文件，按需 grep 检索
- `raw_memories.md`：合并前的提取输出
- `skills/<name>/SKILL.md`：特定技能的记忆
- `rollout_summaries/<slug>.md`：每次会话的摘要，用于驱动合并流程

![](images/img-01.jpg)

这就是整个记忆层。其他所有东西都是填充它的管道和从中读取的读取路径。

## 记忆是如何写入的

写入路径分为两个阶段。

**阶段一：每次发布（per-rollout）。** 当会话空闲足够长的时间后（默认六小时），Codex 认领一个启动任务，对话历史会通过一个严格模式的提取提示词进行采样，每条输出都经过密钥脱敏处理，结果存储到本地状态数据库中。此时，任何数据都还没有写入记忆目录。

**阶段二：全局合并。** 获取一个全局锁（存储在状态数据库中），确保两次合并操作不会并行进行。加载最近的阶段一输出，同步到磁盘，检查生成的工作区是否与现有内容有实际差异，如果有，才会启动一个独立的合并子智能体。该子智能体读取候选记忆，决定哪些要合并、哪些要修补、哪些要丢弃，并将差异写回 `~/.codex/memories/`。

![](images/img-02.jpg)

两个阶段都使用可配置的模型（阶段一用 `extract_model`，阶段二用 `consolidation_model`），且合并阶段以独立的子智能体运行，而不是内嵌在用户对话中。

## 记忆是如何加载的

会话启动时，Codex 完整读取 `memory_summary.md`，将其截断至固定的 **5000 token** 预算（这是读取路径代码中定义的常量，公开文档中未提及），然后注入到开发者指令中。这个被截断的摘要就是智能体预先加载的全部内容。

对于摘要中没有的内容，智能体被指示直接 grep `MEMORY.md`。读取路径模板会告诉智能体：从摘要中提取关键词，搜索 `MEMORY.md`，如果指向了相关的发布摘要文件则打开它，如果没有匹配则停止。整个搜索预算被控制在较少的步骤内。

![](images/img-03.jpg)

没有嵌入向量存储，没有相似度搜索，没有重新排序步骤。这是设计上的选择：纯文本加子字符串匹配。代价是可预测性和零检索时间成本，但无法找到查询和存储措辞不共享关键词的事实。

## 控制它的机制

少数几个配置项控制着以上所有行为。在依赖该系统之前，值得了解一下。

- **默认关闭。** 需要开启一个主开关 `features.memories`。开启后，两个子开关控制运行时行为：`generate_memories`（写入）和 `use_memories`（读取）。功能启用后两者默认为 `true`。
- **空闲阈值。** `min_rollout_idle_hours`（默认 6）设置会话符合阶段一条件所需的最短空闲时间。活跃会话永远不会触发它。
- **合并上限。** `max_raw_memories_for_consolidation`（默认 256，上限 4096）限制每次合并操作考虑的最近发布数量。
- **老化。** `max_rollout_age_days`（默认 30）使超出天数的会话不再参与记忆生成。`max_unused_days`（默认 30）使在该窗口内未被召回的记忆在下次合并中不再被纳入。
- **速率限制感知。** `min_rate_limit_remaining_percent`（默认 25）在用户 API 配额不足时降低合并频率，防止后台工作影响前台请求。
- **密钥脱敏。** 在任何记忆写入磁盘之前，内置凭证清理功能。
- **地理限制。** 发布时，Memories 功能在 EEA、英国和瑞士不可用。这些地区的用户完全无法访问。

## 它的局限性

最简洁的描述：这个记忆系统并不健壮。它是单个用户在固定 token 预算内的 Markdown 文件，大多数失效模式都源于此。

- **加载内容的硬 token 上限。** `memory_summary.md` 在每次会话启动时被截断至 5000 token。超出上限的内容会被静默丢弃。没有警告，没有日志。智能体就是看不到它。
- **仅限关键词的后备检索。** 没有出现在摘要中的任何内容都必须在 `MEMORY.md` 中通过字面子字符串匹配找到。改写过的事实是不可见的。"我们的部署命令是什么？"不会找到"生产部署通过 `make ship-prod` 进行"，除非其中一个确切术语被存储。
- **grep 成本随文件增长。** `MEMORY.md` 是线性搜索的。对于有几个月积累记忆的长期用户，每次未命中再 grep 的成本都会更高。
- **只有生成状态，不可手动编辑。** 文档将 `~/.codex/memories/` 定位为 Codex 管理的目录。手动编辑记忆不是受支持的路径。用户真正想让智能体始终知道的内容应放在 `AGENTS.md` 中。
- **空闲门控的脆弱性。** 会话需要空闲六小时才能触发合并。持续连续编程的开发者可能永远不会触发它。
- **仅本地状态。** `~/.codex/memories/` 是每个用户、每台机器的文件系统状态。没有跨机器同步，没有团队共享，没有远程备份存储。
- **地理封锁。** Memories 在发布时在 EEA、英国和瑞士被屏蔽。

生产场景中触及这些限制

这些结构性限制在真实团队中出现的具体案例中体现得最为明显。

![](images/img-04.jpg)

## Mem0 如何融入

Mem0 是一个位于智能体和持久化存储之间的记忆层。

具体到 Codex，有一个 MCP 集成，文档地址：[docs.mem0.ai/integrations/codex](https://docs.mem0.ai/integrations/codex)。

Codex CLI 原生支持 MCP 服务器。它们在 `~/.codex/config.toml` 的 `[mcp_servers.<name>]` 下配置（[配置参考](https://developers.openai.com/codex/config-reference)）。最简化的 Mem0 配置只需一个代码块：

```toml
[mcp_servers.mem0]
url = "https://mcp.mem0.ai/mcp"
bearer_token_env_var = "MEM0_API_KEY"
```

这一个代码块就向 Codex 暴露了九个 MCP 工具：`add_memory`、`search_memories`、`get_memories`、`get_memory`、`update_memory`、`delete_memory`、`delete_all_memories`、`delete_entities`、`list_entities`。

Codex 的智能体以与使用其他任何 MCP 工具界面相同的方式调用它们。

![](images/img-05.jpg)

底层发生了什么变化：

- **持久化的跨机器记忆。** 本地 `~/.codex/memories/` 的限制消失了。同一个 Mem0 存储跟随用户跨越笔记本、服务器和 CI 环境。在新机器上无需从头重新生成。
- **跨工具记忆。** 一个用户在终端使用 Codex CLI、在编辑器使用 Cursor，可以将两者指向同一个 Mem0 后端。在 Codex CLI 会话中捕获的事实（"暂存部署脚本会静默吞掉错误，同一诊断请使用生产风格的输出"）会在下次对同一项目运行 Cursor Agent 时浮现。用户不需要在两个工具之间手动复制任何内容。
- **语义召回。** Mem0 通过语义检索，借助嵌入向量搜索。Codex 的原生召回完整读取 `memory_summary.md`，不命中时降级为 grep `MEMORY.md`：快速且可预测，但无法找到措辞与查询不同的存储事实。使用 Mem0，问"我们的部署命令是什么？"能找到"生产部署通过 `make ship-prod` 进行"，即使这两组词并不重叠。
- **每用户隔离。** 每个用户的 `userId` 限定其记忆范围。三个使用同一 Mem0 后端的团队成员各自保有独立的存储。
- **没有 5000 token 摘要上限。** 检索是对实际存储的排名语义搜索，而不是整体加载单个摘要文件。大型记忆库保持可用，而不是被截断以适应开发者指令预算。
- **实时更新。** Mem0 在对话进行中写入记忆，而不是等待六小时空闲门控。下次会话能看到上次会话教给它的内容。
- **在 Memories 不可用的地区可用。** EEA、英国和瑞士的用户可以获得一个不依赖 Codex 地区发布的记忆层。

Codex CLI 的记忆层在今日编程智能体领域设计精良：两阶段后台合并、密钥脱敏、基于 grep 的具有可预测 token 成本的读取路径，以及一个完全开源的管道。

如果你今天正在运行 Codex CLI，并且这些差距对你来说很熟悉，Mem0 集成大约只需一分钟 — [docs.mem0.ai/integrations/codex](https://docs.mem0.ai/integrations/codex)

---

*In Context #9*

这篇博客是 *In Context* 系列的一部分，这是 [@mem0ai](https://x.com/mem0ai) 关于 AI 智能体记忆和上下文工程的博客系列。

@mem0ai 是一个智能的开源记忆层，专为 LLM 和 AI 智能体设计，提供跨会话的长期、个性化、上下文感知交互。

- 在此获取免费 API 密钥：[app.mem0.ai](https://app.mem0.ai)
- 或从我们的[开源 github 仓库](https://github.com/mem0ai/mem0)自托管 mem0。
