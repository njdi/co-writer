# 用 Claude 这么久，你可能一直在做无用功

**作者：** Anatoli Kopadze ([@AnatoliKopadze](https://x.com/AnatoliKopadze))  
**日期：** 2026年5月1日  
**来源：** [21 Things Most Claude Users Have Never Set Up](https://x.com/Zephyr_hg/status/2050225292585607440)

最近有一个文件在 GitHub 上火了。

一个叫 CLAUDE.md 的文件，82,000 个 star，7,800 次 fork，直接冲上趋势榜第一。

大多数 Claude 用户根本没听说过它。少数听说过的，也不知道该往里面写什么。

就这么一个文件，一个差距，每周让无数人在不必要的重复上白白耗掉好几个小时。

事情是这样的：每次你打开一个新的 Claude 会话，它就重置了。它不知道你是谁，不知道你在做什么，不知道你有什么偏好。于是你花时间重新交代背景，或者你懒得交代，然后拿到的东西根本不对味。

CLAUDE.md 能一次性解决这个问题。

## 这不只是开发者的事

很多人一听到"配置文件"就觉得这是程序员的东西。其实不是。

CLAUDE.md 是一个普通的文本文件，你写好放在项目文件夹里，Claude 每次开新会话都会自动读一遍。不需要任何特殊设置，不需要懂代码，就这么一个文件。

写作的人用它锁定自己的文风，让 Claude 的输出不会听起来像别人写的。做营销的人用它定义受众，Claude 就不会再写那种放哪都能用的通用文案。做研究的人用它规定信息组织的方式。做生意的人用它一次性交代公司背景，让每次输出都贴合实际。

没有它的代价也很清楚：每次会话从头开始，重复解释同样的事，纠正同样的毛病，把同样的偏好说了一百遍，出来的东西还是差那么点意思。

## 两分钟建好这个文件

步骤很简单：

1. 打开你的项目文件夹，新建一个文件，命名为 `CLAUDE.md`——全部大写，没有空格，普通的纯文本文件。
2. 用你顺手的文本编辑器打开它，把你的指令直接粘进去就行。
3. 从这篇文章里挑几条跟你最相关的，粘进去。不用全部 21 条，先选 3 到 4 条，优先解决你现在最头疼的问题。
4. 保存。之后每次在这个文件夹开新会话，Claude Code 都会自动读取，第一条消息就生效。

接下来这 21 条，是具体能写进去的内容。

---

## Claude 怎么说话

### 1 — 去掉废话开头

你有没有注意到，Claude 几乎每次回复都用"太好的问题了！""当然！""没问题！"开头？

这些话什么信息都没有，只是一个仪式感的热场。每天用好几个小时的话，每次等它说完这段才进入正题，摩擦就这么慢慢积累起来。

一条指令就能把它永久关掉，直接从答案开始。

```
Never open responses with filler phrases like "Great question!", "Of course!", "Certainly!", "Absolutely!", "Sure!", or similar warmups.

Start every response with the actual answer.
No preamble, no acknowledgment of the question.
Just the information.
```

### 2 — 动手之前先给选项

Claude 默认的方式是自己选一个方向，然后冲出去。你让它改一段，它改了整篇的语气。你让它整理一份文档，它按它自己的逻辑重新排，跟你的思路完全两码事。然后你要花时间去纠正一个你根本没让它动的东西。

加上这条，它在每次做比较重要的任务之前，会先给你列出 2 到 3 种做法，你来选方向，它再动手。这样做出来的，才是你想要的。

```
2. Always show options before acting.
...
```

### 3 — 不确定的时候说不确定

Claude 有个习惯：宁可给你一个听起来很有把握的错误答案，也不愿意说"我不确定"。

它会用"听上去很像那回事"的内容来填补自己知识的空白——日期、数据、引用、事实，读起来没毛病，但可能根本站不住脚。你把它用出去了，问题在最不该出现的时候才冒出来。

加上这条，它在不确定的时候会先说清楚，而不是把不确定藏在自信满满的表达里。

```
If you are uncertain about any fact, statistic, date, quote, or piece of information, say so explicitly before including it.

"I'm not certain about this" is always better than presenting a guess as a fact.

Never fill gaps in your knowledge with plausible-sounding information.
When in doubt, say so.
```

### 4 — 长短跟着任务走

问个简单问题，Claude 写了四段话。让它做个复杂的东西，它给你一个看起来完整但实则骨架的东西。两种都不好用。

这条指令把这件事对齐：简单的问题给短回答，需要深度的任务给完整展开，不多也不少。

```
Match response length to task complexity.

Simple questions get direct, short answers.
Complex tasks get full, detailed responses.

Never compress or summarize work that requires real depth.
Never pad responses with restatements of the question or closing sentences that repeat what you just said.
```

---

## Claude 的行为边界

### 5 — 大改之前先确认

你让它修一段，它把整篇文档都重写了。你让它删短点，它把你需要的部分也顺手删了。你让它调个语气，它顺带把结构也动了。

每次你都在失去一些你不想失去的东西，然后得从旧版本里把它找回来。

这条指令把大的改动变成确认节点：Claude 先停下来，告诉你它准备改什么、为什么，等你点头，再动。

```
Before making any change that significantly alters content I've already created (rewriting sections, removing paragraphs, restructuring the flow, changing tone), stop completely.

Describe exactly what you're about to change and why.
Wait for my confirmation before proceeding.

"I think this would be better" is not permission to change it.
```

### 6 — 只做被要求的事

让它修一处，它顺手"优化"另外五处。调了你的措辞，重排了你的结构，把你本来挺满意的句子重新写了一遍。有时候这些改动是进步，更多时候不是。然后你得翻遍整个输出，才能搞清楚到底哪里变了。

这条让它只动被要求动的地方。如果它发现别的地方有问题，可以说——但不能碰，除非你主动让它碰。

```
Only change what I specifically asked you to change.

Do not rewrite, rephrase, restructure, or "improve" anything I didn't ask about, even if you think it would be better.

If you notice something that could be improved elsewhere, mention it at the end of your response.
Do not touch it unless I explicitly ask you to.
```

### 7 — 改完之后交代清楚

Claude 做完事，你开始扫输出，想搞清楚哪里跟之前不一样了。哪几段变了？删了什么没有？加了你没让它加的东西吗？没有摘要，你每次都得自己做 diff。

加上这条，它在每次完成任务后附上一个简短交代：改了什么、没动什么、有什么需要你决定的。

```
After completing any editing or writing task, always end with a brief summary:
- What was changed: [description]
- What was left untouched: [if relevant]
- What needs my attention: [anything requiring a decision or review]

Keep it short. This is a status update, not a recap of everything you just did.
```

### 8 — 没有我的明确确认，别替我做任何事

Claude 接入的东西越来越多——邮件、日历、社交账号、各种文档。接入越多，它在你没完全意识到的情况下帮你"做了件事"的风险就越大。发消息、发帖子、分享文档、安排日程，这些都有真实的后果，而且发生得很快。

这条指令划了一条红线：不管 Claude 觉得你想要什么，任何涉及外部后果的动作，都必须你在那一条消息里明确说"是"，才能执行。

```
Never send, post, publish, share, or schedule anything on my behalf without my explicit confirmation in the current message.

This includes:
- Emails
- Social posts
- Calendar invites
- Document shares
- Any action that affects something outside this conversation

"You mentioned wanting to do this" is not confirmation.
I must say yes in the current message.
```

---

## 让 Claude 了解你

### 9 — 告诉它你是谁、你懂什么

Claude 不知道你是专家还是新手，需要技术细节还是白话解释。没有这些，它只能猜——猜对猜错差不多各一半。有时给你解释你早就知道好几年的东西，有时又跳过你真正需要的背景。

写一段说清楚你是谁，它就知道该怎么跟你说话，而不是对着一个陌生人。

```
About me:
- Name: [Your Name]
- Role: [what you do, writer, founder, marketer, researcher, etc.]
- Background: [relevant experience or knowledge level]
- Strong in: [topics or areas you know well, skip the basics here]
- Still learning: [areas where you need more context and explanation]

Adjust the depth of every response to match this background. Never over-explain what I already know. Never skip context I need.
```

### 10 — 告诉它你在做什么

每次开新会话，Claude 不知道你在做什么项目，不知道是给谁做的，不知道什么东西是真正重要的。于是它只能给你通用答案。它不了解你的受众，不知道你的目标，也不清楚那些塑造你每个决定的约束。

一段简短的项目背景，能让它的建议从通用变成贴合你的实际情况。

```
What I'm working on:
- Project: [one sentence description of what this is]
- Goal: [what success looks like]
- Audience: [who this is for and what they care about]
- Tone: [how the writing or output should feel, casual, professional, direct, conversational, etc.]
- What to avoid: [anything that doesn't fit, jargon, certain topics, specific styles]

Apply this context to every task. When something doesn't fit this picture, flag it before proceeding.
```

### 11 — 锁定你的风格

Claude 有自己的默认写法，还过得去，但那不是你的腔调。它有它惯用的短语，有它自己的句式，语气也跟你说话的方式对不上。每次用它写东西，你都要花时间把它改回你自己的味道。

把你的风格在 CLAUDE.md 里定义一次，它从第一稿就按你的腔调写。改的少了，出来的东西更像你。

```
My writing style, always match this:
- Voice: [e.g. direct, conversational, confident, no-fluff]
- Sentence length: [e.g. short and punchy / long and detailed / mixed]
- Words I use: [phrases or vocabulary that sound like me]
- Words I never use: [words or phrases that don't fit my style]
- Format preference: [e.g. paragraphs only / bullet points / headers / no headers]

When writing anything on my behalf, match this style exactly. Do not default to your own patterns.
```

---

## 给 Claude 一点记忆

### 12 — 让它维护一个记忆文件

Claude 每次会话之间什么都不记得。但它能写文件，文件会留下来。

这条指令让 Claude 维护一个 MEMORY.md，把你们一起做过的每个重要决定都记进去：决定了什么、为什么、考虑了哪些方案最后没选。每次开新会话先读它，它就知道你两个月前为什么做了那个选择，不会再给你建议你已经试过的东西。

```
Maintain a file called MEMORY.md. After any significant decision, about direction, format, content, approach, or strategy, add an entry:

## [Date], [Decision]
**What was decided:** [the choice made]
**Why:** [the reasoning]
**What was rejected:** [alternatives considered and why they were ruled out]

Read MEMORY.md at the start of every session before doing anything. Never contradict a logged decision without flagging it first.
```

### 13 — 结束会话前写一份摘要

你关掉窗口，两天后回来，花 15 分钟翻旧消息，想想清楚上次做到哪里了、完成了什么、还剩什么没做完。

这是一种完全可以避免的浪费。这条指令让 Claude 在你说"结束了"之前，把当次的进度写进 MEMORY.md。下次打开，直接接着来。

```
When I say "session end", "wrapping up", or "let's stop here", write a session summary to MEMORY.md:

## Session Summary, [Date]
**Worked on:** [what we focused on]
**Completed:** [what's finished]
**In progress:** [what's started but not done]
**Decisions made:** [key choices from this session]
**Next session:** [what to pick up first and any important context to carry forward]
```

### 14 — 记录走不通的路

你为一段内容试了一种方法，折腾了四遍才得到能用的东西。三周后回来做类似的任务，Claude 从同一批烂建议重新开始。一样的试错，一样的时间浪费。

这条指令建一个错误日志：每次某个方法超过两次才走通，就记下来——试了什么、为什么不行、最后什么有效。下次遇到类似的任务，先查日志，跳过已知的弯路。

```
Maintain a file called ERRORS.md. When an approach takes more than 2 attempts to work, log it:

## [Task type or description]
**What didn't work:** [approaches that failed and why]
**What worked:** [the approach that finally succeeded]
**Note for next time:** [anything worth remembering for similar tasks]

Check ERRORS.md before suggesting approaches to tasks similar to logged ones. If a task matches a logged failure, say so and skip to what worked.
```

### 15 — 给它一份永远成立的事实清单

每个项目都有一些固定不变的东西：来自过去决定的约束，有重要原因才存在的规则，不管做什么任务都成立的事实。

没有这条，Claude 不知道这些事情存在，会随手建议跟它们冲突的方向，把你有理由做出的决定推翻，或者让你第一百次停下来解释同样的背景。

```
These facts are always true. Apply them to every session and every task without exception:

- [Permanent fact #1, e.g. "My audience does not have a technical background"]
- [Permanent fact #2, e.g. "All content must be appropriate for a professional context"]
- [Permanent fact #3, e.g. "We never make claims without a source"]
- [Permanent fact #4, e.g. "The brand voice is always warm, never corporate"]

If any task conflicts with one of these, flag it before proceeding. Do not work around a constraint without telling me.
```

---

## 面向开发者的部分

下面这六条是专门给用 Claude Code 写代码、审代码或者管理代码库的人的。如果你不是，上面那些就够用了。如果你是，这几条决定了 Claude 到底是个趁手的工具，还是在代码库里到处乱来的麻烦。

### 16 — 只在被要求的范围内动

让 Claude 修一个 bug，它会顺手重构三个文件，重命名你的变量，重整你的 import，把你用了几个月的代码"优化"一遍——全程不问你。有些改动会出问题，有些引入的细微差异要好几天才能追到根源。

```
Only modify files, functions, and lines of code directly and specifically related to the current task.

Do not refactor, rename, reorganize, reformat, or "improve" anything I did not explicitly ask you to change.

If you notice something worth fixing elsewhere, mention it in a note.
Do not touch it. Ever.
```

### 17 — 破坏性操作之前先确认

Claude Code 跑在你的终端里，能访问你的文件系统。它会毫不犹豫地删文件、覆盖函数、清掉数据库表——因为你让它这样做了，哪怕你自己没完全搞清楚在让它做什么。指令被误读，几个小时的工作就消失了，没有撤销。

这条规则把每次破坏性操作变成一个确认节点：Claude 停下来，列出会受影响的内容，等你明确说"是"之后才动。

```
Before deleting any file, overwriting existing code, dropping database records, removing dependencies, or making any change that cannot be trivially undone, stop completely. List exactly what will be affected. Ask for explicit confirmation. Only proceed after I say yes in the current message.
```

### 18 — 红线操作：没有许可，绝对不碰

部署到生产环境。在线上数据库跑迁移。调用外部服务的 API。这些不是"小心一点"的情况，是你必须清醒地在场、主动说"我同意"才能执行的动作。

```
The following actions require explicit in-session confirmation before executing, no exceptions:
- Deploying or pushing to any environment (staging, production, etc.)
- Running migrations or schema changes on any database
- Sending any email, message, or external API call
- Executing any command with irreversible external side effects

"You mentioned this earlier" is not confirmation. I must say yes in the current message.
```

### 19 — 锁定你的技术栈

没有明确的栈，Claude 会推荐它觉得最流行的框架、见过最多的库、它自己默认的包管理器。有时候正好合适，更多时候不是你用的，也不是你团队熟悉的，还可能跟你已有的东西不兼容。

把栈定义一次，它就不再出这种建议了，写出来的所有东西都适配你真正在建的系统。

```
Tech stack, always use these, never suggest alternatives unless I ask:
- Language(s): [list]
- Framework(s): [list]
- Package manager: [npm / yarn / pip / cargo / etc.]
- Database: [list]
- Testing: [your testing framework]
- Linting / formatting: [your tools]

If something in the stack seems like the wrong tool, flag it, but use it anyway unless I say otherwise.
```

### 20 — 做完之后列清楚改了什么

Claude 完成任务，你开始扫输出，想搞清楚哪里不一样了。哪些文件动过了？有没有顺带改了别的？有没有留下什么没做完？没有文件级别的摘要，每次都得自己手动 diff。

```
After completing any coding task, always end with:
- Files changed: [list every file touched]
- What was modified: [one line per file]
- Files intentionally not touched: [if relevant]
- Follow-up needed: [anything requiring my attention or a decision]

Keep it short. This is a status update, not a recap.
```

### 21 — 让 Andrej Karpathy 的 CLAUDE.md 走红的 4 条规则

Andrej Karpathy，特斯拉前 AI 总监，OpenAI 创始成员，总结出了让 Claude Code 在编码任务上出问题的 4 种具体行为。有个开发者把它们提炼成 4 条指令，写进了一个 CLAUDE.md 文件。

那个文件登上 GitHub 趋势榜第一，编码准确率从 65% 涨到了 94%。

就这 4 条，不管你的 CLAUDE.md 里还有什么，都值得加进去：

```
1. Ask, don't assume. If something is unclear or underspecified, ask before writing a single line. Never make silent assumptions about intent, architecture, or requirements.

2. Simplest solution first. Always implement the simplest thing that could work. Do not add abstractions, layers, or flexibility that weren't explicitly requested.

3. Don't touch unrelated code. If a file or function is not directly part of the current task, do not modify it, even if you think it could be improved.

4. Flag uncertainty explicitly. If you are not confident about an approach, a library's behavior, or a technical detail, say so before proceeding. Confidence without certainty causes more damage than admitting a gap.
```

---

CLAUDE.md 不只是个开发者工具。任何认真用 Claude 的人，都应该在正式开始之前把它搭起来。

第 1 到 4 条，解决 Claude 说话的方式。第 5 到 8 条，阻止它在你没让它动的地方乱动。第 9 到 11 条，给它足够的背景，让输出真正贴合你的工作。第 12 到 15 条，给它目前能实现的最接近真实记忆的东西。第 16 到 21 条，给想让 Claude Code 像一把趁手的工具、而不是一个黑盒的开发者用。

建好文件，先粘 3 条进去，用的过程中慢慢加。

关注 [@AnatoliKopadze](https://x.com/AnatoliKopadze)，获取更多真正能改变你和 AI 协作方式的方法。
