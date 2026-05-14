# Codex CLI 的记忆系统是如何工作的

**作者：** mem0 ([@mem0ai](https://x.com/mem0ai))  
**日期：** 2026年5月13日  
**来源：** [How Memory Works in Codex CLI](https://x.com/Zephyr_hg/status/2054580022049198513)

Codex CLI 内置了一套生成式、异步摘要化的记忆存储，位于 `~/.codex/memories/`。

这是一个官方功能：

- 文档地址：[developers.openai.com/codex](https://developers.openai.com/codex)
- 完全开源：[github.com/openai/codex](https://github.com/openai/codex)

在这篇 *In Context* 文章里，我们会逐步拆解 Codex CLI 是如何处理记忆的。

Codex 是 OpenAI 的编程智能体，有三种形式：CLI、IDE 插件，以及 ChatGPT 内部的云端工作空间。

CLI 的文档最完善，记忆内部机制也是开源的，所以我们重点看这个。下面大部分内容同样适用于 IDE 插件，因为两者共用同一套 `~/.codex/` 配置和记忆布局。

## 记忆架构

Codex 的记忆只存在于一个地方：`~/.codex/memories/`。里面是一组固定的 Markdown 文件。没有 SQLite，没有嵌入向量索引，也没有不透明的二进制数据。

关键文件：

- `memory_summary.md`：下次会话启动时首先读取的合并视图
- `MEMORY.md`：完整的长格式合并记忆文件，按需 grep 检索
- `raw_memories.md`：合并前的提取输出
- `skills/<name>/SKILL.md`：特定技能的记忆
- `rollout_summaries/<slug>.md`：每次会话的摘要，用于驱动合并流程

![](images/img-01.jpg)

以上就是整个记忆层，仅此而已。其他所有东西，要么是填充它的写入管道，要么是从中读取的读取路径。

## 记忆是如何写入的

写入分两个阶段。

**阶段一：每次会话结束后。** 当会话空闲足够长时间（默认六小时），Codex 会触发一次后台处理：对话历史通过一个严格格式的提取提示词进行采样，每条输出都经过密钥脱敏，结果存入本地状态数据库。此时，任何数据都还没有写入记忆目录。

**阶段二：全局合并。** 系统会获取一个全局锁（存在状态数据库里），确保两次合并不会同时进行。加载最近阶段一的输出，同步到磁盘，检查生成的内容与现有内容是否有实质差异——如果有，才会启动一个独立的合并子智能体。这个子智能体读取候选记忆，判断哪些保留、哪些合并、哪些丢弃，再把差异写回 `~/.codex/memories/`。

![](images/img-02.jpg)

两个阶段都支持配置各自的模型（阶段一用 `extract_model`，阶段二用 `consolidation_model`），合并阶段以独立子智能体运行，不会打断用户正在进行的对话。

## 记忆是如何加载的

会话启动时，Codex 完整读取 `memory_summary.md`，截断至固定的 **5000 token** 上限（这是读取路径代码里定义的常量，公开文档没有提到），然后注入到开发者指令中。这个被截断的摘要，就是智能体预先获得的全部背景。

摘要里没有的内容，智能体会被要求直接 grep `MEMORY.md`。读取路径模板的指令是：从摘要里提取关键词，搜索 `MEMORY.md`，如果有指向相关发布摘要文件的线索就打开它，没有匹配就停止。整个搜索过程被控制在很少的步骤内。

![](images/img-03.jpg)

没有嵌入向量存储，没有相似度搜索，没有重排序。这是有意为之的设计——纯文本、子字符串匹配。换来的是可预测性和零检索成本，代价是：如果查询的措辞和存储的措辞不共享关键词，就找不到对应事实。

## 控制它的几个参数

少数几个配置项控制着以上所有行为。在依赖这套系统之前，值得提前了解。

- **默认关闭。** 需要先开启主开关 `features.memories`。开启后，两个子开关管理运行时：`generate_memories`（写入）和 `use_memories`（读取），功能启用后两者默认为 `true`。
- **空闲阈值。** `min_rollout_idle_hours`（默认 6）设置会话触发阶段一所需的最短空闲时间。活跃会话永远不会触发。
- **合并上限。** `max_raw_memories_for_consolidation`（默认 256，上限 4096）限制每次合并考虑的最近会话数量。
- **过期清理。** `max_rollout_age_days`（默认 30）使超出天数的会话不再参与记忆生成；`max_unused_days`（默认 30）使在该窗口内未被召回的记忆在下次合并中被排除。
- **配额感知。** `min_rate_limit_remaining_percent`（默认 25）在用户 API 配额不足时降低合并频率，防止后台任务影响前台请求。
- **密钥脱敏。** 任何记忆写入磁盘前，内置凭证清理。
- **地理限制。** 发布时，Memories 功能在 EEA、英国和瑞士不可用，这些地区的用户完全无法访问。

## 它停在哪里

最简洁的说法：这套记忆系统并不健壮。它本质上是单个用户在固定 token 预算内的几个 Markdown 文件，大多数失效模式都从这里来。

- **加载内容的硬上限。** `memory_summary.md` 在每次会话启动时被截断至 5000 token。超出的内容静默丢弃，没有警告，没有日志。智能体就是看不到它。
- **只有关键词检索。** 没进摘要的内容必须在 `MEMORY.md` 里靠字面子字符串匹配找到。换个说法描述的同一件事是不可见的。问"我们的部署命令是什么"，不会找到"生产部署走 `make ship-prod`"——除非这些词正好被存进去了。
- **grep 成本随文件增长。** `MEMORY.md` 是线性搜索的。对于用了好几个月、积累了大量记忆的用户，每次未命中再 grep 都要更贵。
- **只读不写，不支持手动编辑。** 文档把 `~/.codex/memories/` 定位为 Codex 自己管理的目录，手动编辑不是受支持的路径。用户真正想让智能体始终知道的内容，应该放在 `AGENTS.md` 里。
- **空闲门控的脆弱性。** 会话需要空闲六小时才能触发合并。连续高强度编程的开发者可能永远触发不了它。
- **仅限本地。** `~/.codex/memories/` 是每个用户、每台机器独立的文件系统状态。没有跨机器同步，没有团队共享，没有远程备份。
- **地理封锁。** Memories 在 EEA、英国和瑞士被屏蔽。

这些结构性限制在真实团队的具体场景里体现得最清楚。

![](images/img-04.jpg)

## Mem0 如何接入

Mem0 是一个位于智能体和持久化存储之间的记忆层。

Codex 有对应的 MCP 集成，文档在：[docs.mem0.ai/integrations/codex](https://docs.mem0.ai/integrations/codex)。

Codex CLI 原生支持 MCP 服务器，在 `~/.codex/config.toml` 的 `[mcp_servers.<name>]` 下配置（[配置参考](https://developers.openai.com/codex/config-reference)）。接入 Mem0 只需一个代码块：

```toml
[mcp_servers.mem0]
url = "https://mcp.mem0.ai/mcp"
bearer_token_env_var = "MEM0_API_KEY"
```

这一个配置块就向 Codex 暴露了九个 MCP 工具：`add_memory`、`search_memories`、`get_memories`、`get_memory`、`update_memory`、`delete_memory`、`delete_all_memories`、`delete_entities`、`list_entities`。

Codex 的智能体以调用其他 MCP 工具同样的方式使用它们。

![](images/img-05.jpg)

接入之后，底层这几件事会变：

- **跨机器的持久化记忆。** 本地 `~/.codex/memories/` 的限制消失了。同一份 Mem0 存储跟随用户跨越笔记本、服务器和 CI 环境，换台机器不需要从头重建。
- **跨工具的记忆共享。** 用 Codex CLI 做终端工作、用 Cursor 做编辑器工作的用户，可以把两者指向同一个 Mem0 后端。在 Codex CLI 会话里学到的东西（比如"暂存部署脚本会静默吞掉错误，同一诊断请用生产风格的输出"），下次在同一项目用 Cursor Agent 时就能看到。不需要在两个工具之间手动复制任何内容。
- **语义召回。** Mem0 通过嵌入向量搜索，按语义检索。Codex 的原生召回是完整读取 `memory_summary.md`，找不到时降级为 grep `MEMORY.md`——快且可预测，但措辞不同就找不到。换 Mem0 之后，问"我们的部署命令是什么"，也能找到"生产部署走 `make ship-prod`"——即使这两组词根本不重叠。
- **用户隔离。** 每个用户的 `userId` 限定其记忆范围。三个使用同一 Mem0 后端的团队成员各自保有独立的存储。
- **没有 5000 token 的摘要上限。** 检索是对实际存储的语义排名搜索，不是加载单个摘要文件的全部内容。记忆越积越多也不会因截断而失效。
- **实时写入。** Mem0 在对话过程中就写入记忆，不等六小时空闲门控。下次会话能立刻看到上次学到的内容。
- **在 Memories 不可用的地区可用。** EEA、英国和瑞士的用户可以获得一套记忆层，不依赖 Codex 的地区发布进度。

Codex CLI 的记忆层在今天的编程智能体里算是设计用心的：两阶段后台合并、密钥脱敏、基于 grep 的可预测 token 成本读取路径，整套管道完全开源。

如果你今天在用 Codex CLI，并且上面那些短板你已经碰到过，接入 Mem0 大约只需要一分钟 — [docs.mem0.ai/integrations/codex](https://docs.mem0.ai/integrations/codex)

---

*In Context #9*

这篇博客是 *In Context* 系列的一部分——[@mem0ai](https://x.com/mem0ai) 关于 AI 智能体记忆和上下文工程的博客系列。

@mem0ai 是一个智能的开源记忆层，专为 LLM 和 AI 智能体设计，提供跨会话的长期、个性化、上下文感知交互。

- 免费 API 密钥：[app.mem0.ai](https://app.mem0.ai)
- 或从[开源 GitHub 仓库](https://github.com/mem0ai/mem0)自托管 mem0。
