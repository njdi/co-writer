# 为什么我们应该停止替AI智能体设计脚手架

**作者：** Kangwook Lee ([@Kangwook_Lee](https://x.com/Kangwook_Lee))  
**日期：** 2026年5月9日  
**来源：** [Why We Should Stop Designing Harnesses for AI Agents](https://x.com/Zephyr_hg/status/2052925157606568217)

*（如果你不熟悉"马与挽具的类比"，建议先读我最近的那篇文章）*

---

我们造AI智能体的人，有个习惯：替它把运行框架搭好。

循环怎么跑，工具怎么调，记忆怎么存，规划怎么展开——这些东西，过去几年一直是我们人类在设计。这套由人工精心打造的"脚手架"，叫做 harness，是让AI跑起来的那套支撑系统。

这件事我自己也做了很久。设计了好几个当时算得上前沿的框架，从聊天机器人到图像聚类，从游戏伴侣到代码助手。那段时间挺好玩的。

但我越来越觉得，这件事我们该停下来了。

---

## 先建一个思考模型

换个角度来看框架和AI的关系。

通常我们的思路是：AI模型定了，就去调框架，看哪种框架效果好。

我想反过来想：框架定了，让模型能力去变化。

这样一来，同一个框架对同一个任务，就会划出一条"能力门槛线"——高于这条线的模型能搞定，低于这条线的不行。

这条门槛线，我们记作 θ(h)，由框架 h 决定。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODRjZTI2ZjM5N2Q1MGJkZDM1MWU3NmQ3ZGFiMTBlYzNfN2QzZjliNjBiOGU5N2UwZTZiZjc3MzVkYjM3MTA0YTlfSUQ6NzYzODE3MTc5MzIxMTMxMzA4Ml8xNzc4NDAwNDY2OjE3Nzg0ODY4NjZfVjM)

---

## 框架好不好，只在中间那段有差别

两套框架放在一起比，就能看出意思了。

一套好框架（h_good），一套差框架（h_bad）。

好框架让任务更好上手，门槛低；差框架要求模型更聪明才能完成，门槛高。

两条门槛线一画，模型能力就被分成了三段。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGVkNTczY2U1MzMwNDg4NDUyOTAxZTZkODIzMjQ2ZDNfZTM5OTk0NDBhNzgzZDY4ZTQ4MjFjZGM3NDhiNGE3ODRfSUQ6NzYzODE3MTgwMzYzODEzOTg3N18xNzc4NDAwNDY2OjE3Nzg0ODY4NjZfVjM)

**第一段：** 能力太弱，不管用哪套框架都搞不定。

**第二段：** 能力中等，换个好框架就能搞定，换个差框架就不行。

**第三段：** 能力足够强，用什么框架都行。

你看，框架好不好，只在中间那段真正起作用。太弱的救不了，太强的不需要。只有中间这段，好框架才是决定性的。

我们把这套思路叫做"三段位框架"。

---

## 挽具这件事，马自己不会做，AI会

回到"马与挽具"的类比。

马和AI，有一个本质上的区别。

马没法给自己造挽具。AI可以。

于是问题就来了：人造的框架，和AI造的框架，哪个更好？

过去这几年，答案是人类这边：

```
h_good = h_human
h_bad  = h_ai
```

人手工设计的那套——智能体的循环方式、工具调用逻辑、记忆结构、规划脚手架——就是比AI自己鼓捣出来的更管用。"搭一个好智能体"，实际上等于"替它搭一套好框架"。

那时候，会做框架工程的人是稀缺资源。这也是我花了那么多精力在这件事上的原因。

---

## 但前提已经变了

AI越来越会写代码，越来越能调试，迭代系统越来越快。

慢慢地，在搭框架这件事上，它开始比我们做得更好。

局面就翻过来了：

```
h_good = h_ai
h_bad  = h_human
```

套回三段位框架，中间那段的含义变了。以前是"用好框架才能跑起来，好框架靠人造"，现在是"用好框架才能跑起来，好框架靠AI造"。

如果我们还在沿用人工设计的框架，处于中间段位的模型就始终发挥不出它真正的实力。

我们最近有一项研究，Meta Harness（由@yoonholeee主导），专门验证了这件事：在中等规模的模型上，AI自己迭代优化框架，效果已经超过了人工设计。

加一条时间轴来看全局——假设AI的代码能力随时间持续增长，你会得到这样一张二维相图：

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGIxYzJlMTU0MGI2ODM4MmFjMzQzZTA1YTZlYTAzMDlfYzlmOThmZWE3MWU1NGQ3MjY2ODFlNTJmOTFhM2ZhODVfSUQ6NzYzODE3MTgwOTU5MDA3MDIwOF8xNzc4NDAwNDY2OjE3Nzg0ODY4NjZfVjM)

图中"黄色区域"的出现，也给"被埋没的天才"假说提供了一种新解释：不是模型不够好，是我们用的框架拖了后腿。底层模型的潜力，一直被人工框架压着，没能真正浮出来。

---

## 所以，该退一步了

事情其实是这样的——

模型很强，框架好不好无所谓，随便跑；模型太弱，框架好不好也无所谓，怎么搭都救不了。

卡在中间这段的模型，才是真正的问题所在。它有能力，只是需要合适的支撑。而框架的质量，在这里是决定性的。

很长一段时间里，"合适的支撑"只能靠人来设计。

现在不一样了。

要让中间段位的模型真正跑出来，我们得从框架工程这件事上退一步，把空间还给AI自己。

让聪明的马自己造挽具。
