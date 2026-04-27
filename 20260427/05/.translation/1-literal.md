# 那个让我产出提升10倍的CLAUDE.md文件（完整文件附上）

**作者：** darkzodchi ([@zodchiii](https://x.com/zodchiii))  
**日期：** 2026年4月27日  
**来源：** [The CLAUDE.md File That 10x'd My Output (Full File Included)](https://x.com/Zephyr_hg/status/2048683276194185640)

每次Claude Code会话都从读取一个文件开始：CLAUDE.md。在你的第一个提示之前，在任何代码之前，在任何事情发生之前，Claude读取这个文件，并在整个会话中将其视为绝对真实。

大多数人要么没有这个文件，要么他们的文件是300行的个性指令。

一个好的CLAUDE.md和一个坏的CLAUDE.md之间的区别，就像是给高级工程师提供清晰简报来入职，和把新员工扔进没有文档的代码库之间的区别。

以下是如何写一个真正有效的CLAUDE.md👇

在我们深入之前，我在Telegram频道每天分享AI和vibe coding的笔记：https://t.me/zodchixquant🧠

![Image](images/img-01.jpg)

## 为什么大多数CLAUDE.md文件不起作用

三个原因：

**太长了。** 模型能可靠地遵循大约150-200条指令。Claude Code的系统提示已经包含了大约50条。这意味着你的CLAUDE.md在Claude开始遗漏东西之前可能只有100-150条指令的空间。如果你的文件超过200行，Claude并不是故意忽略你的规则。

**内容错误。** 大多数人在CLAUDE.md中填写了Claude自己就能弄清楚的东西。像"做一个高级工程师"或"逐步思考"这样的个性指令。不改变Claude行为的泛泛建议。每一行不能防止特定错误的指令都是浪费的指令。

**没有层次结构。** CLAUDE.md不是唯一放置指令的地方。有三个级别，大多数人把所有东西都堆在一个文件里：

```
~/.claude/CLAUDE.md       → Global (every project)
.claude/CLAUDE.md         → Project (shared with team, in git)  
./CLAUDE.local.md         → Local (personal overrides, gitignored)
```

全局适用于你在每个项目中都会重复的规则。项目适用于你的团队需要的特定技术栈上下文。本地适用于你的个人习惯。

使用全部三个可以使每个文件保持简短和专注。

![Image](images/img-02.jpg)

## 真正重要的5个部分

在查看了来自开源项目、Anthropic自己的文档和社区最佳实践仓库的数十个生产级CLAUDE.md文件之后，每个有效的文件都涵盖了这5件事：

### 1. 关键命令

Claude不知道如何构建、测试或检查你的项目 = 告诉它。

```
## Commands
- Build: `npm run build`
- Dev: `npm run dev`  
- Test single file: `npm test -- path/to/file`
- Lint + fix: `npm run lint:fix`
- Type check: `npx tsc --noEmit`
```

简短且具体。Claude运行这些而不是猜测。没有这个部分，当你的项目使用`pnpm vitest`时Claude会尝试`npm test`，浪费3轮调试一个永远不会工作的命令。

### 2. 架构地图

Claude每次会话都从对你的代码库零知识开始。给它一张地图。

```
## Architecture  
- src/lib/services/ → all business logic
- src/components/ → stateless UI components only
- src/lib/store/ → global state (Zustand)
- src/app/api/ → API routes, no business logic here
- Database access only through Server Actions or API routes
```

不是完整的目录列表。只要足够让Claude知道东西在哪里和什么放在哪里。

### 3. 硬性规则（没有你Claude会出错的事情）

这是最重要的部分。这里的每条规则都应该回答这个问题："删除这一行会导致Claude犯错吗？"

```
## Rules
- NEVER commit .env files or secrets
- All async calls must use try/catch
- Use functional components only, no class components
- Prefix commits: feat:, fix:, docs:, refactor:
- All PRs must pass `npm run verify` before merge
- Static export only, no SSR (deployed to S3)
- IMPORTANT: run type check after every code change
```

两件事要注意：
1. 负面规则和正面规则同样重要（"永远不要提交.env"）
2. 像IMPORTANT这样的强调标记实际上是有效的。

Anthropic自己的文档确认，添加"IMPORTANT"或"YOU MUST"可以提高遵守程度。

这个部分保持在15条规则以内。

### 4. 工作流偏好

你希望Claude如何工作？这可以防止"你要求一行修复时Claude重写了你整个文件"的问题。

```
## Workflow
- Ask clarifying questions before starting complex tasks
- Make minimal changes, don't refactor unrelated code
- Run tests after every change, fix failures before moving on
- Create separate commits per logical change, not one giant commit
- When unsure between two approaches, explain both and let me choose
```

### 5. 不应该包含什么

同样重要的是你省略的内容：

```
## Don't include:
- Personality instructions ("be a senior engineer")
- Code formatting rules your linter already handles  
- @-imports that embed entire docs into every session
- Duplicate rules (if global says "run tests," project doesn't repeat it)
- Anything Claude will learn on its own via auto memory
```

自动记忆在这里被低估了。Claude在`~/.claude/projects/<project>/memory/`维护自己的笔记。运行`/memory`查看Claude已经了解了你的项目什么。

不要在Claude经过一次会话就能弄清楚的事情上浪费CLAUDE.md的行数。

![Image](images/img-03.jpg)

## 完整模板（复制这个）

这是一个可以复制和调整的生产就绪CLAUDE.md。不超过60行。涵盖Claude需要的一切，没有它不需要的。

```markdown
# CLAUDE.md

## Project
[One line: what this project does and who uses it]

## Stack  
[Framework, language, database, deployment target]

## Commands
- Dev: `[command]`
- Build: `[command]`
- Test single: `[command] -- [path]`
- Test all: `[command]`
- Lint: `[command]`
- Type check: `[command]`

## Architecture
- [folder] → [what lives here]
- [folder] → [what lives here]
- [folder] → [what lives here]
- [file] → [what this file does]

## Rules
- [Rule that prevents a specific mistake]
- [Rule that prevents a specific mistake]
- [Rule that prevents a specific mistake]
- IMPORTANT: [The one rule Claude keeps breaking]

## Workflow
- [How you want Claude to approach tasks]
- [Commit conventions]
- [Testing expectations]
- [When to ask vs when to act]

## Out of scope
- [Things Claude should not touch]
- [Files that are manually maintained]
- [Integrations Claude shouldn't modify]
```

删除不适用的部分。

## 改变一切的规则

在测试了数十个CLAUDE.md配置之后，这些是对输出质量产生最大差异的行：

```
# The lines with highest impact:

- IMPORTANT: run type check after every code change
  (prevents Claude from shipping broken types)

- Make minimal changes, don't refactor unrelated code  
  (prevents Claude from rewriting your entire file)

- Create separate commits per logical change
  (prevents the 47-file monster commit)

- When unsure, explain both approaches and let me choose
  (prevents Claude from making architectural decisions for you)

- Static export only, no SSR
  (prevents Claude from adding server-side code to a static site)
```

这些中的每一个都防止了一个特定的、常见的错误。

这是你CLAUDE.md中每一行的测试标准：删除它会导致Claude做错误的事情吗？

## 每个人都会犯的错误

人们把CLAUDE.md当作愿望清单。

你的CLAUDE.md应该是一个技术简报，而不是励志演讲。技术栈、命令、架构、规则、工作流。其他一切都是噪音，和真正重要的指令争夺注意力。

保持在80行以内。当Claude出错时审查它。

这个文件随时间复利增长。第一个月一个好的CLAUDE.md可以让你免于重复自己。

到第六个月，它已经捕获了Claude在你的项目中犯过的每一个错误，并自动防止所有这些错误。

我在Telegram频道每天分享AI、金融和vibe coding的笔记：https://t.me/zodchixquant

![Image](images/img-04.jpg)
