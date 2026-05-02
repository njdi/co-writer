# 21件大多数Claude用户从未设置的事情——这正在每周耗费他们数小时

**作者：** Anatoli Kopadze ([@AnatoliKopadze](https://x.com/AnatoliKopadze))  
**日期：** 2026年5月1日  
**来源：** [21 Things Most Claude Users Have Never Set Up](https://x.com/Zephyr_hg/status/2050225292585607440)

一个单独的CLAUDE.md文件刚刚以82,000个星标和7,800个分叉登上GitHub趋势榜第一名。

大多数使用Claude的人从来没有听说过它。听说过的人也不知道实际上该在里面写什么。

这个差距每周都在让人们浪费数小时。

每次你打开一个新的Claude会话，它都从零内存开始。它不知道你的名字、你的工作、你的偏好，或者你喜欢事情怎么做。你花几分钟重新解释一切，或者你不解释，Claude给你的东西不符合你实际的工作方式。CLAUDE.md永久性地解决了这个问题。

## 为什么这对每个人都很重要——不只是开发者

大多数人认为CLAUDE.md是一个开发者工具。它不是。它是一个Claude在每次会话开始时自动读取的指令文件——它对任何定期使用Claude的人都有效。

作家用它来锁定他们的声音和语气，这样Claude就不会听起来像别人。营销人员用它来定义他们的受众，这样Claude就停止写通用的文案。研究人员用它来设定他们想要信息结构化的方式。企业主用它来给Claude提供他们公司的完整背景，这样每个输出都符合他们的实际情况。

没有CLAUDE.md，你每次会话都从零开始。你重复自己。你纠正同样的错误。你第一百次解释你的偏好。

CLAUDE.md是你在与Claude进行任何严肃工作之前应该设置的第一件事，无论你用它做什么。

## 如何创建文件——只需2分钟

1. 打开你的项目文件夹，创建一个新文件。将其命名为"CLAUDE.md"——大写字母，没有空格。它只是一个带有.md扩展名的纯文本文件。
2. 在任何文本编辑器中打开它——记事本、TextEdit、VS Code，无论你使用什么。你将直接将你的指令粘贴到这个纯文本文件中。
3. 从这篇文章中复制与你相关的指令。粘贴进去。你不需要全部21条，先从解决你最大困扰的3或4条开始。
4. 保存文件。Claude Code每次你在该文件夹中打开会话时都会自动读取它。不需要设置，没有额外步骤——它从第一条消息就开始工作。

## Claude如何与你交流

### 1 — 消灭填充词

Claude的默认设置是用"太好的问题了！"、"当然！"、"肯定！"、"绝对！"开始每个回复——这些短语什么都没有增加，只是浪费你的时间。当你每天使用Claude数小时时，这种摩擦会累积。

一条指令永久消灭它。每个回复都直接从答案开始。没有预热，没有有帮助的表演——只有你立即要求的东西。

```
Never open responses with filler phrases like "Great question!", "Of course!", "Certainly!", "Absolutely!", "Sure!", or similar warmups.

Start every response with the actual answer.
No preamble, no acknowledgment of the question.
Just the information.
```

### 2 — 行动前总是展示选项

Claude默认选择一种方法并执行。你让它重写一段，它改变了整篇文章的语气。你让它重新构建一个文档，它以一种不符合你思维方式的方式重新组织。现在你在纠正一个你没有要求更改的东西。

这条指令完全改变了这种动态。在任何重要任务之前，Claude向你展示2-3种可以处理工作的方式。你选择合适的方向。接下来发生的正是你实际想要的。

```
2. Always show options before acting.
...
```

### 3 — 不知道时要诚实

Claude会给你一个自信、详细、完全错误的答案，然后才承认不确定性。它用听起来合理的信息填补空白——日期、统计数据、引用、事实——感觉是真实的但不是。你使用这些信息，问题在它最重要的时候出现。

这一条指令改变了这种行为。Claude在回答之前标记不确定性，而不是将其隐藏在自信的回复中。回复顶部的"我对此不确定"可以让你避免在一个不存在的基础上建造。

```
If you are uncertain about any fact, statistic, date, quote, or piece of information, say so explicitly before including it.

"I'm not certain about this" is always better than presenting a guess as a fact.

Never fill gaps in your knowledge with plausible-sounding information.
When in doubt, say so.
```

### 4 — 让长度符合实际需要

问Claude一个简单的问题，它写四段话。让它写一些复杂的东西，它给你一个看起来完整但实际上不是的骨架。两者都没用。回复长度应该符合任务实际要求——答案短时就短，工作需要深度时就详细。

这条指令校准了这种关系。简单问题不再有填充，需要真实内容的工作不再有浅薄的输出。

```
Match response length to task complexity.

Simple questions get direct, short answers.
Complex tasks get full, detailed responses.

Never compress or summarize work that requires real depth.
Never pad responses with restatements of the question or closing sentences that repeat what you just said.
```

## Claude的行为方式

### 5 — 在做大改动之前先问

你让Claude修复一段，它重写了整个文档。你让它缩短某些内容，它删除了你需要的部分。你让它调整语气，它也改变了结构。每次，你都失去了一些你不想失去的东西，并且不得不从记忆或早期版本中重建它。

这条指令将每个重大更改变成一个检查点。Claude停止，准确告诉你它将要做什么，并在触及任何东西之前等待你的同意。接下来的工作是你同意的工作。

```
Before making any change that significantly alters content I've already created (rewriting sections, removing paragraphs, restructuring the flow, changing tone), stop completely.

Describe exactly what you're about to change and why.
Wait for my confirmation before proceeding.

"I think this would be better" is not permission to change it.
```

### 6 — 专注于被要求的事情

让Claude修复一件事，它会在里面"改善"其他五件事——调整你的措辞，重新组织你的结构，重新表述你满意的句子。有时候这些变化是改进。通常不是。现在你必须梳理所有内容才能找到实际上改变了什么。

这条指令让Claude保持在任务上。修复被要求的。让其他所有内容保持原样。如果其他地方有值得处理的内容，提到它——但不要在未被要求的情况下触碰它。

```
Only change what I specifically asked you to change.

Do not rewrite, rephrase, restructure, or "improve" anything I didn't ask about, even if you think it would be better.

If you notice something that could be improved elsewhere, mention it at the end of your response.
Do not touch it unless I explicitly ask you to.
```

### 7 — 总是告诉我你改变了什么

Claude完成一项任务，你发现自己在扫描输出，试图弄清楚什么与你之前的不同。哪些部分改变了？它删掉了什么吗？它添加了你没有要求的东西吗？没有摘要，你每次都在手动比对差异。

这条指令让Claude在每个任务结束时附上简短摘要：改变了什么，保持不变的，以及需要你注意的任何事情。你对自己的工作保持控制。

```
After completing any editing or writing task, always end with a brief summary:
- What was changed: [description]
- What was left untouched: [if relevant]
- What needs my attention: [anything requiring a decision or review]

Keep it short. This is a status update, not a recap of everything you just did.
```

### 8 — 未经询问绝不代表我采取行动

随着AI工具变得更加互联——接入你的邮件、日历、社交账号、文档——Claude在每一次新集成中采取你并未完全预期的行动的风险都在增加。发送消息。发布内容。分享文档。安排事项。这些行动有真实的后果，它们发生得很快。

这条指令创建了一道硬墙。无论Claude认为你想要什么，任何具有外部后果的行动都不会在你在那个特定时刻明确说是的情况下发生。

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

### 9 — 告诉Claude你是谁以及你知道什么

Claude不知道你是专家还是初学者，是创始人还是自由职业者，是需要技术深度还是简单语言的人。没有这种背景，它会猜测——而且它猜对和猜错的频率一样高。有时它解释你早已知道多年的事情。有时它跳过你实际需要的背景。

一段关于你是谁的描述会校准Claude从那时起给你的每个回复。它停止像对陌生人一样对待你，开始像对真正了解你的人一样与你交谈。

```
About me:
- Name: [Your Name]
- Role: [what you do, writer, founder, marketer, researcher, etc.]
- Background: [relevant experience or knowledge level]
- Strong in: [topics or areas you know well, skip the basics here]
- Still learning: [areas where you need more context and explanation]

Adjust the depth of every response to match this background. Never over-explain what I already know. Never skip context I need.
```

### 10 — 给Claude提供你正在做什么的背景

每次会话，Claude都不知道你在做什么，是为谁做的，或者什么是真正重要的。它给你通用输出因为它别无选择。它不知道你的受众。它不知道你的目标。它不知道塑造你每个决定的约束条件。

一段简短的背景段落改变了一切。建议不再是通用的，而是开始符合你的实际情况。Claude知道它为谁写作，什么语气是正确的，以及什么权衡对你具体来说是重要的。

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

Claude有一种默认的写作风格。它还不错。但它也不是你的。它使用某些短语，以特定方式构建句子，语气不符合你实际的沟通方式。每次你使用Claude写东西，你最终都会把它编辑回你的声音。

在CLAUDE.md中定义一次你的声音，Claude从第一稿就以它写作。更少的编辑。更多实际听起来像你的输出。

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

### 12 — 让Claude保持一个记忆文件

Claude在会话之间忘记一切。每次对话都重新开始。但Claude可以写文件，文件会持久存在。这条指令告诉Claude维护一个MEMORY.md文件，记录你们一起做出的每个重要决定：决定了什么，为什么，以及考虑过和拒绝了哪些替代方案。

在每次会话开始时，Claude读取那个文件。突然间它知道了你两个月前做出那些选择的原因。它停止重新建议你已经尝试过的东西。它在你的决定基础上构建，而不是与它们矛盾。

```
Maintain a file called MEMORY.md. After any significant decision, about direction, format, content, approach, or strategy, add an entry:

## [Date], [Decision]
**What was decided:** [the choice made]
**Why:** [the reasoning]
**What was rejected:** [alternatives considered and why they were ruled out]

Read MEMORY.md at the start of every session before doing anything. Never contradict a logged decision without flagging it first.
```

### 13 — 会话结束摘要：永不丢失进度

你关闭会话。两天后你回来。你花15分钟阅读旧消息，试图记住你在哪里，你完成了什么，以及你在做什么的中途。这是一种完全可以避免的浪费，几乎每个定期使用Claude的人都会遇到。

这条指令让Claude在你结束之前将会话摘要写入MEMORY.md。下一次会话以完整背景打开。你从上次离开的地方继续，无需从头重建任何东西。

```
When I say "session end", "wrapping up", or "let's stop here", write a session summary to MEMORY.md:

## Session Summary, [Date]
**Worked on:** [what we focused on]
**Completed:** [what's finished]
**In progress:** [what's started but not done]
**Decisions made:** [key choices from this session]
**Next session:** [what to pick up first and any important context to carry forward]
```

### 14 — 记录不起作用的东西：停止两次解决同一个问题

你为一段内容尝试一种提示方法。需要四次尝试才能得到可用的东西。三周后你回来处理类似任务，Claude从同样的糟糕建议重新开始。同样的试错，同样的时间浪费，从头开始。

错误日志打破了这个循环。每种失败的方法都被记录——你尝试了什么，为什么不起作用，最终什么起了作用。下次Claude首先检查日志，直接跳到已知有效的方法。

```
Maintain a file called ERRORS.md. When an approach takes more than 2 attempts to work, log it:

## [Task type or description]
**What didn't work:** [approaches that failed and why]
**What worked:** [the approach that finally succeeded]
**Note for next time:** [anything worth remembering for similar tasks]

Check ERRORS.md before suggesting approaches to tasks similar to logged ones. If a task matches a logged failure, say so and skip to what worked.
```

### 15 — 给Claude一个永不改变的事实列表

每个项目都有永久性事实：来自过去决定的约束，因为重要原因而存在的规则，无论具体任务如何都对你的工作始终成立的事情。没有这条指令，Claude不知道这些事实存在，并且会随意建议与它们相矛盾的事情，撤销你有理由做的工作，或者要求你停下来第一百次解释同样的背景。

这个块给Claude提供了一个永久性基础，适用于每次会话、每个任务、每个输出。你停止重复自己。Claude在你的实际现实中运作，而不是其通用版本。

```
These facts are always true. Apply them to every session and every task without exception:

- [Permanent fact #1, e.g. "My audience does not have a technical background"]
- [Permanent fact #2, e.g. "All content must be appropriate for a professional context"]
- [Permanent fact #3, e.g. "We never make claims without a source"]
- [Permanent fact #4, e.g. "The brand voice is always warm, never corporate"]

If any task conflicts with one of these, flag it before proceeding. Do not work around a constraint without telling me.
```

## 面向开发者

以下指令专门针对使用Claude Code编写、审查或管理代码的人。如果那不是你，以上所有内容就足够了。如果是，这六条规则是Claude成为有用的编码助手和代码库中的失控炮之间的区别。

### 16 — 保持范围：不要触碰你未被要求的任何东西

让Claude修复一个bug，它会重构三个文件，重命名你的变量，重新组织你的导入，并"改进"你已经使用了几个月的代码——所有这些都不问。其中一些更改会破坏东西。有些会引入需要数天才能追踪到的微妙差异。

这是任何使用Claude Code的人最重要的规则之一。范围控制是精确工具和代码库中失控炮之间的区别。

```
Only modify files, functions, and lines of code directly and specifically related to the current task.

Do not refactor, rename, reorganize, reformat, or "improve" anything I did not explicitly ask you to change.

If you notice something worth fixing elsewhere, mention it in a note.
Do not touch it. Ever.
```

### 17 — 任何破坏性操作之前先确认

Claude Code在你的终端中运行，可以访问你的文件系统。它会毫不犹豫地删除文件、覆盖函数和删除数据库表——因为你告诉它这样做，即使你没有完全意识到你在告诉它什么。一条误读的指令，几小时的工作就消失了，没有撤销。

这条规则将每个破坏性行动变成一个检查点。Claude停止，准确显示将受影响的内容，并在触及任何东西之前等待你的明确同意。

```
Before deleting any file, overwriting existing code, dropping database records, removing dependencies, or making any change that cannot be trivially undone, stop completely. List exactly what will be affected. Ask for explicit confirmation. Only proceed after I say yes in the current message.
```

### 18 — 硬性停止：没有明确许可就绝不发生的行动

部署到生产环境。在实时数据库上运行迁移。向外部服务发送API调用。这些不是"小心"的情况——它们是完全停止，要求你有意识地在场并故意说是。这条规则在这些行动周围创建了一道永久的墙。

```
The following actions require explicit in-session confirmation before executing, no exceptions:
- Deploying or pushing to any environment (staging, production, etc.)
- Running migrations or schema changes on any database
- Sending any email, message, or external API call
- Executing any command with irreversible external side effects

"You mentioned this earlier" is not confirmation. I must say yes in the current message.
```

### 19 — 锁定你的技术栈

没有定义的栈，Claude会建议它认为最流行的任何框架，它见过最多的任何库，以及它默认的任何包管理器。有时还好。通常不是你使用的，不是你的团队了解的，与你已经构建的不兼容。

定义一次栈，Claude就停止建议你不想要的东西。它写的所有内容都适合你实际构建的系统。

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

### 20 — 总是准确显示改变了什么

Claude完成一项任务，你发现自己在扫描输出，试图弄清楚什么不同了。哪些文件改变了？它触碰了其他任何东西吗？它留下了什么未完成的吗？没有文件级摘要，每次你让Claude做任何事情都在手动比对差异。

```
After completing any coding task, always end with:
- Files changed: [list every file touched]
- What was modified: [one line per file]
- Files intentionally not touched: [if relevant]
- Follow-up needed: [anything requiring my attention or a decision]

Keep it short. This is a status update, not a recap.
```

### 21 — 让Andrej Karpathy的CLAUDE.md走红的4条规则

Andrej Karpathy，特斯拉前AI总监，OpenAI创始成员，识别出了使Claude Code在编码任务中失败的4种具体行为。一位开发者将它们提炼成一个单一CLAUDE.md文件中的4条指令。那个文件登上了GitHub趋势榜第一名，将编码准确率从65%提高到94%。

这就是那4条规则。无论其中还有什么，它们都值得添加到每个开发者的CLAUDE.md中。

```
1. Ask, don't assume. If something is unclear or underspecified, ask before writing a single line. Never make silent assumptions about intent, architecture, or requirements.

2. Simplest solution first. Always implement the simplest thing that could work. Do not add abstractions, layers, or flexibility that weren't explicitly requested.

3. Don't touch unrelated code. If a file or function is not directly part of the current task, do not modify it, even if you think it could be improved.

4. Flag uncertainty explicitly. If you are not confident about an approach, a library's behavior, or a technical detail, say so before proceeding. Confidence without certainty causes more damage than admitting a gap.
```

---

CLAUDE.md不只是一个开发者工具。它是一个任何认真使用Claude的人都应该在第一次真正会话之前设置的永久指令文件。

指令1-4修复了Claude的通信方式。指令5-8阻止它更改你未授权的事情。指令9-11给它提供了背景，以产生符合你实际工作的输出。指令12-15给它提供了目前存在的最接近真实记忆的东西。指令16-21适合希望Claude Code像精确工具而不是不可预测的工具一样运作的开发者。

创建文件。粘贴3条指令。随着你的使用添加更多。

关注[@AnatoliKopadze](https://x.com/AnatoliKopadze)获取更多实际改变你与AI工作方式的系统。
