# 我是怎么用 Cursor 的

**作者：** lauren ([@poteto](https://x.com/poteto))  
**日期：** 2026年5月26日  
**来源：** [How I Use Cursor](https://x.com/poteto/status/2058975157503570132)

先坦白一件事：在我去 @cursor_ai 面试之前，我压根没碰过 Cursor。

那时候我在 Meta，眼看着 Claude Code 一路火起来。我自己也上头，掏了 200 美元一个月的个人套餐，拿来做业余项目。我喜欢它的简单，喜欢那种很快就能把活干起来、感觉自己挺能产出的劲头。要说唯一让我费劲的，是得自己一点点打磨一套 skills，把 cc 调成几乎我想要的任何样子。后来我甚至动手，在它上面做起了自己的 agent 编排工具。

面试是现场的，前后两天，我就用 Cursor 来做面试项目。那会儿 Cursor 3 还没出，所以我用的是编辑器窗口（Editor Window）。vscode 我用了很多年，快捷键大多还在手上，重新回到 IDE 倒不算难。不过说实话，头一两个小时，我是真有点想念 cli。改用鼠标点来点去，总觉得有点回到原始社会。但也有几件事，一下子就抓住了我。

第一件，是模型。我当时常用的 Opus 和 Codex，在 Cursor 里莫名就显得更聪明了。而且能随手切换模型，还能让它俩同时上，分头干活——Opus 写前端，Codex 管系统。面试前我本来就在到处安利"多模型互相挑刺地评审"，现在能在界面里原生地这么玩，顺手得不得了。更妙的是，还能派生不同模型的 subagent，一次对话里，两边的好处全占上了。

第二件，是压缩（compaction），快得离谱。用 cc 的时候，我早习惯了压缩要等上好几分钟，所以总得提着心盯着上下文和套餐还剩多少。结果到了 Cursor 里，它快到什么程度呢？我基本就不用再去看上下文用了多少了——它就是好使。而在 cc 里，模型一压缩完，我常常觉得它整个人都变迟钝了。

第三件，是我开始体会到，图形界面（GUI）能比纯命令行界面（TUI）多给你不少东西。能直接在 Cursor 自带的浏览器里打开你的 app，再用设计模式（Design Mode）顺手改设计，这事儿做起来特别自然。我也由此想到：要是有专门为这件事打造的界面，agent 写代码的效率，还能再上一个台阶。

## 用 Cursor 来做 Cursor

三月底入职到现在，我主要在做 Cursor 3 的 Agent Window，平时也拿它当主力。我还是觉得 cc 是个很酷的产品，团队也很棒。不过我慢慢发现一个有意思的现象：恰恰因为它够简单，大家反而忍不住想在外面再包一层自己的抽象。在我上一份工作里，几乎每周都能听到有人宣布，又搭了一个新的、基于 cc 的内部编排工具。

@bcherny 经常聊到一个挺老的概念，叫"潜在需求"（latent demand）：

> "产品圈里有个特别老的想法，叫潜在需求……你把产品做得能让人随便折腾，足够开放，开放到人们能拿它去干你没想过的事。然后你盯着看他们都怎么乱用，再照着那个去做。"

我一看，这不就是眼前这事吗。大家不约而同地都涌向编排工具，恰恰说明了一个潜在需求：你用 cli 的时候，其实是把你自己这个人，变成了那个在背后调度一切的人。

可问题是，我用过的那些 agent 工作流，劲儿全使错了地方。把一堆 CLI 塞进一个图形界面里跑，根本没说到点子上。我真正想琢磨的，是另一件事：怎么才能信得过这些 agent。

我从前当过工程经理，所以很快就回过味来——管 agent，跟带一支人类的工程团队，太像了。新人进来，得先 onboard，既要摸清代码库长什么样，也要弄明白这儿的活到底是怎么干的。而且他们入职时是带着本事来的，过去攒下的那些 skills 都在身上：怎么调试、怎么写出靠得住的代码和测试、怎么跟人沟通，等等。

agent 呢，就像是一个永远在失忆、又永远拎不太清的新人。你交代的话他转头就忘，也从来没真正学会过什么新东西。但好在，我们能给他配上规则、skills、工具，再加一份长期记忆，凑出个八九不离十的效果。他有本事，却也真笨，可关键是——他特别好教。所以我干脆把他每次掉链子的地方，都当成一个教学的机会，把我懂的那些"怎么把工程做深、做扎实"的门道，一样样塞给他。

道理也简单：一旦少了那份较真劲儿，agent 就会一味顺着你，怎么省事怎么来，硬把你要的代码给凑出来。而且天哪，它是真能写、也真敢写一大堆。你要是再粗手粗脚地让它并行，那也不过是让它更快地堆出一堆水货罢了。

> **lauren** [@poteto](https://x.com/poteto) · 4月26日
>
> 我越来越觉得，并行调度一大批 agent，真正的价值在走深，不在铺广。你应该挑一个、或者少数几个问题，往深里钻，这样拿到好结果的概率才最大：
>
> - 用 best of N 那种赛马的玩法，从一堆解里挑出最好的那个

## 想跑得快，得先扎得深

我是真信，agent 编排能做出名堂来。但有个前提：得深度优先。

所以我打算把 pstack 开源出来。这是我每天用来做 @cursor_ai 的那套个人 skills，外加一套工程原则。它最早的雏形，是我在业余项目里捣鼓出来的，之后就一直在打磨。

想要的话，从这儿拿：https://cursor.com/marketplace/cursor/pstack

```markdown
/add-plugin pstack
```

这套 skills 如今已经成了 Cursor 团队最常用的一批，所以这回能分享给大家，我挺高兴。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTgxMjJhMjA0YTA1N2ZmZjAyZGQ1Mzg4YzA2ZmU4NzBfMjg1MDQ3NTI4OTFhMzRlNTIyZjhlYTRhYzY0YTlmYTZfSUQ6NzY0Mzk5OTQ4NzQzODU4OTEyOV8xNzc5NzU3MzQwOjE3Nzk4NDM3NDBfVjM)

这是 Cursor 的公司排行榜。光这一周，我的 skills 就被调用了 9000 次！

pstack 干的事，是教 agent 借着多个模型，把活干得更较真。我把自己见过的各种"翻车现场"，一个个都做成了 skills。整个插件的核心，是 /poteto-mode——它是个高阶 skill，会看你要做什么任务，递给 agent 一套该照着走的 playbook（行动手册）。它的目标不是把代码写得越多越好，恰恰反过来：用最少的代码，干出最大的事。

那这份较真劲儿，是从哪儿来的？说穿了，就是让 agent 像一个有经验的工程师那样去想问题。拿调试来说吧，有个特别好用的办法，是把问题的范围当成一片空间，做二分查找：先列上几个"可能是这儿出毛病"的猜想，然后一个个系统地排除，慢慢逼近那个真正的根子。要是 bug 不好复现，你可以想法子人为地把它逼出来；或者加点埋点、打几行日志，趁程序跑着，瞅瞅它当时的状态。

这一串步骤连起来，就是一套 playbook。agent 照着它走，就能把问题真正查清楚，而不是上来就瞎猜——你要是放任不管，它可太乐意猜了。pstack 里自带了不少这样的 skills 和 playbook，让你能用同一股较真劲儿去做软件工程。眼下我手里的 playbook，覆盖这些事：

- Skill 的编写和评测（evals）
- 自主干活
- 修 bug，以及运行时的"现场取证"
- 开发新功能
- 还原视觉效果、快速做原型
- 还有更多

啥时候你想较个真，就在 prompt 前头加一句 /poteto-mode。比如：

```markdown
/poteto-mode 这个 pr 有个挺隐蔽的 bug，就算空闲着，滚动条也会每 750ms 漂一下。先复现，再修，修完验证。
/poteto-mode 一个大列表加载要花一两秒，可我们明明做了虚拟化。跑个 cpu trace，告诉我到底卡在哪。
/poteto-mode 在一个 feature flag 后面做个小功能。做完验证它是真能用。
/poteto-mode 做两个 markdown 渲染器的原型，方便我俩对比。每个都派一个 agent 去做。
/poteto-mode 把这些 skills 做成插件开源出去。内部的东西一点都别漏，在临时目录里干活，先把依赖图给我看。
/poteto-mode 我去睡了。就算 ci 抽风，也把这一摞改动给我落地。我想早上一睁眼，全都合并好了。
/poteto-mode 这个 flag 一开，行间距就太高。第二张图才是对的。复现、修，一直修到跟它对上为止。
```

要是需要，你也可以单独点用其他几个 skills：

- **/how：** 想让人给你讲讲，某个子系统到底是怎么转起来的。
- **/why：** 想搞清楚，某个东西当初为什么是这么做的。它会用上你手头的 MCP，分头并行去翻每一类线索（版本控制、问题跟踪、长文档、实时聊天、基础设施监控、错误跟踪、数据分析仓库）。
- **/architect：** 你马上要动手写一段跨越函数边界的代码，想先把类型和数据结构定下来。
- **/arena：** 想对同一件事并行试 N 回，再从每一回里挑出最妙的那部分。
- **/interrogate：** 想让几个不同的模型，互相挑着刺地把某个东西评审一遍。
- **/tdd：** 你在修 bug。先写一个注定会失败的测试，再动手修。
- **/unslop：** 你在收拾各种 AI 写出来的东西。让它们好好说人话。
- **/reflect：** 一场长对话之后，想让你的 skills 接着往上长一截。
- **/figure-it-out：** 在干点不太寻常的事？给这个任务现设计一套较真、又能事后查账的 playbook。
- **/show-me-your-work：** 想要一条能复查的决策轨迹。它会把每个决定都记进一个你能直接提交的 tsv 文件里。

最后还有个 /automate-me，能帮你做一个专属于你自己的 mode skill。它会把你最近的对话记录翻一遍，照着你平时干活的路数，给你起草一个 your-mode skill，底下再悄悄接到 pstack 上。

pstack 配哪种 agent 编程工具都能用，不过在 Cursor 这类多模型工具里，它格外灵。很多 skills 本身就用上了多模型的玩法，专挑每个模型的长处用、绕开它的短板。说到底，这还是 agent 编排，只不过走的是深度优先，不是广度优先。

agent 真正卡脖子的地方，是验证。它能飞快地写出一大堆代码，可要确认这堆东西真的全都对，那才叫难。等哪天你真把这一关过了，真正的 agent 并行——就像一座专门造软件的"暗工厂"（dark factory，意思是没人盯着、全自动运转的工厂）——说不定就成真了。

但路得一步步走：先扎深，先较真。我觉得，往那个方向走的办法，就是一点一点地，把信任调上去。

去试试 pstack，回头告诉我你的感觉。

## 禅与软件维护的艺术

有了这套 skills，我写代码时心里踏实多了。可话说回来，现在代码全是 agent 在写，维护这事儿反倒成了一桩头疼事。Bug、性能问题、新功能的需求，照样得一件件慢慢啃。更要命的是，这些活儿现在还多了好几倍！

在 Cursor，我特别爱用它的自动化（automations）。这些是一批跑在云端的 agent，可以定时让它们干活，也可以让它们听见动静就动——比如 Slack 频道里冒出来一条新消息。我的机器人 Benny 就是这么个例子，我把 pstack 里那套 skills，原封不动也给了他一份。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTM0ZTQwOWU2MDlhZDUyZDkyZTgyODcwOThmNTQ2NDlfZGRlMGIzODE0NDVhYmYzNTExMDUwNGM4ZDU3MTY4Y2RfSUQ6NzY0Mzk5OTQ5NjcxMjI0NDQzM18xNzc5NzU3MzQwOjE3Nzk4NDM3NDBfVjM)

Benny 的几副不同面孔

Benny 还在打磨,但我心里的设想是：把软件维护这一整条流程，能自动化的都自动化掉。思路是这样的——既然我们现在已经有底气，靠 pstack 基本能"一把搞定"问题，而且对 PR 的质量也挺有把握，那"收反馈"这一环，照理说也能交给机器去做。

这座工厂的头一道工序，是分流（triage）：从同事那儿把 bug 报告的信息收上来。我们自己天天用 Cursor，所以每出一个发布候选版本，同事们就会扔过来一堆反馈。Benny 能看懂图片和视频附件，会用 pstack 的 skills 去把代码库摸一遍；要是复现步骤说得不清不楚，他还会回头找报告的人聊几句，把话问明白。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWVkZDc3MmM0ZWNjNmNjMzQ2YTFjNTVjZGQ3NGI2NzRfMWRhMWVhY2IxMGY1ZjQ5Y2RmMDdiN2I4ZWU2MTNlNmJfSUQ6NzY0Mzk5OTUwNDA2NDc5MzgxNV8xNzc5NzU3MzQwOjE3Nzk4NDM3NDBfVjM)

Benny 在追问更多细节

别小看这一步，它是整个 bug 报告流程里很关键的一环。没有清楚的复现步骤，也没搞明白到底哪儿坏了，agent 就只能闭着眼瞎猜该怎么修。我们得让他清清楚楚地知道：问题出在哪、又是怎么坏的。

分流一做完，Benny 就动手建一个工单，把他查到的东西全填进去：他翻过代码，翻过最近 bug 回归的 git 历史，翻过 Slack 上别人提到同一个 bug 的消息，甚至连 Notion 上"这个功能本该怎么运作"的设计和产品决策都翻了——为的就是搞清一件事：这到底是个 bug，还是人家当初就设计成这样的？

工单一提交，又有另一个 Benny 机器人接手，用的是我做的另一个 skill，叫 /orchestrate。

> **Cursor** [@cursor_ai](https://x.com/cursor_ai) · 5月8日
>
> 给大家介绍一下 /orchestrate：一个会递归派生 agent、靠 Cursor SDK 去啃你最有野心的那些任务的 skill。
>
> 我们已经拿它来：
> - 自动研究我们的内部 skills，token 用量砍掉 20%，评测分还更高了
> - 把内部后端的冷启动时间，砍掉了 80%

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjViODI4M2I2OTAyZGExZDJiM2JiN2IwOGUwZWIyZWNfZThlMzliNjIwNmM3NGE4YjJlZTg4YzNkM2I1MGNhMDlfSUQ6NzY0Mzk5OTUxMjQ1NzUxNDE2NF8xNzc5NzU3MzQwOjE3Nzk4NDM3NDBfVjM)

他干的第一件事，是用"计算机使用"（computer use）去试着把问题复现出来。Cursor 的云端 Agent，能在云里头跑起一个 Cursor 本体，在那儿操作桌面、点按钮、敲键盘。这背后又用上了我做的另一批 skills——靠 CDP 这类协议（或者别的等效手段），用程序去操控我们自家的产品。

这么一来，这个 bug 报告到底复不复现得出来，我们就能当场演示。要是它真能稳定地复现，他就接着试着去修。碰上性能问题，Benny 还能把修复前后的 CPU trace 和堆快照都拍下来。子规划器（subplanner）会再派出一批 worker，用 pstack 的 skills 去验证这个修复，再对着工单核一遍：到底修好没。

同一轮里还会另派几个 worker，去录一段修复前后的对比视频；最后由一个 worker 出面开 PR、送去评审，描述里就把那段视频附上。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODVlZjc3MzM1Y2I0NjE3MmJlZGYzMzE1ZDYzYzk0ZmRfZTJjMjk3MTI1OTI2ODBkNDkxOGNkZDFmZTI0ODFhNjFfSUQ6NzY0Mzk5OTUxOTM2MTUzNTE1NF8xNzc5NzU3MzQwOjE3Nzk4NDM3NDBfVjM)

最近一次成功复现、并修好的运行记录

这一切都还在路上，要做的事多着呢。但一想到能有这么一支 agent 团队，在我睡觉、或者忙别的时候，踏踏实实地替我修 bug，我就挺来劲。怎么让代码评审也跟着规模化，是另一个大方向——我估摸着，Cursor 接下来会有几个挺酷的功能来帮上忙。

不过说到底，想建起一座属于你自己的"软件工厂"，最要紧的还是那两个字：信任。除非你能信得过一个 agent，让它把一个问题从头管到尾——连验证都一并兜住——否则你那套流程，根本自动化不起来。而当你用上 pstack 这类插件，给 agent 添上更多工程上的深度，把信任一格一格地往上调，你就能开始去啃那些更有野心的问题了。反过来，对那些你还信不过的 agent 硬上并行，那纯属白烧 token，还顺手往你的代码库里又塞了一堆水货。

谢谢你读到这儿！
