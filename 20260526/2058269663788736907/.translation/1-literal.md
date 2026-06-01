# 改变一切的 18 个 Claude 设置

**作者：** Mnimiy ([@Mnilax](https://x.com/Mnilax))  
**日期：** 2026年5月24日  
**来源：** [18 Claude settings that change everything](https://x.com/Mnilax/status/2058269663788736907)

改变一切的 18 个 Claude 设置。其中 14 个藏在三次点击之外。4 个不在任何文档里。

Anthropic 给 Claude Code 的 settings.json 提供了 125+ 个键。官方文档大约只覆盖了 40 个。

缺失的那些里，有 14 个藏在 Claude.ai 界面三次点击之外。有 4 个根本不出现在任何文档里。你只能通过读 GitHub issue、看工程师在 Discord 里泄露它们，或者凌晨一点去 grep Claude Code 二进制文件来找到它们。

大多数 Claude 用户用的还是 Anthropic 六个月前发布的那套配置。账单慢慢涨，输出慢慢漂，他们却怪模型。

下面是真正驱动你的 Claude 的 18 个设置。

- 8 个在 Claude dot ai。
- 7 个在 Claude Code。
- 3 个在 API 和 Console。

每一个都给出：它在哪里、它做什么、一行修复。

## 第一节：Claude（8 个设置）

### 1. Memory：范围、排除项，以及"忘掉这个"命令

**在哪里：** Settings → Capabilities → Memory

**它做什么：** Memory 在 2026 年 3 月向 Free 和 Pro 用户推出。默认情况下，它会存下所有 Claude 认为值得存的东西。三个大多数人错过的控制项：按项目划分范围、排除列表、即时忘记命令。

**为什么重要：** 默认的 memory 会漂移。4-6 周之后，它装满了一次性的纠正（"我在 Python 里喜欢用 tab"，你只对一个文件说过这一次）、会泄露到无关聊天里的项目专属事实，以及过时的角色背景。输出质量下降，因为 Claude 现在在为一个错误的"你"做优化。

**修复：**

打开按项目划分范围的 memory：Settings → Capabilities → Memory → Scope per Project。Project 内部的记忆只留在那个 Project 里。仅此一项就能修复大部分漂移。

把任何你不想在无关聊天里冒出来的话题加进排除列表。例子：离婚、医疗、薪水数字、客户名字。除非排除，否则这些都会持续存在，不管上下文是什么。

在任何聊天里使用内联的忘记命令：`forget what you remembered about [topic]`

Claude 会对照你的记忆库解析它，并确认它删掉了什么。没有菜单，没有设置页。

### 2. Extended Thinking：按聊天开关

**在哪里：** 聊天输入框 → 模型选择下拉菜单 → Extended Thinking: Off / Light / Full

**它做什么：** Extended Thinking 在回答之前加一轮 `<thinking>` 推理。Anthropic 给 Opus 默认开启它。这个三态开关是按聊天的，会覆盖全局设置。

**为什么重要：** Extended Thinking 对数学、调试、多步骤规划很棒。但用在摘要、翻译、格式化、重写、快速查询上就是浪费。在这些任务上，它会为同样的答案增加 3-12 秒延迟和 20-40% 的 token。

**修复：** 把默认设成 Light（只在模型判断有用时才用 thinking），并在做难活时显式切到 Full。我给大多数用户演示这个之后，他们第一周的 Opus token 开销就降了 18-25%。

### 3. Custom Styles：不是"声音"，而是真正的输出契约

**在哪里：** 聊天输入框 → 样式选择器 → Create New Style

**它做什么：** Styles 一开始是个语气开关（"正式 / 简洁 / 解释型"）。Custom Styles 实际上是一份输出契约。你粘贴一份 200-1500 字的指令文件。该样式下的每个回复在生成之前都会应用它。

**为什么重要：** 大多数人用 Styles 来"写短一点"。真正的用法是在每个回复里强制结构性规则，而不必反复粘贴。引用格式。禁用词。必需小节。代码块语言。长度上限。要不要问后续问题。

**修复：** 为每个工作流创建一个 Style。我的：

```markdown
# Style: Draft for X

Output contract:
- Open with one concrete number or named entity. No "I've been thinking..."
- Sentences under 18 words where possible.
- No em-dashes unless rhythm requires.
- No "delve", "leverage", "robust", "unlock", "game-changing".
- If listing 3+ items, use a hyphen list, not numbered.
- End on a statement, not a question.

If a draft exceeds 280 characters and the user didn't ask for a thread,
say so before answering.
```

轮换使用其中三个（Draft for X、Code review、Summarize PDF）就替代了我 80% 的保存 prompt。

### 4. Projects：大多数人留空的"instructions"字段

**在哪里：** 任意 Project → 右上角 ⋯ → Edit project instructions

**它做什么：** Projects 是持久化的工作空间。instructions 字段相当于系统提示词，会被注入到那个 Project 的每个聊天里。Anthropic 介绍 Projects 时配的是知识上传功能，那是人们记住的部分。instructions 字段就在同一个页面上，而我在实际中见到的 70% 的 Project 都把它留空。

**为什么重要：** 没有它，Project 里的每个聊天都是冷启动。有了它，你就不用反复建立上下文。（"这是一个 Polymarket 研究工作流。默认保持怀疑。永远展示概率计算。永远不要推荐交易——只描述 EV。"）

**修复：** 把它当成给 Claude 的 CLAUDE.md。保持在 400 字以内。指定角色、默认怀疑程度、格式规则、永远不要做什么。每月重读一次并修剪。

### 5. 搜索过往聊天（Pro+）以及怎么真正搜

**在哪里：** Settings → Profile → Search past chats（必须启用）

**它做什么：** 让 Claude 在相关时搜索你的对话历史。仅限 Pro+。

**为什么重要：** 对新账号默认关闭，即使是 Pro。一旦打开，诀窍在于知道它是关键词匹配，不是语义匹配。"我们昨天讨论的中国机器人是什么"会什么都搜不到，除非你的过往聊天里字面上包含"Chinese robots"或者"China"和"robots"。

**修复：** 打开它。然后学会真正的查询形态。用内容名词，不要用元词。"Polymarket Iran"有效。"我们上周聊的那个东西"没用。

### 6. Web search：按对话开关，以及引用行为

**在哪里：** 聊天输入框 → + → Web search: On / Off

**它做什么：** web search 开关是按对话的，但其行为会根据一个不太为人所知的设置而改变：Settings → Capabilities → Web search citations: Inline / Footnotes / Hidden。

**为什么重要：** 默认是 Inline。Inline 引用会破坏复制粘贴。当你把 Claude 的回答复制到别处时，你复制到的是指向虚无的标记。Footnotes 模式让回答保持干净，并在末尾列出来源。

**修复：** 如果你会把 Claude 的网络搜索答案复制到另一个文档、邮件或消息里，就切到 Footnotes。只有当你在 Claude 里读完所有内容时才保留 Inline。

### 7. Connectors：Cowork 里"信任此文件夹"的陷阱

**在哪里：** Settings → Connectors → Cowork → Trusted folders

**它做什么：** Cowork（2026 年 4 月 GA）让 Claude 访问你机器上的一个文件夹。默认情况下，Anthropic 在每个会话前会问你要不要信任这个文件夹。trusted-folders 列表是那道绕过口。

**为什么重要：** 一旦某个文件夹进了 trusted，Claude 在每个 Cowork 会话里都会从中读取而不再询问。如果你三月做测试时加了一个文件夹然后忘了，那 Claude 从那之后的每个会话都在悄悄读它。

**修复：** 打开 trusted folders。删掉任何不是当前活跃项目的东西。这个列表增长得比你想象的快。

### 8. Incognito 模式，以及它实际跳过了什么

**在哪里：** 侧边栏 → New incognito chat（或 Cmd/Ctrl + Shift + N）

**它做什么：** Incognito 聊天不被保存、不被记忆、不可被搜索、不被用于模型改进。聊天在你关闭时被删除。

**为什么重要：** 人们以为 Incognito 只是把聊天从侧边栏里藏起来。它实际上跳过了四个系统：memory 写入、聊天历史、过往聊天搜索索引、训练数据 opt-in（如果你开着的话）。

**修复：** 对任何涉及敏感数据的事情都有意识地用它：薪水、医疗、家庭、法律草稿、客户名字。三个按键，不用动脑。

![](images/img-01.jpg)

## 第二节：Claude Code（7 个设置）

这些都在 `~/.claude/settings.json`（用户级）或 `.claude/settings.json`（项目级）里。后者优先。

v2.1.105 二进制里一共有 125+ 个键。下面这七个是真正能产生效果的。

### 9. enabledPlugins —— 禁用，而不是卸载

**在哪里：** `~/.claude/settings.json` → enabledPlugins

**它做什么：** 设定哪些已安装的插件在会话启动时被加载。Plugin 市场让安装变得容易。卸载更难，而且如果你只是把值设成 false，就根本不必卸载。

**为什么重要：** 每个活跃的插件都会把它的 hooks、SKILL.md 内容和工具 schema 加载进你的上下文预算。三个你忘掉的插件 = 在你还没打一个字之前就预先消耗 3-8K token。

我开始这次审计时启用了 14 个插件。现在活跃的有 4 个。

**修复：**

```json
{
  "enabledPlugins": {
    "formatter@acme-tools": true,
    "deployer@acme-tools": false,
    "analyzer@security-plugins": false,
    "old-experiment@personal": false
  }
}
```

`false` 让插件保持已安装但不加载。需要时用 `/plugin enable name@marketplace` 按会话重新启用。

### 10. permissions.deny —— 关于那个 bug 你该知道的

**在哪里：** `~/.claude/settings.json` → permissions.deny

**它做什么：** 阻止 Claude 运行特定工具或访问特定文件。意图：防止 rm -rf、防止读 .env、防止在项目外写入。

**为什么重要：** 有一个已知 bug。deny 规则有时不会阻止。已经提了多个 GitHub issue。被引用最多的（anthropics/claude-code#11544）记录的是 hooks 在配置有效的情况下不加载；类似的模式也影响 deny 的执行。规则在你的配置里。debug 日志显示"0 matchers found"。Claude 还是照样读了那个文件。

**修复：**

```json
{
  "permissions": {
    "deny": [
      "Read(.env)",
      "Read(.env.*)",
      "Read(**/*secret*)",
      "Bash(rm -rf:*)",
      "Bash(sudo:*)"
    ]
  }
}
```

在文件系统层面再加一层。`chmod 600 .env`，这样即使 Claude 试图读它，操作系统也会拒绝。不要只信 deny 列表。在 Claude Code 里用 `/permissions` 验证。如果你的规则没出现，重启会话。

### 11. hooks.SessionStart —— 让我的上下文膨胀减少 30% 的那 4 行

**在哪里：** `~/.claude/settings.json` → hooks.SessionStart

**它做什么：** SessionStart 在你于某个目录里打开 Claude Code 时触发。你可以运行任何东西：打印环境信息、检查 git 状态、注入一个上下文文件、预热缓存。

**为什么重要：** 大多数人注入得太多。CLAUDE.md 涨到 5K token，因为每条项目规则都塞进去了。SessionStart 让你只加载与当前分支或目录相关的规则。

**修复：**

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "cat .claude/context-$(git branch --show-current).md 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

你的 main 分支加载 context-main.md。你的 feat/auth 分支加载 context-feat-auth.md。每个文件都很小。上下文预算不再流血。

### 12. disableAllHooks —— 紧急开关

**在哪里：** `~/.claude/settings.json` → disableAllHooks: true

**它做什么：** 用一个开关禁用所有 hook。在 2026 年 3 月的更新里发布。大多数人不知道它存在。

**为什么重要：** 当 Claude Code 开始行为怪异时（幽灵命令在跑、会话启动时挂起、神秘的文件写入），80% 的情况是某个 hook 在乱触发。一个一个禁用 hook 很慢。这个一次性全杀掉，好让你隔离问题。

**修复：** 让它保持 false。当出问题时，翻到 true，重启，看问题是否消失。如果是，再一个一个重新启用 hook。如果不是，bug 在别处。

### 13. model 按项目覆盖

**在哪里：** `.claude/settings.json`（项目根目录）→ model

**它做什么：** 为该项目设定默认模型。覆盖你的全局设置。

**为什么重要：** 大多数人全局设了 Opus，因为他们想用它做难活。然后他们打开一个主要是改 markdown 或 shell 脚本的项目。他们为 Haiku 用 1/20 成本就能做的任务付了 Opus 的钱。

**修复：**

```json
// 在你的 /docs 项目里：
{ "model": "claude-haiku-4-5-20251001" }

// 在你的 /infra 项目里：
{ "model": "claude-sonnet-4-6" }

// 在你的 /core-engine 项目里：
{ "model": "claude-opus-4-7" }
```

项目级覆盖优先。打开项目，拿到对的模型。继续干活。

### 14. mcpServers 配合 enabled 标志

**在哪里：** `~/.claude/settings.json` → mcpServers

**它做什么：** MCP server 把 Claude 连接到外部工具。每个连上的 server 都会把它完整的工具 schema 加载进你的上下文。每个 server 从 800 到 6000 token 不等。

**为什么重要：** 人们连上 MCP server 来测试，从不断开。三个月后你连着 12 个，其中真正在用的是 3 个。那 9 个没用的 server 在每次会话启动时花掉你约 25-40K token 的上下文 schema。

**修复：** 用 enabled 标志让连接保持已配置但不加载。

```json
{
  "mcpServers": {
    "github":   { "command": "...", "enabled": true },
    "postgres": { "command": "...", "enabled": true },
    "slack":    { "command": "...", "enabled": false },
    "linear":   { "command": "...", "enabled": false }
  }
}
```

需要时按会话翻成 true。大多数日子我有 2-3 个活跃。规划日则 6 个。

### 15. cleanupPeriodDays —— 没人提的那个缓存

**在哪里：** `~/.claude/settings.json` → cleanupPeriodDays

**它做什么：** 设定 Claude Code 保留 transcript、debug 日志和中间会话数据多少天。默认是 30。

**为什么重要：** Dreaming 和过往聊天搜索都依赖这些 transcript。在默认的 30 天窗口下，Dreaming 只能从一个月的工作里学习。六个月给它 6 倍的信号。磁盘成本：大约 200MB。

**修复：**

```json
{ "cleanupPeriodDays": 180 }
```

180 天的会话历史可供 Dreaming、记忆整合，以及你自己在找"三月那会儿我跟 Claude 说过的那个 auth bug 是啥"时用的 grep。

### Claude Code 成品：一份应用了全部 7 个设置的 settings.json

把这个复制进 `~/.claude/settings.json`。把路径和插件名改成你自己的。重启 Claude Code。重新运行 `/permissions` 和 `/hooks` 验证一切都加载了。

```json
{
  "model": "claude-sonnet-4-6",

  "enabledPlugins": {
    "formatter@acme-tools": true,
    "old-experiment@personal": false
  },

  "permissions": {
    "deny": [
      "Read(.env)",
      "Read(.env.*)",
      "Read(**/*secret*)",
      "Bash(rm -rf:*)",
      "Bash(sudo:*)"
    ]
  },

  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "cat .claude/context-$(git branch --show-current).md 2>/dev/null || true"
          }
        ]
      }
    ]
  },

  "disableAllHooks": false,

  "mcpServers": {
    "github":    { "command": "npx", "args": ["@modelcontextprotocol/server-github"], "enabled": true },
    "postgres":  { "command": "npx", "args": ["@modelcontextprotocol/server-postgres"], "enabled": false },
    "slack":     { "command": "npx", "args": ["@modelcontextprotocol/server-slack"], "enabled": false }
  },

  "cleanupPeriodDays": 180
}
```

项目级覆盖放在项目根目录的 `.claude/settings.json` 里。最有用的那个：

```json
// .claude/settings.json（在一个 docs 项目里）
{ "model": "claude-haiku-4-5-20251001" }
```

![](images/img-02.jpg)

## 第三节：API 和 Console（3 个设置）

这些在代码里或 Anthropic Console 里。它们是本文里最影响成本的设置。每一个都能把你的账单改变 30-90%。

### 16. cache_control 断点：放在哪里

**在哪里：** API 请求体，任意内容块上的 cache_control 字段

**它做什么：** 把你 prompt 的一个前缀标记为可缓存。后续带相同前缀的请求按大约 10% 的输入费率计费，而不是全价。

**为什么重要：** 这是 API 里最大的单个成本杠杆。人们知道它存在。大多数人把断点放错了，结果只省了一部分而不是全部。在我自己的配置上，修好断点把每月 $340 的账单砍到了 $87。

**修复：** 断点放在静态内容和动态内容的边界上。断点之前的任何东西都被缓存。之后的任何东西都被重算。

```python
# 错误 —— 断点在用户消息之后，没有可复用的东西被缓存
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": user_question,
     "cache_control": {"type": "ephemeral"}}
]

# 正确 —— 断点在稳定的系统提示词之后，下次调用全量命中缓存
messages = [
    {"role": "system", "content": SYSTEM_PROMPT,
     "cache_control": {"type": "ephemeral"}},
    {"role": "user", "content": user_question}
]
```

有两种 TTL 可用：5 分钟 ephemeral（默认）和 1 小时。对会话之间不变的系统提示词用 1 小时：

```python
{"cache_control": {"type": "ephemeral", "ttl": "1h"}}
```

缓存写入比基础输入贵 25%。缓存读取是基础输入的 10%。临界点：一个被缓存的前缀，如果你在 TTL 窗口内读它 2 次以上，就回本了。

### 17. inference_geo 和数据驻留税

**在哪里：** API 请求 → inference_geo 参数

**它做什么：** 把推理路由到一个特定的地理区域。仅美国驻留、仅欧盟，等等。

**为什么重要：** 仅美国数据驻留在 Opus 4.7 及以上会加 10% 的溢价。它不在标准价格表上。你会在发票上看到它。

**修复：** 如果你的合规制度并不真的要求区域驻留，就别设 inference_geo。大多数应用默认"为了保险"就设了它，因为法务里有人说"确保数据留在美国"。核实这个要求是合同性的还是只是愿景。如果只是愿景，就省掉这个参数，在每次 Opus 调用上省 10%。

如果你确实需要它，就把这 10% 算进你的模型选择里。基础价 $3 的 Sonnet 实际变成 $3.30，这会改变 Opus 对 Sonnet 的平衡点。

### 18. 工作空间级速率限制（防止凌晨三点宕机的那个）

**在哪里：** Console → Settings → Workspaces → [你的工作空间] → Per-feature rate limits

**它做什么：** 设定按工作空间、按功能的速率限制，独立于你的账号级限制。

**为什么重要：** 账号级限制保护你不破产。工作空间级限制在一个失控的批处理任务试图吃掉你整个 ITPM 额度时，保护你的交互式产品。你上线了一个新功能，它出 bug，它循环，它吃光一切，你面向客户的聊天开始返回 429。工作空间限制让一个功能不会饿死另一个。

**修复：** 为每个面（交互式聊天、批处理、内部工具、实验性）创建一个工作空间。把每个工作空间的速率限制设成账号档位的 60-70%。留 30% 给任何需要突发的工作空间。

本文里第四个未记录的设置：每个工作空间里有一个功能级的上限，只有当你点进某个具体功能卡片、而不是工作空间总览时才看得见。默认 = 无限制。

如果你在一个工作空间里有三个功能，其中一个能饿死另外两个，而工作空间级限制抓不到它。给任何做批处理的东西设功能级上限。

![](images/img-03.jpg)

## 第四节：18 项清单

走一遍。20 分钟。任何你 12 个月里都没碰的东西，你大概永远不会碰。

```markdown
## Claude.ai
- [ ] #1  Memory：项目范围打开，排除列表已填
- [ ] #2  Extended Thinking：默认 = Light
- [ ] #3  Custom Styles：至少创建一个工作流样式
- [ ] #4  Project Instructions：为每个活跃 Project 填写
- [ ] #5  Past-chats search：打开（Pro+）
- [ ] #6  Web search citations：Footnotes 模式
- [ ] #7  Cowork trusted folders：已审查、已修剪
- [ ] #8  Incognito：记住键盘快捷键

## Claude Code
- [ ] #9  enabledPlugins：只有活跃的 = true
- [ ] #10 permissions.deny：env 文件 + sudo + rm -rf 已阻止，OS 级备份就位
- [ ] #11 hooks.SessionStart：分支感知的上下文加载器
- [ ] #12 disableAllHooks：false（知道开关在哪）
- [ ] #13 model：为 docs/infra/core 项目设了按项目覆盖
- [ ] #14 mcpServers：用 enabled 标志，不是完全删除
- [ ] #15 cleanupPeriodDays：180

## API / Console
- [ ] #16 cache_control：断点在稳定的系统提示词之后，每日稳定的前缀用 1h TTL
- [ ] #17 inference_geo：只在合规确实要求时才设
- [ ] #18 Workspace rate limits：按工作空间 且 按功能的上限都设了
```

## 第五节：审计脚本（每周跑一次）

把这个放进 `~/bin/claude-audit.sh`。每周跑。它会标记清单里 Claude Code 那一半，加上 API 那一半里 cache_control 的部分。

```bash
#!/usr/bin/env bash
# claude-audit.sh — flags settings drift across the 7 Claude Code + 1 API checks

CLAUDE_DIR="$HOME/.claude"
SETTINGS="$CLAUDE_DIR/settings.json"

echo "=== Plugins enabled ==="
jq '.enabledPlugins // {} | to_entries | map(select(.value==true)) | length' "$SETTINGS" 2>/dev/null
echo "Target: 3-5 active. Re-enable per session for the rest."

echo
echo "=== MCP servers enabled ==="
jq '.mcpServers // {} | to_entries | map(select(.value.enabled==true)) | length' "$SETTINGS" 2>/dev/null
echo "Target: 3 always-on. Per-session enable rest."

echo
echo "=== permissions.deny rules present ==="
jq '.permissions.deny // [] | length' "$SETTINGS" 2>/dev/null
echo "Target: >=5 rules. .env / sudo / rm -rf at minimum."

echo
echo "=== SessionStart hook configured ==="
jq '.hooks.SessionStart // [] | length' "$SETTINGS" 2>/dev/null
echo "Target: >=1 entry."

echo
echo "=== cleanupPeriodDays ==="
jq '.cleanupPeriodDays // 30' "$SETTINGS" 2>/dev/null
echo "Target: 180."

echo
echo "=== Per-project model overrides ==="
find . -maxdepth 3 -name "settings.json" -path "*/.claude/*" 2>/dev/null | while read f; do
  model=$(jq -r '.model // "—"' "$f")
  echo "  $f → $model"
done
echo "Target: docs → haiku, infra → sonnet, core → opus."

echo
echo "=== API cache_control check (set API_KEY to run) ==="
if [ -n "$ANTHROPIC_API_KEY" ]; then
  echo "Manual check: every system_prompt over 1K tokens should have cache_control with 1h TTL."
else
  echo "Skipped — set ANTHROPIC_API_KEY to enable."
fi
```

保存，`chmod +x ~/bin/claude-audit.sh`，每周跑，直到每一行都达标。

## 第六节：没能入选的

我在发布前去掉了四个候选项。值得点名，免得你浪费时间去追它们。

**Adaptive Reasoning 开关。** Anthropic 把它发布成默认开启。覆盖项在 Settings → Capabilities → Reasoning mode。在 30 天的对比里，我找不到一个覆盖它就能显著改变结果的工作流。信任默认值。继续走。

**Skill 自动激活。** 你可以切换 Claude 是基于相关性检测自动加载技能，还是需要显式调用。我本以为这会有影响。它没有。带渐进式披露的自动激活（在需要之前只加载 SKILL.md 元数据）调得很好。让它开着。

**Dispatch 手机到桌面控制。** 有用的功能，不是设置审计项。要么你有个适合它的工作流，要么没有。没有哪个隐藏开关能改变结果。

**按工作空间的 max_tokens 上限。** 你可以强制每个回复在 800、2000 或 4000 处截断。它在啰嗦的工作流上能省真金白银，但会毁掉需要长输出的代码生成。值得按工作空间测试。不值得作为默认推荐。

T H E _ E N D

今晚走一遍清单。你们大多数人会修 6-8 处。少数人会修 14+。你账单仪表盘和用量图里的数字会告诉你，这 20 分钟值不值。
