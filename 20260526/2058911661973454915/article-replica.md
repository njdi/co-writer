# 从零造一个大模型，到底要走哪五步：拆开 GPT 和 Claude 背后的完整流程

**作者：** Codez ([@0xCodez](https://x.com/0xCodez))  
**日期：** 2026年5月25日  
**来源：** [How to build your own LLM from scratch in 5 Stages: exact pipeline behind GPT and Claude](https://x.com/0xCodez/status/2058911661973454915)

我做了件事：把大语言模型到底是怎么造出来的，整个拆了开来。ChatGPT、Claude、Gemini 背后那一整条流水线，我把它压成了一张图。

你可以先收藏。读完之后，你会清楚地看到：从一堆原始的互联网文本，到一个能像助手一样跟你对话的模型，中间到底要走哪五步。

先把话说在前头——这不是标题党。大多数人都觉得，造一个大模型，关键在架构。可越往里看你越会发现，事情恰恰反过来：架构，是这五步里最不重要的一步。

## 先说一个几乎人人都信的误解

你随便找个人问：像 Claude 这样的模型是怎么来的？十有八九会答你一个词——"transformer"。好像那个秘密，就藏在神经网络怎么搭这件事上。

可惜不是。

transformer 这套架构，早就标准化了，论文也都公开发表着。各大实验室手里用的，其实是差不多的几块积木。你想想，要是架构真的是那道护城河，那大家手里岂不是早就人手一个 GPT-4 了？

这就有意思了。真正决定一个模型行不行的，是另外三样东西：数据、评估，还有系统。而不是在架构上修修补补。所以有句话我特别想让你记住——最好的模型，不是"训练"出来的，是"工程"出来的。

这份指南，就是顺着这个思路写的。一共五个阶段。架构呢，只占第一个阶段里的一小段。剩下那四步，才是模型真正分高下的地方。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGI4NGRkMzY0ZTk3ZGU3MWNhMTljOWZmNzExYjNhMjZfMjk3Zjc5ZjQ5MmU4NWE1MDllOTFhMWNjMTNlMmQzOGFfSUQ6NzY0NDAwMTA2NjE4MDU0NTcxNl8xNzc5NzU3NzE1OjE3Nzk4NDQxMTVfVjM)

## 第一步：预训练——先让模型学会"语言"本身

一切都从一个看起来简单到不像话的目标开始：预测下一个词。

听着平平无奇，对吧？给模型一串词，让它去猜接下来最可能出现的是哪个词——这就是所谓的自回归语言建模。

可奇妙的地方就在这儿。你让它在足够多的文本上，一遍一遍地这么猜，猜着猜着，它就把语法、事实、甚至推理的套路，全都吸收进去了。没有人专门教过它这些，它只是为了把"下一个词"猜得更准，不得不把这些本事都学会。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OWUzMTNkOGVhNDZkZDFkNzIwMDk0ODZjOTBmZjdjNjRfOTMwZTQ5OWIxNWNmMTJlNzY2YmQ2Y2JkMDVmNzkyNjBfSUQ6NzY0NDAwMTA3NzU0NDYxOTIxMF8xNzc5NzU3NzE1OjE3Nzk4NDQxMTVfVjM)

### 在这之前，得先分词

不过在模型真正"看到"文本之前，还有一步：文本要先被切成一个个 token。

标准做法叫字节对编码，简称 BPE。别小看这一步，它的逻辑会一路影响到后面所有环节。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjNjNjE1YzhjYmM1OGU5Mzc1Mzk2ZGI4OTI4YTliODlfMjJlZjBjNDhjYmE2NmJiYzJhOTVjMzBlZWRmZjk5MGNfSUQ6NzY0NDAwMTA4MzM3OTc0ODAzMV8xNzc5NzU3NzE1OjE3Nzk4NDQxMTVfVjM)

### 再说说架构——也就是最不重要的那一环

模型本身，就是个 transformer。这一段基本上说到这里也就够了。而这"没什么可说的"，恰恰就是重点。

你不会因为发明了一个更聪明的 transformer 就赢了。真正的胜负，在另外四个阶段。

讲座里用一组缩放曲线，把这事说得明明白白：transformer 的表现就是比老一代的 LSTM 好。所以呢，用现成的标准件就行了，别在这儿纠结，往下走。

## 第二步：数据——真正拉开差距的地方

既然架构最不重要，那反过来，数据就最重要。

这一步，是把一个好模型和一个平庸模型彻底分开的地方，偏偏也是大多数人最容易看轻的一步。

事情是这样的。整条流水线，是从一个叫 Common Crawl 的东西开始的。它相当于把公开的互联网抓了一遍，规模大到得用 PB 来量：2500 亿个网页，一百多万 GB。

但问题来了——原始的网络数据，特别脏。要把这么一大堆东西，变成能拿来训练的干净材料，得过一道又一道很严的筛子。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjVkYTU2ZDAzMDY0ODdkODc4OTJmMmEyOTc3NjY4YThfM2NiNzVlOGU3MmNjOGZjYjEyOGJlY2ZkNWUyOGY1NTVfSUQ6NzY0NDAwMTA5MDQzMjM4ODI3N18xNzc5NzU3NzE1OjE3Nzk4NDQxMTVfVjM)

大致是这么几关：

- 先从 HTML 里把正文抠出来，顺带还得处理好数学公式、模板套话这些麻烦的特殊情况。
- 把不想要的内容滤掉，比如色情、有害信息、个人隐私。
- 去重，按网址、按文档、还要按行——因为网上的东西，页眉页脚菜单栏，没完没了地重复。
- 做一轮启发式过滤，按词数、按那些异常的、脏的 token，把低质量的文档剔出去。
- 再用一个模型来过滤，让它判断：这个页面，够不够格被维基百科引用？
- 最后调配比例，把内容分门别类——代码、书籍、娱乐——再按缩放定律，重新调整每一类的分量。

这里有句话，值得你记牢：数据，质量比数量重要。

把数据收集好，几乎就是做出一个能用的大模型的关键。也正因为太关键，它成了这个行当里捂得最严实的秘密。

光看数字你就懂了：闭源的数据集，规模根本不是开源能比的。LLaMA 3 用了 15 万亿个 token，GPT-4 据说用了 13 万亿。

## 第三步：缩放定律——把算力花在刀刃上

来设想一个场景。你手上有 1 万张 GPU，能用一个月。你会拿它训练一个什么样的模型？

是把模型做得更大一点，还是给它喂更多的数据？

这个选择可不能瞎猜——猜错了，就是几百万美元打了水漂。好在，缩放定律能给你一个相当靠谱、还能提前算出来的答案。

经验告诉我们：数据越多、模型越大，效果就越好。更妙的是，在你真正开训之前，光凭模型的大小和数据量，就能把它最后大概什么表现，给预测出来。

所以现在通行的玩法是：先在小模型上，把各种超参数调好；再顺着那条曲线往上推，去赌最后那一把特别烧钱的大训练。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDRmMTMyNjlmZTk5ODQ3MjNlODllOTliZjZkNTA4ZGVfY2ExYzQ0NjUxN2ZiMDAwNDI5MWI5YmJjNTk3MmE2YzBfSUQ6NzY0NDAwMTA5ODg3NzkzMDY4NF8xNzc5NzU3NzE1OjE3Nzk4NDQxMTVfVjM)

这里面最有名的，是 Chinchilla 算出来的一个结论：每个参数，大概配 20 个 token 的训练数据，最划算。

不过要注意，这笔账只算了"训练"这一头。

可模型造出来不是摆着看的，是要跑的。一旦你把"跑模型"的成本——也就是推理——也算进去，这个比例就猛地往上窜，超过了每个参数 150 个 token。说白了，你宁可拿一个小一点的模型，去喂多得多的数据。为什么？因为这模型造好以后，你得花钱让它跑上几百万次。

说到底，还有一条更上层的道理，叫"惨痛的教训"（the bitter lesson）：别把事情搞复杂。把简单的事做扎实，然后往大了堆。长远看，唯一真正管用的，就是把算力给用足。

## 第四步：后训练——把一个"会预测"的模型，调教成"会答话"的助手

预训练做完，你手里这东西其实已经很强了。但尴尬的是，你拿它来聊天，根本没法用。

为啥？因为它只会接着把文本往下补，压根不知道自己是该来"回答"你的。

你问它一个问题，它没准反手又给你抛三个问题回来。你别觉得它在抬杠——单从"下一个词该接什么"来看，这么续下去，完全说得通。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Nzc4ZmRlNmE4MmU5YmI2MWEzZjZhODQ5ODllNDYyNWRfYTE5ZmU4YmQ5YzFmNDczOTBmODQzZmJmNDkyNjQ0MjdfSUQ6NzY0NDAwMTEwOTc0ODk2MDQ1Nl8xNzc5NzU3NzE1OjE3Nzk4NDQxMTVfVjM)

### 监督微调（SFT）

那怎么办？你给它看成千上万个例子：一句提问，配一段好答案。看多了，它就学会模仿这个套路了。

这个过程有个名字，叫行为克隆。正是这一步，把 GPT-3 变成了 ChatGPT。

有意思的是，这一步需要的数据少得让人意外。几千个例子就够了。为什么这么少？因为 SFT 教的，只是"一个好答案该长什么样"这个格式而已——真正的知识，预训练那会儿早就塞进模型脑子里了。

有个叫 Alpaca 的项目，玩得更绝：它干脆拿另一个大模型来造数据，生成了 5.2 万对指令和回答，就这么把一个 LLaMA 7B，调教成了一个挺能干的助手。

### RLHF——让模型对上人的口味

不过 SFT 也有它的毛病，而且是三个。

一是它的天花板，被人的能力卡死了。二是它会教模型学会"一本正经地胡说"——你让它去克隆一个连它自己都不懂的"正确答案"，这不就等于在教它编瞎话吗。三是，写出那些理想答案，真的很贵。

RLHF 换了个思路来治这三个病：它要优化的，不再是"模仿"，而是"人到底更喜欢哪个"。

做法也不复杂。让模型一次生成两个答案，由人来挑哪个更好。把这些选择攒起来，去训练一个专门的"奖励模型"，然后再回头去调原来那个大模型，让它想方设法把这个奖励做到最高。经典的做法，是用一个叫 PPO 的算法。

后来又出了个更省事的新办法，叫 DPO。它用普普通通的监督学习，就能做出差不多的效果，现在已经成了开源圈里的标配。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGY3ODRhNzJhYmIzMWVhNGJkZTFmNzlhMzQ2ZmMyNTFfYzJlMGQ4YmRjOGM2Nzc0NmYwNWFhOGNjMmU0ZjE3MjZfSUQ6NzY0NDAwMTExNzY3ODIyNjY0Nl8xNzc5NzU3NzE1OjE3Nzk4NDQxMTVfVjM)

## 第五步：评估和系统——证明它真行，也让它真造得出来

最后这一步，其实是两件事，它俩像一层壳，把前面整条流水线从头到尾包了起来。这两样少了哪个，你都不好意思说自己手里有个真正的模型。

### 评估：一个没有标准答案的东西，你怎么打分

预训练那会儿，衡量的指标叫困惑度。你可以把它理解成：模型在多少个 token 之间"拿不定主意"。

这些年进步有多大？从 2017 到 2023 年，最好的模型，从在大约 70 个词之间犹豫，降到了不足 10 个。

可问题来了：模型一旦经过对齐，困惑度这把尺子就不灵了。于是评估只好转向各种基准和对比：

- MMLU 和 HELM：覆盖很多领域、自带标准答案的题库。其中 MMLU，是大家最认可的预训练基准。
- Chatbot Arena：让人盲测两个模型，再投票，30 多万张票，撑起了一个 Elo 排行榜。
- AlpacaEval：让一个大模型，去给别的大模型打分。它的结果和 Chatbot Arena 有 98% 对得上，3 分钟内、花不到 10 美元就能跑完——当然它也有偏心，比如格外偏爱长答案。

说句实在话：给一个对齐过的模型打分，是真难。没有哪一个数字，能把它说清楚。夸张到什么程度？同一个模型，你光是把提问的格式换一换，它在 MMLU 上的分，就能从 0.637 掉到 0.488。

### 系统：让训练，在现实里真的能跑起来

还有一个谁也绕不开的现实：所有人都被算力卡着脖子。GPU 又贵又难买，物理上还被通信速度死死拖着。

给你个直观的数：一个 7B 的模型，要是啥优化都不做地硬训，光显存就得吃掉差不多 112GB。

所以系统这一层，根本不是"锦上添花"，而是让这一整套东西能真正落地的前提。常见的几招是这样：

- 低精度：用 16 位（bf16）代替 32 位，显存直接砍一半，速度反而更快。
- 算子融合和分块：尽量少去碰那个慢吞吞的全局内存。光是一个 FlashAttention，端到端就能快上大约 1.7 倍。
- 数据并行：把数据集切开，分到好几张 GPU 上跑（再用 ZeRO 把优化器的状态也拆开，省显存）。
- 模型并行：把模型本身切开，分到多张 GPU 上。要么按层切（这叫流水线），要么按矩阵切（这叫张量）。
- 稀疏化：也就是专家混合（MoE）。参数变多了，但计算量不变——靠的是每个 token，只叫醒其中一部分参数干活。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzMwMzQwYWE4ZWNiNjE3NDJhZjI2ZWY2ZWIyY2NmNmRfNWY2ZDg4NTAyNGY4ZTRjODQ5Yzk5NzA1Y2U3MmE2MTdfSUQ6NzY0NDAwMTEyNDUxMzQxODQ0NF8xNzc5NzU3NzE1OjE3Nzk4NDQxMTVfVjM)

## 把这五步走完，它到底想告诉我们什么

现在你回过头，把这五个阶段从头再捋一遍，那个结论就硬得没法反驳了。

架构——大家最痴迷的那一块——反倒是着墨最少的。真正一个决定接一个决定被拍板的地方，是数据、是缩放、是对齐、是评估、是系统。

这也正好解释了一件事：为什么两个用着同一套架构的实验室，造出来的模型能差出十万八千里。架构是大家共享的，而那些真正要紧的东西，一样都不共享。

## 几个最容易让 LLM 项目翻车的坑

- 死磕架构。它恰恰是整套技术栈里，被抄得最多、也最没区分度的部分。
- 把数据当成随手就能买到的大路货。数据一脏，你堆再多算力，上限也被它压得死死的。记住，质量比数量重要。
- 跳过 Chinchilla 那笔账。模型相对它的数据做得太大，就是训练不够，纯属白白浪费算力。
- 走到 SFT 就不往下走了。微调出来的模型，只会模仿；没有 RLHF 或者 DPO，它永远不知道人到底喜欢什么。
- 对齐之后还盯着困惑度看。后训练早就把分布给改了，这时候的困惑度，也就不再说明什么问题了。

## 最后

一个出色的模型，不是训练出来的，是工程出来的。

我猜，大多数人还是会继续相信：造大模型，关键在架构。然后继续去读那些讲 transformer 的文章，也就继续错过了——真正的活儿，到底是在哪儿干成的。

而真正把这条流水线搞懂的人，会看得清清楚楚：先是语言建模，然后是干净的数据，接着把算力缩放到最优，再是对齐，最后，在一套高效的系统上，做一次诚实的评估。五个阶段。架构，不过是其中某一个阶段里的一段话罢了。

所以，挑一个你一直在绕着走的阶段——多半是数据，或者评估。往深里钻进去。差距，就藏在那儿。
