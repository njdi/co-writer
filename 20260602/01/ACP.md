# 从扣子本地 Agent 的一次「装包失败」，搞懂 ACP 协议

> 这篇从我接入扣子本地 Agent 时踩的一个坑讲起，把背后的门道一层层拆开：那个后台程序 `coze-bridge` 到底在做什么、日志里一直装不上的 npm 包是干嘛用的、以及当下越来越常被提到的 ACP 协议到底解决了什么问题。搞懂原理之后，再往前走一步看两个更实际的问题：我自己写代码能不能用这个包驱动本地的智能体？走 ACP 之后，对话还能像平时用 Claude Code 那样连贯、记得上下文吗？

最近扣子 3.0 出了一个新功能——本地 Agent。简单说，就是让你把自己电脑上已经装好的编程智能体（比如 Claude Code、Codex）接进扣子里用。

我挺感兴趣，就下载了桌面端，照着流程创建了一个基于 Claude Code 的本地 Agent。创建很顺利，界面也明确给了我「创建成功」的提示。

可问题就出在「创建成功」之后。

## 创建成功，却始终收不到响应

我打开对话框，发了第一条消息，然后就开始等。

等了很久，没有任何响应。

我以为是网络慢，又多等了一会儿，最后等来的是一行冷冰冰的「失败」。

我有点困惑。是我哪一步配置错了吗？于是我又试了 Codex 的本地 Agent，心想换一个框架总该行了吧。结果一模一样——创建成功，对话没响应，最后失败。

两个框架都这样，问题大概率不在某个具体框架上，而在它们共同依赖的那一层。可那一层是什么，我当时并不知道。

## 偶然抓到的一段错误日志

找不到原因的时候，我干脆开始「广撒网」：又接连创建了好几个本地 Agent，相当于反复做测试，看看能不能撞出点线索。

还真撞出来了。其中某一个 Claude Code 的本地 Agent，给我吐了这么一段错误日志：

```text
[Error] ACP wrapper 安装失败

Framework: claude-code
Package: @agentclientprotocol/claude-agent-acp@^0.39
执行命令: npm install -g @agentclientprotocol/claude-agent-acp@^0.39
失败原因: Command failed: npm install -g @agentclientprotocol/claude-agent-acp@^0.39
        (killed by SIGKILL) (phase=killing) | signal=SIGKILL
耗时: 55041ms

排查建议:
检查网络: curl -v https://registry.npmjs.org
查看当前 npm 源: npm config get registry
国内网络建议切镜像源:
npm config set registry https://registry.npmmirror.com/
```

日志说得很清楚：在执行 `npm install -g @agentclientprotocol/claude-agent-acp@^0.39` 这条命令时，安装跑了 55 秒，最后被 SIGKILL 干掉了。排查建议也直指国内网络和 npm 源不稳定。

到这里，「为什么没响应」的直接原因算是浮出水面了：本地 Agent 运行时需要装一个 npm 包，而这个包没装上。

但我更好奇的是另一个问题——这个叫 `@agentclientprotocol/claude-agent-acp` 的包，到底是干什么用的？它凭什么决定了我能不能收到响应？

## 先认识一下后台的 coze-bridge

要回答这个问题，得先从扣子本地 Agent 的运行方式说起。

其实在踩坑之前，我就注意到一个细节：接入本地 Agent 的核心，是要在自己电脑上安装并运行一个轻量程序——`coze-bridge`。按官方的说法，它负责在扣子和你电脑上的本地 Agent 之间建立连接。

我特意翻了一下进程列表，确认 `coze-bridge` 确实已经在后台跑着了。

所以这里的角色就清晰了：扣子的界面在云端，而真正干活的 Claude Code 在你本地，两边隔着网络，谁也碰不到谁。`coze-bridge` 就是中间那座桥，把云端的你和本地的智能体连起来。

可桥归桥，它怎么和本地各式各样的智能体「对话」呢？Claude Code 有 Claude Code 的用法，Codex 有 Codex 的用法，如果 `coze-bridge` 要针对每一个框架单独写一套对接逻辑，那也太累了。

顺着这条线查下去，我就查到了那个 npm 包，也查到了它背后的 ACP 协议。

## ACP 协议：让客户端和智能体能对上话

ACP 的全称是 Agent Client Protocol，直译过来是「智能体客户端协议」，由开发 Zed 编辑器的团队提出。

它要解决的问题，正是上面那个「太累」的困境。

打个比方。不同品牌的电器有不同的插头，如果每个插座都要为每种插头单独开一个孔，那墙上就得密密麻麻全是孔。后来大家约定了统一的插头标准，插座只认标准，电器也只做标准，两边就都省心了。

ACP 就是智能体世界里的这个「统一标准」。它定义了一套规则，规定「客户端」和「智能体」之间该怎么对话：

- **谁是客户端**：发起对话的一方，比如 Zed 编辑器，也比如这里的 `coze-bridge`。
- **谁是智能体**：真正干活的一方，比如 Claude Code、Codex。

只要双方都遵守 ACP，客户端就不用关心对面具体是哪个智能体——反正大家说的是同一种「语言」。这也是 ACP 最吸引人的地方：自带你的智能体，想换就换。

具体到通信方式，ACP 有几个值得一提的设计：

- **基于 JSON-RPC 2.0**：消息用大家都熟悉的 JSON 格式来传，简单通用。
- **走标准输入输出（stdio）**：客户端按需把智能体当作一个**子进程**拉起来，两边通过这个子进程的标准输入、标准输出来收发消息。不用配端口、不用管网络，进程之间天然隔离。
- **双向通信**：不只是客户端给智能体下命令，智能体也能反过来向客户端发请求。比如智能体要执行某条命令前，可以先回头问客户端：「这个操作要不要授权？」

如果你了解过 LSP（让各种编辑器都能复用同一套语言能力的协议），可以把 ACP 理解成「编程智能体界的 LSP」——同样是用一套标准，把原本两两耦合的关系解开。

## 那个装不上的包，正是关键的「翻译官」

现在回头看 `@agentclientprotocol/claude-agent-acp` 这个包，它的身份就清楚了。

Claude Code 的内核是 Claude Agent SDK，它本身并不是天生就会说 ACP。而这个 npm 包，就是一层**适配器**（日志里管它叫 wrapper，包装器）：它把 Claude Agent SDK 包装成一个标准的 ACP 智能体，对外说一口流利的 ACP。

有了它，任何 ACP 客户端都能驱动本地的 Claude Code。Codex 那边同理，对应的是 Codex 自己的那套 ACP 包装器。

于是整条链路就能完整地串起来了：

```text
扣子云端
   │
coze-bridge（本地的 ACP 客户端，那座桥）
   │  说 ACP
ACP wrapper（@agentclientprotocol/claude-agent-acp，那个 npm 包）
   │  翻译
Claude Code（Claude Agent SDK，真正干活的智能体）
```

`coze-bridge` 只负责说标准的 ACP，至于对面是 Claude Code 还是 Codex，它不操心；而把 ACP 翻译成各个框架听得懂的话，是那个 npm 包的活儿。

## 回到最初：为什么「创建成功」却没有响应

把这条链路看明白，我一开始那个困惑也就解开了。

「创建成功」这一步，其实只是把配置存了下来，告诉系统「我要接一个 Claude Code 的本地 Agent」。这一步不需要那个 npm 包，自然不会报错。

真正用到那个包，是在我**发出第一条消息**、链路需要被真正打通的时候。这时 `coze-bridge` 才去执行 `npm install -g`，想把 ACP 包装器装好、拉起子进程。

而我的网络偏偏卡在了这一步：包装器没装上，子进程起不来，链路就断在了「桥」和「翻译官」之间。消息发出去了，却没有任何一环能把它送达 Claude Code，更没人把结果传回来。

于是我看到的，就是「创建成功」之后那段漫长的、最终以失败收场的等待。

这也是为什么 Claude Code 和 Codex 两个框架都失败——它们卡住的不是各自的内核，而是中间那层共用的 ACP 链路。

至于解决办法，日志其实早就写在最后了：要么让网络能正常访问 npm 官方源，要么把源切到国内镜像，让那个包顺利装上。包装好了，桥和翻译官接上了，对话自然就通了。

## 顺手想到的：我能不能自己写代码接入？

把链路看明白之后，我冒出一个念头：扣子能做的事，我自己写代码是不是也能做？毕竟那个 npm 包又不是扣子专属的，它说的是标准的 ACP。

答案是可以。思路其实就是——**我自己写的程序，去扮演 `coze-bridge` 那个角色，也就是当一个 ACP 客户端**。那个 wrapper 包一行都不用改，直接拿来当智能体子进程用。

具体要做的事，对照前面的链路就能想明白：

第一步，**把 wrapper 当子进程拉起来**。用代码启动 `claude-agent-acp` 这个可执行文件，拿到它的标准输入和标准输出。从此我和它之间的所有对话，都走这两根管子——我往它的标准输入写消息，从它的标准输出读回复。

第二步，**按 ACP 的规矩收发 JSON-RPC 消息**。一条消息就是一行 JSON。一个典型的来回是这样的：

```text
initialize      ——  先握手，双方互相通报自己支持哪些能力
session/new     ——  开一个会话，告诉它工作目录在哪
session/prompt  ——  把我的问题发进去
（之后它会用一连串通知，把回答流式地推回来，我边收边显示）
```

第三步，**接住它反过来发给我的请求**。别忘了 ACP 是双向的：智能体要执行命令、读写文件之前，会回头问客户端「这个操作授权吗？」。这些请求是发给**我的客户端**的，我得接住并回应同意或拒绝。这一步是自己写客户端时最容易漏掉的，但少了它，智能体一碰到需要授权的操作就会卡住。

好在不用从零去拼 JSON。官方提供了现成的客户端 SDK，把握手、收发、流式更新这些协议细节都封装好了：TypeScript / JavaScript 用 `@zed-industries/agent-client-protocol`，Python 用对应的 python-sdk。用上 SDK，剩下要操心的基本就是「启动子进程、开会话、发问题、显示回复」这几件事。

说到底，就是把扣子那条链路里「云端 + coze-bridge」整段，换成我自己的程序：**我的客户端 ── ACP wrapper（npm 包）── 本地 Claude Code**。想换成 Codex，也只是把 wrapper 换成 Codex 对应的那个包而已。

## 那对话上下文呢？会像 Claude Code 一样连贯吗？

还有一个我很在意的问题，可能也是很多人会关心的。

平时在某个目录下启动 Claude Code，启动之后就有了一个会话，能一直连着聊，它记得前面说过什么、读过哪些文件、改过哪些代码。那如果改走 ACP 协议，能有同样的效果吗？还是说每问一句都是独立的、问完就忘？

我直接去翻了 ACP 的官方规范，特别是讲会话管理的那一页（地址放在本节末尾）。结论是：能，而且几乎是一一对应的。关键就在 ACP 的「会话（session）」这个概念上。下面每一条，我都尽量贴着规范的原文来说。

### 创建会话，约等于「在某个目录里启动 Claude Code」

客户端要开始一段对话，第一步是调 `session/new`。这个调用里有一个很关键的参数 `cwd`，规范对它的描述是「the working directory for the session」（会话的工作目录），并且明确要求它必须是一个**绝对路径**，用来作为这个会话在文件系统上操作的边界——也就是说，不管 wrapper 子进程是在哪儿被启动的，会话真正认的工作目录是这个 `cwd`。

一个 `session/new` 请求大致长这样：

```json
{
  "method": "session/new",
  "params": {
    "cwd": "/home/user/project",
    "mcpServers": []
  }
}
```

这一步其实就等价于「在 `/home/user/project` 这个目录下把 Claude Code 启动起来」——会话从这一刻起，就绑定在了那个目录上。调用成功后，智能体会返回一个唯一的会话 ID（`sessionId`），后面所有对话都靠它来认人。

### 同一个会话里，上下文是连贯的

这是我最想确认的一点。规范里有一句话说得很直接：每个会话都维护着自己独立的上下文、对话历史和状态（"Each session maintains its own context, conversation history, and state"）。

发起一轮对话用的是 `session/prompt`，请求里要带上 `sessionId`。所以只要我**守着同一个 `sessionId` 连续发 `session/prompt`**，第二句就能接着第一句来——它记得前面聊过什么、做过什么。这和平时用 Claude Code 连着聊，是一模一样的体验。

智能体的回答不是「等它全部想完再一次性丢回来」，而是过程中通过一连串 `session/update` 通知，把思考过程、工具调用、生成的文字**流式地**推回给客户端，由客户端边收边渲染。这也是为什么在编辑器里能看到智能体「一边干活一边冒字」的效果。

反过来，连贯与否的控制权其实在客户端手里：如果我每问一句之前都先 `session/new` 再发，那才是真正的「问一句忘一句」，相当于每问一次就重开一个 Claude Code。换句话说，**「独立」不是协议强加的，而是你自己选不选择复用会话的结果。**

### 比单开一个终端更灵活的地方

会话这套机制，除了能复刻 Claude Code 的连贯体验，还多给了几样东西，都能在规范里找到对应：

- **可以并发多个会话。** 规范原文说一个连接可以支撑若干并发会话，让你「同时进行多条思路」（"Each connection can support several concurrent sessions, so you can have multiple trains of thought going on at once"）。每个会话有各自唯一的 `sessionId`，互不干扰——相当于在好几个目录里各开了一个 Claude Code 同时跑，而它们共用同一个 wrapper 子进程。
- **可以恢复会话，而且分两种。** 一种是 `session/load`：规范说它会把**整段对话历史重放**给客户端（以 `session/update` 通知的形式，"replay the entire conversation to the Client"），适合你想把之前的上下文完整加载回来接着聊。另一种是 `session/resume`：规范特别强调它和 load 相反——智能体**不重放**历史（"the Agent MUST NOT replay the conversation history"），只恢复会话状态。
- **可以关闭会话。** 还有 `session/close`，用来关掉一个活跃会话。

### 一个重要前提：这些都要看「能力协商」

不过有一点必须说清楚，否则容易误导：上面这些进阶能力，**并不是无条件都有的**。

ACP 在最开始握手（`initialize`）时有一个**能力协商**的过程，智能体会声明自己支持哪些功能。`session/load`、`session/resume`、`session/close` 这些都各自对应一个能力开关——比如要用加载会话，智能体必须先声明 `loadSession` 能力；规范明确写道，如果 `loadSession` 是 `false` 或干脆没声明，客户端就**不允许**去调 `session/load`。

所以「这个会话到底能不能恢复、能不能并发」，对具体某一个 wrapper（比如 `@agentclientprotocol/claude-agent-acp`）来说，还得看它实际声明了哪些能力，不能一概而论。最基础的「开会话、连续对话」是普遍支持的，进阶的恢复 / 关闭则因实现而异。

### 回到扣子

这样再看扣子那个场景就更清楚了：界面上的每一个本地 Agent 对话，背后基本就对应着 `coze-bridge` 维持的一个 ACP 会话——一个绑定了目录、带连续上下文的 session。所以你在扣子里也能连着聊，它记得前文，而不是问一句忘一句。

> 本节关于会话的结论，均来自 ACP 官方规范的「Session Setup」页面：<https://agentclientprotocol.com/protocol/session-setup>。其中 `cwd`、`session/prompt`、`session/load`、`session/resume`、`session/close` 的方法名与行为，以及「每个会话维护独立上下文」「一个连接可并发多个会话」「`loadSession` 能力约束」等表述，均可在该页面查到。
