# 帮我翻了10倍效率的 CLAUDE.md（完整文件附上）

**作者：** darkzodchi ([@zodchiii](https://x.com/zodchiii))  
**日期：** 2026年4月27日  
**来源：** [The CLAUDE.md File That 10x'd My Output (Full File Included)](https://x.com/Zephyr_hg/status/2048683276194185640)

每次 Claude Code 会话，Claude 做的第一件事就是读一个文件：CLAUDE.md。在你敲第一句 prompt 之前，在任何代码之前，在任何事情发生之前，Claude 就已经把这个文件读完了，并把它当作整个会话的最终依据。

大多数人要么根本没有这个文件，要么写了 300 行人设类指令。

一个好的 CLAUDE.md 和一个烂的 CLAUDE.md，差距就像：给高级工程师一份清晰的上手文档，vs 把新人扔进没有任何文档的代码库。

以下是怎么写一个真正管用的 CLAUDE.md👇

正文开始前，我每天在 Telegram 频道分享 AI 和 vibe coding 的笔记：https://t.me/zodchixquant🧠

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Yjk5MTY5NmZlNTUwZDI0OTAxNjc0MGU5YTUwOTk4MTdfYTNkZDIyMDQzOWViNzAxOTcxMjY4ZjYyYTAzZmYzZDRfSUQ6NzYzMzQwMjA5OTE2MTk0Mjk4N18xNzc3Mjg5OTQxOjE3NzczNzYzNDFfVjM)

## 为什么大多数 CLAUDE.md 都没用

三个原因：

**太长了。** 模型能稳定遵循大约 150-200 条指令。Claude Code 的系统提示本身已经占了约 50 条。也就是说，你的 CLAUDE.md 能用的空间大概只有 100-150 条。文件超过 200 行？Claude 漏掉你的规则不是故意的。

**内容写错了。** 大多数人在 CLAUDE.md 里塞的，都是 Claude 自己就能搞定的事。比如"你是一个高级工程师"、"逐步思考"之类的人设指令。或者改变不了 Claude 行为的泛泛建议。每一行没办法阻止具体错误的指令，都是在浪费位置。

**没有分层。** CLAUDE.md 不是唯一能放指令的地方。一共有三层，大多数人却把所有东西都塞进同一个文件：

```
~/.claude/CLAUDE.md       → Global (every project)
.claude/CLAUDE.md         → Project (shared with team, in git)  
./CLAUDE.local.md         → Local (personal overrides, gitignored)
```

全局层放每个项目都通用的规则。项目层放团队需要知道的技术栈信息。本地层放你自己的个人偏好。

三层都用起来，每个文件自然就短了，也聚焦了。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjYzNGI3Nzg0OTQ5YzM2ODAyNTUwZDk5ZTI2YzM0MjlfZDBmNGVjYmM3NWVmOTU1NTE1ZTUzZWNmMDE3ZWU3YTBfSUQ6NzYzMzQwMjExMjcyNjEyNTUyNV8xNzc3Mjg5OTQxOjE3NzczNzYzNDFfVjM)

## 真正重要的 5 个部分

我翻遍了来自开源项目、Anthropic 官方文档和社区最佳实践库的几十份生产级 CLAUDE.md，所有有效的文件都覆盖了这 5 件事：

### 1. 关键命令

Claude 不知道怎么构建、测试或 lint 你的项目——告诉它。

```
## Commands
- Build: `npm run build`
- Dev: `npm run dev`  
- Test single file: `npm test -- path/to/file`
- Lint + fix: `npm run lint:fix`
- Type check: `npx tsc --noEmit`
```

简短具体。Claude 直接跑这些，不用猜。没有这一节，你的项目明明用的是 `pnpm vitest`，Claude 却会去跑 `npm test`，然后花 3 轮调试一个根本跑不起来的命令。

### 2. 架构地图

每次会话，Claude 对你的代码库一无所知。给它一张地图。

```
## Architecture  
- src/lib/services/ → all business logic
- src/components/ → stateless UI components only
- src/lib/store/ → global state (Zustand)
- src/app/api/ → API routes, no business logic here
- Database access only through Server Actions or API routes
```

不需要完整的目录树，只要让 Claude 知道各模块在哪、各类代码放哪就够了。

### 3. 硬性规则（少了你，Claude 必然出错的地方）

这是最重要的部分。每一条规则都应该能回答这个问题："删掉这行，Claude 会犯错吗？"

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

两点值得注意：
1. 禁止类规则和要求类规则同样重要（"永远不要提交 .env"）
2. IMPORTANT 这类强调词真的有用。

Anthropic 官方文档明确指出，加上"IMPORTANT"或"YOU MUST"可以提高 Claude 的遵守率。

这个部分控制在 15 条以内。

### 4. 工作流偏好

你希望 Claude 怎么干活？这一节专门解决"你只要求改一行，Claude 把整个文件重写了"的问题。

```
## Workflow
- Ask clarifying questions before starting complex tasks
- Make minimal changes, don't refactor unrelated code
- Run tests after every change, fix failures before moving on
- Create separate commits per logical change, not one giant commit
- When unsure between two approaches, explain both and let me choose
```

### 5. 不该写什么

留白同样重要：

```
## Don't include:
- Personality instructions ("be a senior engineer")
- Code formatting rules your linter already handles  
- @-imports that embed entire docs into every session
- Duplicate rules (if global says "run tests," project doesn't repeat it)
- Anything Claude will learn on its own via auto memory
```

自动记忆这个功能被严重低估了。Claude 会在 `~/.claude/projects/<project>/memory/` 里维护自己的笔记。运行 `/memory` 可以看它已经记住了你项目的哪些东西。

Claude 跑一次会话就能自己搞清楚的事，别浪费 CLAUDE.md 的行数。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTNmYTdlNGU0Yjc5NWMzZTI5NjA4MDYxZTNlYzRiNDZfYmVkM2ZkYmQ1ODRmN2M3NjliNjU5ZWI1ZTJlNDQ0MDNfSUQ6NzYzMzQwMjExODQ4OTY4OTAxOF8xNzc3Mjg5OTQxOjE3NzczNzYzNDFfVjM)

## 完整模板（直接拿去用）

下面是一份拿来就能用的 CLAUDE.md，不超过 60 行，该有的都有，不该有的一行没有。

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

不适用的部分直接删掉。

## 真正起作用的几行

测试了几十份 CLAUDE.md 配置之后，这几行对输出质量影响最大：

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

每一条都在阻止一个具体的、高频的错误。

这也是判断 CLAUDE.md 里每一行的标准：删掉它，Claude 会出错吗？

## 大家都在犯的错

大家都把 CLAUDE.md 当愿望清单在写。

CLAUDE.md 应该是一份技术简报，不是励志演讲。技术栈、命令、架构、规则、工作流。其他一切都是噪音，会把 Claude 的注意力从真正重要的指令上分走。

控制在 80 行以内。Claude 出错了就回来改它。

这个文件的价值会随时间累积。第一个月写好 CLAUDE.md，你就不用一遍遍重复同样的要求了。

到第六个月，它已经记录下 Claude 在这个项目里犯过的所有错误，并自动把它们全挡住了。

我每天在 Telegram 频道分享 AI、金融和 vibe coding 的笔记：https://t.me/zodchixquant

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzNjZjZiOGVlNDgxYWQwNThmZjdiZWQ5ZWQ1ZGFkOTVfYWY4MWM5NGZiMWVmNDg5MWRkYjgwMjU4MjI3ZmVmMmVfSUQ6NzYzMzQwMjEyNzM4MTM1MTM4NV8xNzc3Mjg5OTQxOjE3NzczNzYzNDFfVjM)
