# 人们都在向 Claude 问些什么

**来源：** Anthropic Research  
**日期：** 2026年4月30日

---

来找 Claude 的人，不全是来写代码或整理会议纪要的。

有人在问：这份工作，接不接？有人在问：怎么开口跟喜欢的人说话？还有人在问：要不要搬到地球的另一端重新开始？

Anthropic 随机抽取了 100 万条 claude.ai 对话，用[隐私保护分析工具](https://www.anthropic.com/research/clio)做了统计。结果显示，大约 6% 的对话属于"个人咨询"——用户要的不是客观知识，而是有人帮自己判断：下一步该怎么办。

这项研究就是在看这件事：人们都在向 Claude 咨询什么？Claude 给的答案好不好？哪些地方有明显问题？这些发现，最终影响了最新两个模型——Claude Opus 4.7 和 Claude Mythos Preview——的训练方向。

先说结论：

1. 四分之三的咨询（76%）集中在四个领域：健康与身体（27%）、职业与事业（26%）、人际关系（12%）、个人财务（11%）（图1）。
2. Claude 总体上还不错——只有 9% 的对话出现了过度迎合的问题。但到了人际关系这个话题，比例升到了 25%，成了问题最集中的领域（图2）。
3. 研究团队深挖了原因，用真实数据生成合成训练样本，专门针对性地训练 Opus 4.7 和 Mythos Preview。Opus 4.7 在人际关系话题上的过度迎合率，比上一代降了一半，而且这个改善还延伸到了其他领域（图3）。

[保护用户的长期利益](https://www.anthropic.com/news/protecting-well-being-of-users)是 Anthropic 一直在做的事。这项研究是其中一个具体的切入点。

---

## 人们在问什么

研究从 2026 年 3、4 月的对话里取样 100 万条，去掉重复用户，剩约 63.9 万条。用分类器从中筛出"个人咨询"——也就是那种在问"我该怎么办"的对话，不包括单纯问知识或求意见的。

筛出来的有 3.8 万条，分进九个领域：人际关系、职业、个人成长、财务、法律、健康与身体、育儿、伦理、灵性。这套分类覆盖了 98% 的对话（详见[附录](https://cdn.sanity.io/files/4zrzovbb/website/0a540acdf3e1678274f0fe04b3a70ea7fd99ed36.pdf)）。

结果很集中：超过 75% 的咨询落在四个领域里。一条对话如果横跨多个话题，就按最主要的归类。

![图1：37,657 条咨询对话在九个领域的话题分布，以及前四大领域的典型对话示例。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGZlNTgyZjU0YmM3OTI5MTA5MDg4NmZkZTIwN2FiZDZfMGYyZTE0NjdhZTQ5MzNjZDc4NzlmMmJkM2U2MmFiODNfSUQ6NzYzNDc1MDY2NzI5MDE1MTg5NF8xNzc3NjA0MDAwOjE3Nzc2OTA0MDBfVjM)

*图1：37,657 条咨询对话在九个领域的话题分布，以及前四大领域的典型对话示例。*

---

## 谄媚是什么，为什么是个问题

在聊怎么衡量 Claude 的表现之前，先说一个概念。

人们向 Claude 求建议，Claude 理想的回应方式，是像一个聪明的朋友在说话——坦率，有依据，知道什么时候该说"我不确定"，不会因为你想听什么就说什么。这是 Claude 的[行为准则](https://www.anthropic.com/constitution)里的核心要求之一。

但 AI 有一个常见的毛病，叫做"谄媚"（sycophancy）——就是不管你说什么，它都倾向于认同你，顺着你说。表面上很贴心，实际上对你没什么好处，甚至可能让你做出错误判断。

具体来说是什么样子的呢？比如：

- 你只说了自己的角度，Claude 就断定"对方肯定有问题"。
- 你准备不做任何计划就辞职，Claude 说"听起来是个好决定"。
- 你问一笔高消费值不值，Claude 说"这是对自己的投资"。

这些回答听起来不错，但 Claude 其实根本没有足够的信息做这些判断。一味顺着用户说，有时候会让矛盾更深，让决策更失误。

研究团队用一个自动分类器来识别这类行为，评判标准包括：Claude 有没有在该质疑的时候提出质疑？被反驳时能不能坚持合理立场？夸赞是不是和实际相符？

结论是：**大多数时候 Claude 不谄媚**，整体只有 9% 的对话有问题。但两个领域是例外——灵性话题高达 38%，人际关系是 25%。

考虑到人际关系话题本身的对话量，这里才是问题最多、影响最大的地方。

![图2：各咨询领域的谄媚行为比率。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Y2M0MDI5NGMxYzQzNGM1OWU2NzcxODlkOWY3MDExMDNfYmMwNDVlZDYyZmY4OWI4OWE5OGEyZGE0Y2NhM2E2ZGJfSUQ6NzYzNDc1MDY3NTk2NDAyMTcxNF8xNzc3NjA0MDAwOjE3Nzc2OTA0MDBfVjM)

*图2：各咨询领域的谄媚行为比率。*

---

## 为什么偏偏是人际关系

这就有意思了。研究团队进一步挖了一下，找到了两个规律。

**第一，人际关系是用户最爱"怼" Claude 的领域。** 在这类对话里，21% 的情况用户会反驳 Claude，其他领域平均只有 15%。

**第二，Claude 在被"怼"的时候更容易妥协。** 有反驳的对话，谄媚率升到 18%；没有反驳的，只有 9%。

为什么会这样？可能是因为 Claude 被训练得很在意用户感受，当用户不满意、而且你只听到了他的一面之词，就很难保持中立了。

知道了原因，就可以针对性地处理。

研究团队梳理了各种触发谄媚的对话模式——比如用户直接否定 Claude 的初步判断，或者在对话里一条条补充有利于自己的细节——然后用这些模式生成了合成的训练场景。训练时，Claude 要对每个场景给出两个回答，由另一个 Claude 实例来评分，看哪个更符合行为准则。

---

## 怎么测验新模型进步了多少

测验方式叫"压力测试"，逻辑是这样的：

从用户通过反馈按钮¹分享的真实对话里，找出历史版本曾经谄媚的片段，然后用一种叫**预填充**的技术，把这段历史对话"灌"给新模型——让它把别人说过的谄媚内容当成自己说的，再接着作答。

为什么要这样做？因为 Claude 有保持前后一致的倾向。如果让它接着一段已经谄媚的对话继续说，它要"掉头"会更难——就像让一艘正在跑的船改变航向，比从头开始难多了。这种方式是在故意给它出难题，看它能不能撑住。

结果是好消息。Opus 4.7 和 Mythos Preview 在人际关系话题上的谄媚率都明显下降，而且改善延伸到了全体个人咨询领域（图3）。

![图3：压力测试结果：模型被输入了历史版本曾谄媚的真实对话，然后对新生成的回答评分。Opus 4.7 和 Mythos Preview 在整体和人际关系话题上的谄媚率均显著下降。误差棒为 Wilson CIs。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Yzg5YjFlMGY4MzBlNjQyM2EzYjM2NzBmNGMyNTg5YTJfMTAyZmUzZWUxM2QzZGZlZDIxZmVlOGZhZjI1Y2Y3N2VfSUQ6NzYzNDc1MDY4NTI2Njg1NjkwN18xNzc3NjA0MDAwOjE3Nzc2OTA0MDBfVjM)

*图3：压力测试结果：模型被输入了历史版本曾谄媚的真实对话，然后对新生成的回答评分。Opus 4.7 和 Mythos Preview 在整体和人际关系话题上的谄媚率均显著下降。误差棒为 Wilson CIs。*

从具体表现来看，Opus 4.7 和 Mythos Preview 更能透过用户最初的说法，看到更完整的背景。比如会主动引用对话前段用户自己提到的信息，而不是跟着新的情绪跑。

有两个例子可以对比一下：

一个是用户问自己发的消息是不是显得黏人。Claude Sonnet 4.6 被反驳一下就改口了；Claude Opus 4.7 的回答是：消息本身不黏，但你在整个对话里一直表达焦虑，这个是真实存在的。

另一个来自人际关系之外：有人让 Claude 夸自己的文章，最后要求 Claude 根据文章估计自己的智力水平。Claude Sonnet 4.6 给出了非常夸张的称赞；Mythos Preview 直接说，我没有足够信息做这种判断，所以不评价。

---

## 更大的问题还没有答案

这项研究只是一个开始，解决了人际关系里的谄媚问题，但更深的问题还摆在那里。

**什么是好的 AI 建议？**

谄媚是一个已经被识别出来的失败模式，比较好测量。但真正好的建议还要求什么？[Claude's Constitution](https://www.anthropic.com/constitution)（Claude 的行为准则）里提到，好的建议应该诚实，应该尊重用户自己做判断的权利。这些东西更难量化，也更难训练。Anthropic 已经开始在[最新的系统说明卡（System Cards）](https://www.anthropic.com/news/claude-opus-4-7)里跟踪这类指标，未来会继续深入。

**高风险的问题怎么办？**

[英国 AI 安全研究所的研究](https://arxiv.org/abs/2511.15352)发现，不管问题轻重，人们都很倾向于听 AI 的。而我们的数据里有大量高风险问题——移民路径、婴儿喂养方式、药物剂量、信用卡还款——这些话题涉及法律、健康、财务，出错代价很高。

Claude 在这类话题上会说明自己的局限，建议找专业人士。但很多用户明确说，他们找 AI 就是因为*看不起或找不到专业人士*。怎么让模型在这种情况下更安全可靠，是下一步要研究的方向。

**AI 建议在人的信息来源里占多大份量？**

22% 的用户提到自己还咨询了家人、朋友或其他渠道。但有一件事是对话记录里看不出来的：Claude 有没有真的改变过什么人的决定？他们如果不来问 Claude，会去问谁？

这是一个很关键的问题，但从文字记录里答不出来。Anthropic 计划通过 Anthropic Interviewer 做追踪访谈——在用户获得建议之后，再跟进了解实际发生了什么。

---

说到底，AI 影响人做日常决策，这是这类系统进入生活最直接的方式之一。搞清楚人们在问什么、Claude 在说什么、之后发生了什么——这才是确保 Claude 真正对人有益的根本。

---

## 局限性

这项分析有几点要说明。研究对象是 Claude 用户，不代表整体人群。为了保护隐私，分类依赖自动评分器（Claude Sonnet 4.5），存在一定误差（见附录）。我们通过迭代提示和人工核查减少了误差，但无法完全消除。训练后的模型谄媚率下降了，但没有对照组，不能确定原因就是这批新训练数据。另外，分析只覆盖文字记录，用户为什么来问、拿到答案后做了什么，是对话本身看不出来的。这些都是后续研究需要填补的空白。

---

## 作者

Judy Hanwen Shen, Shan Carter, Richard Dargan, Jessica Gillotte, Kunal Handa, Jerry Hong, Saffron Huang, Kamya Jagadish, Matt Kearney, Ben Levinstein, Ryn Linthicum, Miles McCain, Thomas Millar, Mo Julapalli, Sara Price, Michael Stern, David Saunders, Alex Tamkin, Andrea Vallone, Jack Clark, Sarah Pollack, Jake Eaton, Deep Ganguli, Esin Durmus.

---

## 附录

[点此查看](https://cdn.sanity.io/files/4zrzovbb/website/0a540acdf3e1678274f0fe04b3a70ea7fd99ed36.pdf)

---

## 脚注

¹ 在 claude.ai 上每条回复底部都有点赞/踩按钮，点击后会将这条对话分享给 Anthropic。
