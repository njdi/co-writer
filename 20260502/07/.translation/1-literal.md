# 我如何将我的 Claude Code 变成一个 24/7 开发团队（完整指南 + 仓库列表）

**作者：** regent0x ([@regent0x_](https://x.com/regent0x_))  
**日期：** 2026年4月29日  
**来源：** [How I Turned My Claude Code Into 24/7 Dev Team (Full Guide + Repos)](https://x.com/Zephyr_hg/status/2049499354323399002)

大多数人把 claude code 当聊天机器人用。我把我的变成了一个 24/7 的开发团队，它记住了一切，并且每次会话都越来越聪明。

把这篇文章收藏起来，以免忘记。

我连续 3 个月都用错了 claude code。

每一次会话都是这样开始的。"我在用 typescript 构建一个 react 应用，使用 postgres，部署在 vercel 上，这是我的文件夹结构......"

同样的解释。一遍又一遍。每天都是。

然后我手动写同样的提示词。"审查这段代码。""为这个写测试。""修复 CI。"在一个终端里打出一段段话，而它一旦关闭就会忘记一切。

我统计了一周的时间。每天浪费 47 分钟在向一个本应了解我的工具重复解释自己。

然后我从头重建了我的整个配置。

现在 claude code 记住了我做过的每一个决定。它在我睡觉时并行运行 5 个 agent。它自动执行我的编码规范，不需要我每次询问。而且它每次会话都越来越聪明，而不是每次都归零。

整套系统的运行成本是每月 $20 的订阅费。

以下是我一步步构建它的详细过程。

## /第一部分 - CLAUDE.md：改变一切的基础

这个文件是 90% 的用户要么跳过、要么写错了的。

CLAUDE.md 存放在你的项目根目录。claude code 在每次会话开始时都会读取它。这是你一次性永久告诉 claude 你是谁、你在构建什么，以及你希望事情如何完成的方式。

大多数人写的是"这是一个 react 应用，请提供帮助"之类的话。

这没有用。

以下才是真正有效的做法：

```
# CLAUDE.md

## project
- stack: next.js 14, typescript, tailwind, postgres via prisma
- deployed on vercel, staging branch auto-deploys
- monorepo: /apps/web, /apps/api, /packages/shared

## conventions
- all components in PascalCase
- API routes return { data, error } format
- no default exports except pages
- tests live next to source files, named *.test.ts
- commits follow conventional commits (feat:, fix:, chore:)

## architecture decisions
- chose prisma over drizzle (dec 2024): type safety priority
- chose zustand over redux (jan 2025): less boilerplate
- auth via clerk, not next-auth: better DX for our team size

## current focus
- migrating payment system from stripe checkout to stripe elements
- performance audit on /dashboard (target: LCP < 2s)

## rules
- never mass edit more than 3 files without showing me the plan first
- always run existing tests before writing new ones
- if a task takes more than 5 steps, create a plan document first
```

差距是天壤之别。不用再花每次会话开头的 5 分钟解释你的项目，claude 已经知道你的技术栈、你的规范、你的架构决策，以及你当前正在做什么。

但这只是开始。CLAUDE.md 是静态的。它不会学习。它不会成长。为此你需要下一层。

## /第二部分 - 持久记忆：永不遗忘的配置

这是改变我一切的部分。

默认情况下，claude code 在会话之间没有任何记忆。每次对话都从零开始。你解释相同的上下文，做相同的更正，重新发现相同的解决方案。

我用三个工具协同工作来解决了这个问题。

![Image](images/img-01.jpg)

**记忆在会话之间如何流动**

**Obsidian 作为知识库**

我专门为我的开发工作搭建了一个 obsidian vault。不是笔记，不是书签，而是一个 claude code 可以读取和写入的结构化 wiki。

结构如下：

```
/vault
  /decisions      — 每一个架构决策及其上下文
  /errors         — 我们遇到的 bug 以及如何修复它们
  /patterns       — 在我们的代码库中有效的代码模式
  /sessions       — 每天发生了什么的摘要
  /stack           — 我们使用的每个工具的文档
  Memory.md       — 我是谁，我在构建什么，我的偏好
  index.md        — vault 中所有内容的主索引
```

这个想法来自 andrej karpathy 的 LLM wiki 概念——claude 不是在每次会话中从零开始重新发现知识，而是从一个随时间复利的持久 wiki 中读取。

> https://github.com/karpathy/llm-wiki

**claude-mem 用于会话持久性**

claude-mem 通过压缩添加长期记忆。在每次会话结束时，它将关键决策和上下文压缩到一个持久存储中，并将其携带到下一次会话。

> https://github.com/thedotmack/claude-mem

**潜意识 agent**

这个很厉害。claude-subconscious 运行一个后台 agent，它监视你的会话，读取你的文件，并随着时间的推移构建记忆，而无需你做任何事情。

这就像有一个初级开发者坐在你身后，记录你所做的一切。

> https://github.com/0xfurai/claude-subconscious

结果是：我在周一早上打开 claude code，它已经知道我周五正在调试支付 webhook 中的竞态条件，我决定从轮询切换到 websockets，以及我还需要更新测试。

不需要解释。它就是知道。

## /第三部分 - Skills：将通才变成专家

开箱即用，claude code 是一个通才。它什么都能做，但没有什么做得特别出色。

Skills 改变了这一点。它们是 markdown 文件，教 claude 如何按你想要的方式执行特定任务。

每个人都应该安装的第一个是 superpowers。

170k+ github stars。官方收录在 anthropic 插件市场。它将 claude code 从"被要求时写代码"转变为一套完整的开发方法论。

```
/plugin install superpowers@claude-plugins-official
```

它实际做的是：不是 claude 直接开始写代码，superpowers 强制执行一个工作流——头脑风暴 → 规格 → 计划 → TDD → 实现 → 审查。claude 询问你真正想构建什么，为你的审批编写规格，创建足够详细的计划供初级开发者跟随，然后用测试驱动开发来执行。

> https://github.com/obra/superpowers

在 superpowers 之后，我添加了专门的 skills：

> trail of bits 安全 skills - 真正的安全审计工作流，由真正的安全工程师构建。每个 PR 在我查看之前都会被扫描漏洞。

> https://github.com/trailofbits/claude-code-skills

> anthropic 的官方 skills - PDF、DOCX、XLSX 生成，数据分析。其他一切都基于此构建的权威参考。

> https://github.com/anthropics/skills

> tdd-guard - 自动阻止跳过测试的提交。claude 字面上无法发布未经测试的代码。它解释为什么阻止发生以及需要什么测试。

> https://github.com/nizos/tdd-guard

你可以堆叠任意多的 skills。它们不会冲突。每一个都让 claude 在某一件特定的事情上更好，合在一起它们创造了一个了解你确切工作流的专家。

## /第四部分 - Subagents：一个 claude 变成五个

这才是真正变得严肃的地方。

一个 claude code 会话一次只能做一件事。你让它写一个功能，然后审查代码，然后修复一个 bug，然后写文档——它按顺序执行每一个，当你到达第四个任务时，上下文已经被污染了。

Subagents 分配工作。不是一个超载的 claude，而是一个专家团队，每个人都有自己的上下文和单一职责。

我的配置使用五个 agents：

- **architect** - 处理高层设计决策，编写规格，规划实现。从不直接触碰代码
- **coder** - 按照 architect 的计划编写实际代码。拥有完整的工具访问权限
- **reviewer** - 以安全优先的思维审查每个 PR。标记问题，提出改进建议，检查测试覆盖率
- **tester** - 编写并运行测试。执行 TDD。与 tdd-guard 密切合作，确保没有没有覆盖率的东西被发布
- **ops** - 处理部署、CI/CD、基础设施。监控构建，修复失败

每个 agent 都有自己的 CLAUDE.md，包含特定的指令、工具权限和上下文边界。coder 永远看不到部署配置。reviewer 永远不写代码。干净的分离。

对于现成的 agent 集合：

> https://github.com/wshobson/agents - 25k+ stars，涵盖策略、开发、安全、设计的生产级 subagents

> https://github.com/davepoon/claude-code-subagents-collection - 100+ agents，适合任何工作流的即插即用

## /第五部分 - Hooks 和 Slash 命令：自动化重复性的事情

每次你发现自己第三次输入同样的指令，那就是一个等待出现的 slash 命令。

我设置了这些并每天使用它们：

> /fix-issue 456 - 读取 github issue，创建一个分支，编写一个带测试的修复，打开一个 PR。一个命令代替 10 分钟的工作流。

> https://github.com/claude-commands/command-fix-issue

> /review - 对当前 PR 触发带有安全检查、测试覆盖率分析和代码质量评分的 reviewer agent

> /deploy staging - 通过 ops agent 运行完整的部署流水线

对于 57 个生产就绪命令的完整集合：

> https://github.com/wshobson/commands - 1.7k+ stars，15 个工作流 + 42 个工具

Hooks 更进一步。它们在特定时刻自动触发：

> **pre-commit hook** - tdd-guard 在任何提交通过之前检查测试是否存在并通过

> **session start hook** - 从 obsidian 加载记忆，读取最近的会话日志，预热上下文

> **pre-push hook** - 代码到达远程之前，安全审查自动运行

你不再需要提醒 claude 你的规则，因为规则会自我执行。

## /第六部分 - 编排：agents 在你睡觉时工作

这是最后一块拼图。将每月 $20 的订阅变成感觉像拥有一个开发团队的东西。

claude-squad 是一个专门为并行运行多个 AI agents 构建的终端多路复用器。每个 agent 通过 git worktrees 获得自己的隔离工作区，因此它们在单独的分支上工作，不会有冲突。

```
brew install claude-squad
cs
```

就这样。你得到一个 TUI，你可以在其中启动、监控、暂停和恢复 agents。关闭终端——它们继续工作。早上回来就有完成的 pull requests 等着你。

> https://github.com/smtg-ai/claude-squad

![Image](images/img-02.jpg)

**我的夜间工作流**

睡前我打开 claude-squad 并启动三个会话：

- agent 1："修复仓库中所有标记为'bug'的未解决问题"
- agent 2："为 /apps/api/src/services/ 编写缺失的测试"
- agent 3："重构 dashboard 组件以使用新的设计 tokens"

我为可信任的任务启用自动接受模式（cs -y），对任何有风险的事情切换到计划模式。

我关上电脑。去睡觉。

早上：三个 PR 等待审查。每一个都在自己的分支上，没有冲突，测试通过。

对于更高级的编排：

> https://github.com/ruvnet/claude-flow - 11.4k+ stars，企业级多 agent 编排，具有持久记忆

## /第七部分 - 完整技术栈及其成本

以下是所有东西一起运行的情况：

```
layer 1: CLAUDE.md              — 免费（只是一个文件）
layer 2: obsidian + claude-mem  — 免费（obsidian 是免费的，仓库是开源的）
layer 3: superpowers + skills   — 免费（全部开源，MIT 许可证）
layer 4: subagents              — 免费（markdown 文件）
layer 5: hooks + commands       — 免费（全部开源）
layer 6: claude-squad           — 免费（开源）

total infrastructure cost: $0

claude code subscription: $20/mo (pro plan)
```

这个列表上的所有东西都是开源的。你唯一需要付费的是 claude 订阅本身。

ROI 完全不在一个量级上。我追踪了这套配置前后两周的生产力：

![Image](images/img-03.jpg)

**之前 vs 之后**

我每天浪费的那 47 分钟？没了。但更重要的是，agents 现在在凌晨 3 点做我以前在下午 3 点做的工作。

## /附赠 - 从哪里开始

你不需要今天就构建全部 6 层。

从这三个开始。它们只需要一个下午的时间：

![Image](images/img-04.jpg)

**一个下午的配置**

这套配置我花了 3 个月才摸索出来。

你可以在一个下午内构建好它。

你现在的 claude code 配置是什么样的？

关注我 [@regent0x_](https://x.com/@regent0x_) 来研究和了解最新的 alpha 信息。

感谢阅读。别忘了收藏这篇文章。
