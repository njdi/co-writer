# 我用3周研究怎么做AI网红，把所有干货整理在这里了

**作者：** RetroChainer ([@RetroChainer](https://x.com/RetroChainer))  
**日期：** 2026年5月6日  
**来源：** [I spent 3 weeks figuring out how to make AI influencers. Here's everything you need to know.](https://x.com/Zephyr_hg/status/2051980350239191077)

## 第一步 - 选择垂类

真正的核心是**垂类**。它决定了一切：

- 模型的外貌和风格
- 内容形式和触点
- 用户粘性和账号增长

AI网红这个市场，也就是几个月前才冒出来的。各个垂类的潜力还远远没有被挖掘——跟着别人的路子复制成功女孩，没有意义，你需要找到自己的方向。

三个跑得通的方向：

![Image](images/img-01.jpg)

**1. 亚文化** — 动漫、Cosplay、游戏女主播、足球俱乐部的女球迷。经久不衰的话题，受众参与度极高。

举个例子：你可以找一段女性CS2主播的视频，把她替换成你的AI模型。或者做一个漫威宇宙cosplay角色的账号。一篇触碰到某个社区内部争议点的帖子，就因为一个细节，就能撬动大量互动。

**2. 旅行和活动** — 你的模型现在就可以出现在戛纳红毯、东京街头或某场演唱会上，连家都不用出。这类内容看起来很贵，因为观看的人隐约能感觉到背后的功夫。

**3. 外貌特征** — 胎记、疤痕、独特的面部特征，可以作为额外触点，但不适合作为账号的核心卖点。几个月前，那种不真实的外貌还能引起轰动——现在已经没人觉得新鲜了。

![Image](images/img-02.jpg)

> **实验假设：** 做一个某支足球队的铁杆女球迷，定期强调某位球员是全队最强。仇恨涌来 + 支持涌来 = 额外互动 + 算法加权。

## 第二步 - 生成面部

没有参考图的AI，生成的脸都是平均值——长得不难看，但没有辨识度。你刷一圈新的AI账号，每张脸都长得一个模子出来的。原因就在这里。

**工具：**

- [Pinterest](https://www.pinterest.com/) - 收集参考图
- [Nano Banana Pro (Higgsfield)](https://higgsfield.ai/) - 面部融合

![Image](images/img-03.jpg)

**操作流程：**

1. 找两张不同女孩的照片，面部要清晰
2. 把两张照片和提示词一起上传到 [Nano Banana Pro](https://higgsfield.ai/)：

> Integrate a face into an existing scene. Substitute the face in the reference image with the face from the donor image. The objective is a seamless merge: the new face must inherit the exact expression, pose, and lighting interaction from the reference, while its color attributes (hair and eyes) are adapted from the donor for a perfectly harmonious and natural result.

![Image](images/img-04.jpg)

3. 拿到结果。如果需要，加一个辨识特征（胎记、特殊眼睛颜色）

**怎么挑脸**

最常见的错误是选两张长得像的脸。神经网络会把差异磨平，最后还是回到那个平均结果。

要选对比鲜明的脸，提前分好角色：

- **第一张脸**（基底脸）：定垂类的气质（高颧骨，"冷感"眼神）
- **第二张脸**（融合脸）：柔化，增加亲和力（娃娃脸，丰唇）

![Image](images/img-05.jpg)

**不同垂类对应的脸型：**

- **Cosplay**、动漫、游戏角色
- **硬朗面孔** — 哥特风、暗黑少女

![Image](images/img-06.jpg)

- **柔和/浪漫面孔** — 时尚、精致生活方式

![Image](images/img-07.jpg)

> **实验假设：** 在动漫女孩垂类里，找不同种族女孩的照片，把她们融合在一起，加上胎记作为辨识点——一下子就把亚文化和外貌触点两个维度都抓住了。

## 第三步 - 生成视频

这个方法的核心：AI复制参考视频里真人的动作，然后把画面里的人完全替换成你的模型。

**3.1 找参考视频**

在TikTok和Instagram上搜，以你的垂类为关键词——哥特女孩、动漫女孩、cosplay。

好参考的标准：

- 播放量高
- 面部表情有感染力、有张力
- 带点浪漫感
- 有你垂类的触点

> **关键原则：** 参考视频里的人和你的模型长得越像，生成效果越真实。Kling在把长发女孩的动作迁移到短发模型上时会出问题。

**3.2 制作第一帧**

不能直接把你的模型照片丢进去就点"生成"。[Kling](https://app.klingai.com/global/video-motion-control/new) 会读取你上传的照片里的背景和姿势，而不是参考视频里的。所以你需要先做一帧起始图。

上传到 [Nano Banana Pro](https://higgsfield.ai/)：

1. 你的AI模型照片

![Image](images/img-08.jpg)

2. 参考视频第一帧的截图

![Image](images/img-09.jpg)

3. 提示词：

> Take the girl's face and body from the first image, and the pose, emotion, and background from the second. Use the girl's face from the first image as the character's face and replace it in the second image, it is necessary to accurately convey emotion and playfulness, it is necessary to accurately convey the appearance of the girl from the first image without changing her appearance, the photo must be alive, the girl is not a doll, sincere real, photo taken on an iPhone phone camera.

![Image](images/img-10.jpg)

**3.3 在 Kling 里生成**

上传到 [Kling Motion Control](https://app.klingai.com/global/video-motion-control/new)：起始帧 + 参考视频。在高级设置里粘贴以下提示词：

```
Use the attached reference video as the sole motion blueprint and transfer its movement onto the character from the attached photo(s), preserving the character's exact identity, body proportions, face and hair features, skin texture, clothing fit, and overall silhouette with zero morphing, zero style drift, and no added accessories; match the reference motion precisely frame-by-frame including timing, speed, acceleration/deceleration, weight shifts, center-of-mass trajectory, foot placement, heel-to-toe roll, balance corrections, hand paths, finger articulation, head turns, eye-line direction, micro-expressions, breathing rhythm, and any subtle pauses, ensuring strict real-world biomechanics and believable inertia, muscle tension, and joint limits without exaggeration or "animation-like" elasticity; keep the action grounded in realistic physics with consistent gravity, natural momentum, correct contact forces, and clean interaction with the ground and body (no foot sliding, no limb stretching, no jitter, no teleporting, no sudden snaps), and do not invent any new gestures, effects, camera tricks, slow motion, extra movement, or transitions beyond what exists in the reference video; maintain stable, artifact-free rendering throughout with crisp continuity and no blur, warping, flicker, double-imaging, or AI glitches while the character performs the exact same motion sequence from start to finish.
```

这段提示词专门针对 Kling 的两个老问题——外貌漂移和画面瑕疵。它把动作的生物力学锁死，让模型不会自己发挥。

**3.4 在 CapCut 里后期**

Kling 出来的原始渲染，一眼就看出是AI。目标是去掉那种塑料感，让视频像手机拍出来的。

**后期之前有个重要步骤：** 先把视频通过 Telegram 或 AirDrop 从电脑传到手机。神经网络会在文件里留下"AI生成"的元数据标记，传输这一步能把它清掉——平台就会把视频当成普通用户内容。

[CapCut](https://www.capcut.com/) 参数参考：

| 参数 | 数值 | 作用 |
|------|------|------|
| 颗粒 | 40 | 去掉AI的塑料感 |
| 清晰度 | 20 | 还原面部和服装细节 |
| 亮度 | –5 到 –10 | 增加层次感，去除"塑料"观感 |
| 暗角 | 10–15 | 增加电影质感 |

这些数值是参考，不是死规则。场景本来就暗就别动亮度；对比度高就把颗粒调小一点。核心是颗粒 + 降低亮度这两个变量。

> **实验假设：** 同一个视频做两个版本——有后期和没有后期的，间隔几天发出去，对比触达量。这个数据会告诉你后期到底对算法有多大影响。

## 完整流程

**垂类** → **面部**（Nano Banana Pro）→ **起始帧**（Nano Banana Pro）→ **生成**（Kling Motion Control）→ **后期**（Telegram → CapCut）

下一步是搭建自己的工作流。Kling 上手简单，但不是最强的工具。一套完整的工作流能带来明显更高的质量——我们下次单独聊。

更多关于AI网红、工作流和变现的内容，关注我的Telegram：https://t.me/+Qc2hxi7IClViMDRi
