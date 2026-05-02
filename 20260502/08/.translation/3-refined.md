# 21件大多数 Claude 用户从未设置的东西——每周就这么白白浪费好几个小时

**作者：** Anatoli Kopadze ([@AnatoliKopadze](https://x.com/AnatoliKopadze))  
**日期：** 2026年5月1日  
**来源：** [21 Things Most Claude Users Have Never Set Up](https://x.com/Zephyr_hg/status/2050225292585607440)

一个 CLAUDE.md 文件，刚刚以 82,000 个 star、7,800 次 fork，登上了 GitHub 趋势榜第一。

大多数 Claude 用户从来没听说过它。少数听说过的，也不知道该往里写什么。

就这么一个差距，每周在让人们白白浪费好几个小时。

每次你打开一个新的 Claude 会话，它都从零开始。它不知道你是谁，不知道你在做什么，不知道你喜欢怎么工作。你得花几分钟重新交代背景——或者你懒得交代，然后 Claude 给你的东西根本不对味。CLAUDE.md 能一次性解决这个问题。

## 为什么这件事跟每个人都有关，不只是开发者

大多数人以为 CLAUDE.md 是个开发者工具。不是的。它是一个指令文件，Claude 每次开新会话时都会自动读取——不管你用 Claude 做什么，只要你是经常用的人，都适用。

作家用它锁定自己的腔调，让 Claude 写出来的东西不会像别人的风格。营销人员用它定义受众，让 Claude 不再写那种放之四海皆准的烂文案。研究员用它规定信息的组织方式。企业主用它把公司背景一次性告诉 Claude，让每次输出都贴合实际。

没有 CLAUDE.md，你每次会话都从头来。重复解释同样的事，纠正同样的毛病，把同样的偏好说了一百遍。

CLAUDE.md 是你在认真用 Claude 做任何事之前，第一个应该搭起来的东西。

## 怎么创建这个文件——两分钟搞定

1. 打开你的项目文件夹，新建一个文件，命名为"CLAUDE.md"——全部大写，中间没有空格。它就是一个普通的纯文本文件，扩展名是 .md。
2. 用任何文本编辑器打开它——记事本、TextEdit、VS Code，随便哪个都行。把你的指令直接粘贴进去，纯文本就好。
3. 从这篇文章里挑跟你相关的指令，粘贴进去。不用全部 21 条，先挑 3 到 4 条，优先解决你现在最头疼的问题。
4. 保存文件。之后每次你在这个文件夹里开新会话，Claude Code 都会自动读取它。不需要任何额外设置，第一条消息就生效。

## Claude 怎么跟你说话

### 1 — 去掉废话开头

Claude 默认每次回复都以"太好的问题了！""当然！""没问题！""绝对可以！"开头——这些话什么都没说，只是在浪费你的时间。每天用好几个小时的话，这种摩擦累积起来很可观。

一条指令就能永久消灭它。每次回复直接从答案开始，没有热场，没有表演热情，要什么给什么。

```
Never open responses with filler phrases like "Great question!", "Of course!", "Certainly!", "Absolutely!", "Sure!", or similar warmups.

Start every response with the actual answer.
No preamble, no acknowledgment of the question.
Just the information.
```

### 2 — 动手之前先给选项

Claude 默认自己选一个方向就冲了。你让它改一段，它把整篇的语气都改了。你让它重新整理一份文档，它按照它自己的逻辑重组，跟你的思路完全不是一回事。然后你得去纠正一个你根本没让它动的地方。

这条指令改变这个模式。每次做比较重要的任务之前，Claude 先给你列出 2 到 3 种做法，你选方向，然后它再动手。接下来做出来的，才是你真正想要的。

```
2. Always show options before acting.
...
```

### 3 — 不确定就说不确定

Claude 会给你一个听起来很有把握、细节很丰富、但完全错误的答案，然后才承认自己不确定。它习惯用"听上去很像那么回事"的内容来填补自己知识的空白——日期、数据、引用、事实，感觉没毛病，但可能根本对不上。你拿去用了，问题在最不应该出问题的时候才冒出来。

这一条指令把这个行为掰过来。Claude 在回答之前先标出不确定的地方，而不是把它藏在自信满满的回复里。开头一句"我对这点不太确定"，能让你避免在一个靠不住的基础上继续往下建。

```
If you are uncertain about any fact, statistic, date, quote, or piece of information, say so explicitly before including it.

"I'm not certain about this" is always better than presenting a guess as a fact.

Never fill gaps in your knowledge with plausible-sounding information.
When in doubt, say so.
```

### 4 — 长短跟着任务走

问 Claude 一个简单问题，它写了四段话。让它写一个复杂的东西，它给你一个看起来完整、实则骨架的东西。两种都没用。回复的长短应该跟任务实际要求一致——简单的就简短，需要深度的就展开。

这条指令把这件事对齐。简单问题不再有填充，需要真材实料的工作不再给你交差了事的轻描淡写。

```
Match response length to task complexity.

Simple questions get direct, short answers.
Complex tasks get full, detailed responses.

Never compress or summarize work that requires real depth.
Never pad responses with restatements of the question or closing sentences that repeat what you just said.
```

## Claude 的行为方式

### 5 — 大改之前先问

你让 Claude 修一段，它把整篇文档都重写了。你让它删短点，它把你需要的部分也删掉了。你让它调一下语气，它顺带把结构也动了。每次你都在失去一些你不想失去的东西，然后不得不从记忆或者旧版本里把它找回来。

这条指令让每次大改动都变成一个确认节点。Claude 先停下来，告诉你它准备改什么、为什么要改，等你点头了才动。你同意的，才是接下来会发生的。

```
Before making any change that significantly alters content I've already created (rewriting sections, removing paragraphs, restructuring the flow, changing tone), stop completely.

Describe exactly what you're about to change and why.
Wait for my confirmation before proceeding.

"I think this would be better" is not permission to change it.
```

### 6 — 只做被要求的事

让 Claude 修一处，它会顺手"优化"另外五处——调你的措辞，重排你的结构，把你本来挺满意的句子重新写一遍。有时候这些变化是进步，更多时候不是。然后你得翻遍整个输出，才能搞清楚到底哪里变了。

这条指令让 Claude 只做它被要求做的。修要求改的，其他地方一个字不动。如果它发现别的地方有问题，可以说——但不能碰，除非你开口。

```
Only change what I specifically asked you to change.

Do not rewrite, rephrase, restructure, or "improve" anything I didn't ask about, even if you think it would be better.

If you notice something that could be improved elsewhere, mention it at the end of your response.
Do not touch it unless I explicitly ask you to.
```

### 7 — 改完之后告诉我改了什么

Claude 完成任务，你开始扫输出，想搞清楚哪里跟之前不一样了。哪几段变了？它删了什么吗？加了你没让它加的东西吗？没有摘要，你每次都得手动做 diff。

这条指令让 Claude 每次完成任务后附上一个简短交代：改了什么、没动什么、有什么需要你留意的。你的工作始终在你自己手里。

```
After completing any editing or writing task, always end with a brief summary:
- What was changed: [description]
- What was left untouched: [if relevant]
- What needs my attention: [anything requiring a decision or review]

Keep it short. This is a status update, not a recap of everything you just did.
```

### 8 — 没有我的确认，别替我做任何事

AI 工具越来越深入——接入邮件、日历、社交账号、文档。接入的越多，Claude 在你没完全意识到的情况下替你做了什么事的风险就越大。发消息、发帖子、分享文档、安排日程——这些动作有真实的后果，而且发生得很快。

这条指令划了一条红线。不管 Claude 觉得你想要什么，任何涉及外部后果的动作，都必须你在那一条消息里明确说"是"，才能执行。

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

## 你的背景

### 9 — 告诉 Claude 你是谁、你懂什么

Claude 不知道你是专家还是新手，是创始人还是自由职业者，是需要技术细节还是白话解释的人。没有这些信息，它只能猜——猜对猜错的概率差不多各占一半。有时它给你解释你早就知道了好几年的东西，有时它跳过你真正需要的背景。

一段说清楚你是谁的话，能让它对准你。从那以后，它说话的方式就是对着你说的，而不是对着一个陌生人。

```
About me:
- Name: [Your Name]
- Role: [what you do, writer, founder, marketer, researcher, etc.]
- Background: [relevant experience or knowledge level]
- Strong in: [topics or areas you know well, skip the basics here]
- Still learning: [areas where you need more context and explanation]

Adjust the depth of every response to match this background. Never over-explain what I already know. Never skip context I need.
```

### 10 — 告诉 Claude 你在做什么

每次开新会话，Claude 不知道你在做什么项目，不知道是给谁做的，不知道什么是真正重要的。它只能给你通用答案，因为它别无选择。它不了解你的受众，不知道你的目标，也不清楚塑造你每个决定的那些约束。

写一段简短的项目背景，一切就不一样了。建议开始贴合你的实际情况，Claude 知道它在为谁写，什么语气合适，什么取舍对你来说是真正重要的。

```
What I'm working on:
- Project: [one sentence description of what this is]
- Goal: [what success looks like]
- Audience: [who this is for and what they care about]
- Tone: [how the writing or output should feel, casual, professional, direct, conversational, etc.]
- What to avoid: [anything that doesn't fit, jargon, certain topics, specific styles]

Apply this context to every task. When something doesn't fit this picture, flag it before proceeding.
```

### 11 — 锁定你的声音和风格

Claude 有它自己的默认写法。还过得去，但那不是你的风格。它有自己惯用的短语，有自己的句子结构，语气也跟你实际说话的方式对不上。每次用 Claude 写东西，你都要花时间把它改回你自己的腔调。

在 CLAUDE.md 里定义一次你的风格，Claude 从第一稿就按那个写。改稿的时间少了，输出听起来真的像你写的。

```
My writing style, always match this:
- Voice: [e.g. direct, conversational, confident, no-fluff]
- Sentence length: [e.g. short and punchy / long and detailed / mixed]
- Words I use: [phrases or vocabulary that sound like me]
- Words I never use: [words or phrases that don't fit my style]
- Format preference: [e.g. paragraphs only / bullet points / headers / no headers]

When writing anything on my behalf, match this style exactly. Do not default to your own patterns.
```

## 记忆与连续性

### 12 — 让 Claude 维护一个记忆文件

Claude 每次会话之间什么都不记得，每次对话都是重新开始。但 Claude 能写文件，文件会留下来。这条指令让 Claude 维护一个 MEMORY.md，把你们一起做过的每个重要决定都记在里面：决定了什么、为什么、考虑过哪些方案最后没选。

每次开新会话，Claude 先读那个文件。它突然知道你两个月前为什么做了那个选择，不会再建议你已经试过的东西，而是在你之前的决定基础上继续往前走，而不是跟它们反着来。

```
Maintain a file called MEMORY.md. After any significant decision, about direction, format, content, approach, or strategy, add an entry:

## [Date], [Decision]
**What was decided:** [the choice made]
**Why:** [the reasoning]
**What was rejected:** [alternatives considered and why they were ruled out]

Read MEMORY.md at the start of every session before doing anything. Never contradict a logged decision without flagging it first.
```

### 13 — 会话结束摘要：不要每次都从头想起来你在哪里

你关掉窗口，两天后回来，花 15 分钟翻旧消息，想想清楚你上次做到哪里、完成了什么、还有什么没做完。这是一种完全可以避免的浪费，几乎每个经常用 Claude 的人都遇到过。

这条指令让 Claude 在你结束会话之前把摘要写进 MEMORY.md。下次打开，背景完整，你从上次停的地方接着来，不需要重建任何东西。

```
When I say "session end", "wrapping up", or "let's stop here", write a session summary to MEMORY.md:

## Session Summary, [Date]
**Worked on:** [what we focused on]
**Completed:** [what's finished]
**In progress:** [what's started but not done]
**Decisions made:** [key choices from this session]
**Next session:** [what to pick up first and any important context to carry forward]
```

### 14 — 记下走不通的路，不要每次都从头摸索

你为一段内容试了一种方法，折腾了四遍才得到能用的东西。三周后回来做类似的任务，Claude 从同样的烂建议重新开始。一样的试错，一样的时间浪费，从零起步。

错误日志断开这个循环。每条走不通的路都记下来——试了什么，为什么不行，最后什么有效。下次 Claude 先查日志，直接跳到已知有用的做法。

```
Maintain a file called ERRORS.md. When an approach takes more than 2 attempts to work, log it:

## [Task type or description]
**What didn't work:** [approaches that failed and why]
**What worked:** [the approach that finally succeeded]
**Note for next time:** [anything worth remembering for similar tasks]

Check ERRORS.md before suggesting approaches to tasks similar to logged ones. If a task matches a logged failure, say so and skip to what worked.
```

### 15 — 给 Claude 一份永远成立的事实清单

每个项目都有一些固定的事实：来自过去决定的约束，有重要原因存在的规则，不管做什么任务都始终成立的东西。没有这条指令，Claude 不知道这些事实存在，会随手建议跟它们冲突的东西，把你有理由做出的决定推翻，或者让你第一百次停下来解释同样的背景。

这个部分给 Claude 一个永久的底座，适用于每次会话、每项任务、每个输出。你不用再重复自己，Claude 在你真实的现实里工作，而不是一个通用的模板版本。

```
These facts are always true. Apply them to every session and every task without exception:

- [Permanent fact #1, e.g. "My audience does not have a technical background"]
- [Permanent fact #2, e.g. "All content must be appropriate for a professional context"]
- [Permanent fact #3, e.g. "We never make claims without a source"]
- [Permanent fact #4, e.g. "The brand voice is always warm, never corporate"]

If any task conflicts with one of these, flag it before proceeding. Do not work around a constraint without telling me.
```

## 面向开发者

下面这些指令是专门给用 Claude Code 写代码、审代码或者管理代码库的人准备的。如果你不是，上面那些就够用了。如果你是，这六条规则决定了 Claude 到底是个趁手的工具，还是在你代码库里到处乱来的麻烦。

### 16 — 只在被要求的范围内动

让 Claude 修一个 bug，它会顺手重构三个文件，重命名你的变量，重整你的 import，把你用了好几个月的代码"优化"一遍——全程不问你一句。有些改动会出问题，有些会引入细微差异，要花好几天才能追到根源。

这是用 Claude Code 的人最该记住的规则之一。管住范围，才是精确工具和在代码库里乱来之间的区别。

```
Only modify files, functions, and lines of code directly and specifically related to the current task.

Do not refactor, rename, reorganize, reformat, or "improve" anything I did not explicitly ask you to change.

If you notice something worth fixing elsewhere, mention it in a note.
Do not touch it. Ever.
```

### 17 — 任何破坏性操作之前先确认

Claude Code 跑在你的终端里，可以访问你的文件系统。它会毫不犹豫地删文件、覆盖函数、清掉数据库表——因为你让它做了，哪怕你自己没完全搞清楚你在让它做什么。指令被误读，几个小时的工作就消失了，没有撤销。

这条规则把每次破坏性操作变成确认节点。Claude 先停下来，列出会受影响的内容，等你明确说"是"之后才动。

```
Before deleting any file, overwriting existing code, dropping database records, removing dependencies, or making any change that cannot be trivially undone, stop completely. List exactly what will be affected. Ask for explicit confirmation. Only proceed after I say yes in the current message.
```

### 18 — 红线操作：没有明确许可，绝对不碰

部署到生产环境。在线上数据库跑迁移。向外部服务发 API 调用。这些不是"小心一点"的情况，而是你必须清醒地坐在那里、主动说"我同意"的动作。这条规则在这些操作周围拉起一道永久的防线。

```
The following actions require explicit in-session confirmation before executing, no exceptions:
- Deploying or pushing to any environment (staging, production, etc.)
- Running migrations or schema changes on any database
- Sending any email, message, or external API call
- Executing any command with irreversible external side effects

"You mentioned this earlier" is not confirmation. I must say yes in the current message.
```

### 19 — 锁定你的技术栈

没有明确的栈，Claude 会推荐它觉得最流行的框架、见过最多的库、它默认的包管理器。有时候正好合适，更多时候不是你用的、不是你团队熟悉的、跟你已有的东西不兼容。

把栈定义一次，Claude 就不再给你出不想要的建议。它写的所有东西都适配你真正在建的系统。

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

### 20 — 做完之后准确告诉我改了什么

Claude 完成任务，你开始扫输出，想搞清楚哪里不一样了。哪些文件动过了？有没有顺带改了别的？有没有留下什么没做完？没有文件级别的摘要，每次让 Claude 做事都得自己手动 diff。

```
After completing any coding task, always end with:
- Files changed: [list every file touched]
- What was modified: [one line per file]
- Files intentionally not touched: [if relevant]
- Follow-up needed: [anything requiring my attention or a decision]

Keep it short. This is a status update, not a recap.
```

### 21 — 让 Andrej Karpathy 的 CLAUDE.md 走红的 4 条规则

Andrej Karpathy，特斯拉前 AI 总监，OpenAI 创始成员，总结出了让 Claude Code 在编码任务中出问题的 4 种具体行为。有个开发者把它们提炼成 4 条指令，写进了一个 CLAUDE.md 文件。那个文件登上了 GitHub 趋势榜第一，把编码准确率从 65% 拉到了 94%。

这就是那 4 条规则。不管你的 CLAUDE.md 里还有什么，这几条都值得加上去。

```
1. Ask, don't assume. If something is unclear or underspecified, ask before writing a single line. Never make silent assumptions about intent, architecture, or requirements.

2. Simplest solution first. Always implement the simplest thing that could work. Do not add abstractions, layers, or flexibility that weren't explicitly requested.

3. Don't touch unrelated code. If a file or function is not directly part of the current task, do not modify it, even if you think it could be improved.

4. Flag uncertainty explicitly. If you are not confident about an approach, a library's behavior, or a technical detail, say so before proceeding. Confidence without certainty causes more damage than admitting a gap.
```

---

CLAUDE.md 不只是个开发者工具。任何认真用 Claude 的人，都应该在开始正式工作之前把它搭起来。

第 1 到 4 条，解决的是 Claude 说话的方式。第 5 到 8 条，阻止它在你没授权的情况下乱动东西。第 9 到 11 条，给它足够的背景，让它输出的东西真正贴合你的工作。第 12 到 15 条，给它目前能实现的最接近真实记忆的东西。第 16 到 21 条，是给想要 Claude Code 像一把趁手的工具、而不是一个让你提心吊胆的黑盒的开发者用的。

创建文件。先粘 3 条进去。用的过程中慢慢加。

关注 [@AnatoliKopadze](https://x.com/AnatoliKopadze)，获取更多真正能改变你和 AI 协作方式的方法。
