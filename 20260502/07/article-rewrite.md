# 我如何把 Claude Code 变成一支 24/7 的开发团队

**作者：** regent0x ([@regent0x_](https://x.com/regent0x_))  
**日期：** 2026年4月29日  
**来源：** [How I Turned My Claude Code Into 24/7 Dev Team (Full Guide + Repos)](https://x.com/Zephyr_hg/status/2049499354323399002)

先收藏，以免丢了。

---

说一件有点丢人的事：我用错了 claude code，整整 3 个月。

每次打开终端，第一件事就是解释："我在用 typescript 写一个 react 应用，用 postgres，部署在 vercel，这是我的目录结构......"

同样的一段话，每天重复，像在跟一个失忆的助手打交道。

不止如此。每次想让它干点具体的事，还得手动把提示词打一遍——"帮我 review 这段代码""给这个写测试""把 CI 修一下"。一大段话，打完，用完，关掉，全忘。

后来我数了一下：每天有 47 分钟，我在干同一件事——向一个本该已经了解我的工具，重复解释我自己。

于是我把整套配置从头重来。

现在的情况是：claude code 记得我做过的每一个决定。它在我睡觉时并行跑 5 个 agent。我的编码规范它自动遵守，不用我每次开口。而且越用越好用，而不是每次都回到原点。

整套系统，每月 20 美元的订阅费。

下面我一层一层拆给你看。

---

## 第一层：CLAUDE.md，让它记住你是谁

这个文件，90% 的人要么跳过了，要么写错了。

CLAUDE.md 放在项目根目录，claude code 每次会话开始时都会读它。说白了，它就是你告诉 claude "我是谁、在做什么、希望你怎么做事"的地方——一次写好，永久生效。

大多数人写的是"这是一个 react 应用，请提供帮助"。

没用。

这样写才有用：

```
# CLAUDE.md

## 项目信息
- 技术栈：next.js 14、typescript、tailwind、postgres（通过 prisma）
- 部署在 vercel，staging 分支自动部署
- monorepo 结构：/apps/web、/apps/api、/packages/shared

## 编码规范
- 所有组件使用 PascalCase 命名
- API 路由统一返回 { data, error } 格式
- 除 pages 外禁止使用默认导出
- 测试文件放在源文件旁边，命名为 *.test.ts
- commit 遵循约定式提交（feat:、fix:、chore:）

## 架构决策
- 选 prisma 而非 drizzle（2024年12月）：类型安全优先
- 选 zustand 而非 redux（2025年1月）：减少样板代码
- 用 clerk 做认证，不用 next-auth：对我们团队规模来说开发体验更好

## 当前重点
- 将支付系统从 stripe checkout 迁移到 stripe elements
- /dashboard 性能优化（目标：LCP < 2s）

## 规则
- 一次改动超过 3 个文件时，必须先给我看方案
- 写新测试之前，先跑一遍已有的测试
- 任务超过 5 个步骤，先创建一份计划文档
```

有了这个，你不用再花每次会话开头的 5 分钟解释背景。claude 已经知道你的技术栈、你的规范、你的架构选择，以及你现在在做什么。

不过这只是起点。CLAUDE.md 是静态的——它不会学习，不会成长。要解决"每次都要重新解释"的问题，需要下一层。

---

## 第二层：持久记忆，让它记住发生过的事

这是改变我最多的一部分。

claude code 默认在会话之间没有任何记忆。每次对话都从零开始。同样的上下文要一遍遍解释，同样的错误要一遍遍纠正，同样的解决方案要一遍遍重新摸索。

靠三个工具配合，我把这个问题解决掉了。

![Image](images/img-01.jpg)

**记忆在会话之间如何流动**

**Obsidian 当知识库**

我专门为开发工作搭了一个 obsidian vault。不是记笔记，不是存书签，而是一个 claude code 可以读取和写入的结构化 wiki。

结构是这样的：

```
/vault
  /decisions      — 每一个架构决策及其背景
  /errors         — 遇到的 bug 和修复方法
  /patterns       — 在这个代码库里好用的代码模式
  /sessions       — 每天发生了什么的摘要
  /stack           — 每个工具的使用文档
  Memory.md       — 我是谁，在做什么，我的偏好
  index.md        — vault 中所有内容的总索引
```

这个思路来自 andrej karpathy 的 LLM wiki 概念。核心逻辑很简单：与其让 claude 每次从头摸索，不如给它一个随时间持续积累的知识库，让它每次都从已有的认知出发。

> https://github.com/karpathy/llm-wiki

**claude-mem：压缩会话，带到下一次**

claude-mem 在每次会话结束时，把关键决策和上下文压缩存起来，下次会话时带回来。

> https://github.com/thedotmack/claude-mem

**潜意识 agent：什么都不用做，它自己记**

这个有点意思。claude-subconscious 会在后台默默跑一个 agent，监视你的会话，读取你的文件，随着时间自己积累记忆——不需要你做任何操作。

就像有个实习生一直坐在你背后，把你做的事情都记下来。

> https://github.com/0xfurai/claude-subconscious

效果是：周一早上打开 claude code，它已经知道我上周五在调试支付 webhook 里的竞态条件，知道我决定把轮询换成 websockets，知道测试还没更新。

不需要解释。它直接知道。

---

## 第三层：Skills，把通才变成专家

claude code 开箱即用是个通才——什么都能做，但没有哪件事做得特别出色。

Skills 改变了这一点。它们是一些 markdown 文件，教 claude 按你想要的方式完成特定任务。

第一个所有人都应该装的是 superpowers。

170k+ github stars，已收录进 anthropic 官方插件市场。它做的事情是：把 claude code 从"你让我写什么我就写什么"，变成一整套开发方法论。

```
/plugin install superpowers@claude-plugins-official
```

具体怎么变？它不让 claude 上来直接写代码，而是强制走一套流程：头脑风暴 → 需求确认 → 计划 → TDD → 实现 → 审查。claude 会先问你真正想做什么，写一份需求文档让你确认，再列出一份初级开发者也能跟着做的详细计划，然后用测试驱动开发推进。

> https://github.com/obra/superpowers

装了 superpowers 之后，我又加了几个专项 skills：

> trail of bits 安全 skills——由真正的安全工程师写的审计工作流。每个 PR 在我看之前都会被扫一遍漏洞。

> https://github.com/trailofbits/claude-code-skills

> anthropic 官方 skills——PDF、DOCX、XLSX 生成，数据分析。其他很多 skills 都在这个基础上搭建。

> https://github.com/anthropics/skills

> tdd-guard——自动拦截跳过测试的提交。claude 没办法发布没有测试的代码，它会解释为什么被拦，以及需要哪些测试。

> https://github.com/nizos/tdd-guard

skills 可以叠加，不会冲突。每一个让 claude 在某件事上更专，叠在一起就是一个懂你工作方式的专家。

---

## 第四层：Subagents，一个 claude 变成五个

事情从这里开始真的不一样了。

一个 claude code 会话一次只能做一件事。让它写功能、review 代码、修 bug、写文档——只能一件件来，做到第四件事时，上下文早就乱了。

Subagents 把工作拆开。不是一个疲于奔命的 claude，而是一支各有专责的团队，每个人有自己的上下文，只盯一件事。

我的配置用了五个 agent：

- **architect**——负责高层设计决策，写需求文档，规划实现方案。从不直接碰代码
- **coder**——按照 architect 的方案写代码，拥有完整的工具权限
- **reviewer**——以安全优先的视角审查每个 PR，标问题，提改进，查测试覆盖率
- **tester**——写测试、跑测试，执行 TDD，配合 tdd-guard 确保没有测试的代码不能上线
- **ops**——负责部署、CI/CD、基础设施，监控构建，处理失败

每个 agent 有自己的 CLAUDE.md，有各自的指令、工具权限和上下文边界。coder 看不到部署配置，reviewer 不写代码，职责清晰。

想用现成的 agent 集合：

> https://github.com/wshobson/agents——25k+ stars，覆盖策略、开发、安全、设计的生产级 subagents

> https://github.com/davepoon/claude-code-subagents-collection——100+ agents，任何工作流都能直接用

---

## 第五层：Hooks 和 Slash 命令，把重复的事情交出去

每次你发现自己第三次在打同一段指令，那就是一个 slash 命令该出现的地方。

我每天在用的几个：

> /fix-issue 456——读取 github issue，建分支，写带测试的修复，开 PR。一条命令搞定原本要 10 分钟的流程。

> https://github.com/claude-commands/command-fix-issue

> /review——对当前 PR 触发 reviewer agent，做安全检查、测试覆盖率分析和代码质量评分

> /deploy staging——通过 ops agent 跑完整个部署流水线

57 个生产就绪命令的完整合集：

> https://github.com/wshobson/commands——1.7k+ stars，15 个工作流 + 42 个工具

Hooks 更进一步，在特定时机自动触发，不需要你手动：

> **pre-commit hook**——tdd-guard 在提交通过前检查测试是否存在并通过

> **session start hook**——从 obsidian 加载记忆，读最近的会话日志，把上下文预热好

> **pre-push hook**——代码推到远端之前，安全审查自动跑一遍

你不再需要每次提醒 claude 遵守哪些规则了，因为规则自己会执行。

---

## 第六层：编排，让 agents 在你睡觉时工作

这是最后一块。把每月 20 美元，变成真的像有一支开发团队的感觉。

claude-squad 是一个专门为并行跑多个 AI agent 设计的终端复用器。每个 agent 通过 git worktrees 拥有自己的独立工作区，各自在不同分支上工作，互不干扰。

```
brew install claude-squad
cs
```

就这两步。你得到一个 TUI 界面，可以启动、监控、暂停、恢复 agent。关掉终端，它们照跑不误。早上起来，已经完成的 pull request 在等你。

> https://github.com/smtg-ai/claude-squad

![Image](images/img-02.jpg)

**我的夜间流程**

睡前打开 claude-squad，启动三个会话：

- agent 1："修复仓库里所有标了 'bug' 的 issue"
- agent 2："给 /apps/api/src/services/ 补上缺失的测试"
- agent 3："把 dashboard 组件重构成用新的 design tokens"

信任的任务开自动接受模式（cs -y），有风险的切换到计划模式。

关上电脑，去睡觉。

早上：三个 PR 等着 review，每个都在自己的分支上，没有冲突，测试都过了。

想要更高阶的编排方案：

> https://github.com/ruvnet/claude-flow——11.4k+ stars，企业级多 agent 编排，带持久记忆

---

## 算一下，这套东西要多少钱

所有东西一起跑起来的成本：

```
layer 1: CLAUDE.md              — 免费（一个文件而已）
layer 2: obsidian + claude-mem  — 免费（obsidian 免费，仓库开源）
layer 3: superpowers + skills   — 免费（全开源，MIT 许可）
layer 4: subagents              — 免费（markdown 文件）
layer 5: hooks + commands       — 免费（全开源）
layer 6: claude-squad           — 免费（开源）

total infrastructure cost: $0

claude code subscription: $20/mo (pro plan)
```

这张单子上所有东西都是开源的。唯一要付钱的，是 claude 的订阅本身。

回报差距根本不是一个级别的。我追踪了配置前后两周的生产力：

![Image](images/img-03.jpg)

**之前 vs 之后**

每天浪费的那 47 分钟没了。但更重要的事情是：那些我以前下午三点才能做的事，agents 现在凌晨三点就做完了。

---

## 从哪里开始

不用今天就把 6 层全搭完。

先从这三个开始，一个下午就够了：

![Image](images/img-04.jpg)

**一个下午能搭好的配置**

这套东西，我花了 3 个月才摸索出来。

你一个下午就能搭好。

你现在的 claude code 配置是什么样的？

关注 [@regent0x_](https://x.com/@regent0x_)，持续研究和分享最新内容。

感谢阅读，别忘了收藏。
