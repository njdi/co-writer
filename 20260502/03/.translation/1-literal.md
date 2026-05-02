# 如何找到下一个100倍回报的想法

**作者：** hoeem ([@hooeem](https://x.com/hooeem))  
**日期：** 2026年5月2日  
**来源：** [How to Find the Next 100x Idea](https://x.com/Zephyr_hg/status/2050332284675362853)

每个人都想让他们的AI给他们一个100倍回报的想法，谁不想呢？他们去找AI，问它问题，然后得到的全是垃圾。

停止浪费你的时间，转而构建这个。

是时候去寻找痛点了。

真实的痛点。反复出现的痛点。代价高昂的痛点。那种人们已经在抱怨、搜索、绕路解决，有时甚至付钱给设计糟糕的工具来解决的问题。

这是我们要构建的：

```
社交监听提醒
→ 数据库
→ AI提取痛点
→ 机会评分
→ 手动MVP
→ 构建 / 转向 / 放弃
```

这就是我们如何找到想法的方式，甚至可以利用它来改善你现有的业务或想法。

我们要收集的数据是看起来像这样的社交信号：

- "我讨厌手动做这件事。"
- "有没有人知道一个能做这个的工具？"
- "有没有这个的替代品？"
- "这太贵了。"
- "我还在用电子表格。"
- "我每周在这上面浪费好几个小时。"
- "为什么这么难？"
- "我试过X、Y和Z，但还是很糟糕。"

那就是黄金所在。

## Reddit和X的真相

Reddit和X是这类研究最好的两个来源。

但你需要小心。

Reddit很有用，因为人们在上面写长篇的、带有情绪的投诉。他们解释他们的问题、绕路方法、失败的工具、奇怪的边缘情况，以及他们为什么感到恼火。

X很有用，因为人们在公开场合抱怨、寻求推荐、比较工具，并实时揭示正在发生的变化。

不要构建一些粗糙的爬虫然后把它叫做"AI研究"。

- 尽可能使用官方API。
- 在API混乱的地方使用经过批准或授权的监控工具。
- 使用提醒，而不是盗窃。
- 只存储你需要的内容。
- 遵守规则。

AI并不能神奇地让糟糕的数据收集变得可以接受。

![Image](images/img-01.jpg)

## 平台地图：我实际上会使用什么

Reddit适合：

- 痛点挖掘
- 长篇投诉
- 竞争对手替代品
- 小众社区
- "有没有人知道一个工具？"类型的帖子
- 带有情感色彩的客户语言

Reddit是了解人们在没有被采访时如何说话的最佳场所之一。

这很重要。

X适合：

- 实时投诉
- 创始人/运营者的闲聊
- 工具比较
- 市场变化
- 公开的购买意向
- 人们向他们的网络寻求推荐

X适合速度，Reddit更适合深度。

YouTube适合：

- 创作者市场
- 教育产品
- 软件教程
- "我怎么做X？"的行为
- 评论中抱怨现有解决方案令人困惑

当问题已经有教育需求时，YouTube特别有用。

Facebook适合：

- 没什么用，哈哈，好吧，它在群组里可能还不错。

LinkedIn适合：

- 手动搜索
- 内容
- 外联
- 访谈
- 以关系为导向的验证

## 你要构建什么？

你要为想法构建一个**AI痛点挖掘机器**。

![Image](images/img-02.jpg)

它的工作：

1. 在Reddit、X、YouTube、评论、论坛、博客和社交平台上搜索公开对话。
2. 将有用的提及拉入数据库。
3. 让AI提取痛点、绕路方法、竞争对手、紧迫性和购买意向。
4. 对每个信号进行评分。
5. 将反复出现的问题归类为商业机会。
6. 将最强的机会转化为一个提案。
7. 用登陆页面、表单、外联或手动MVP来测试它。

像这样：

```
找到痛点
→ 对痛点评分
→ 聚类痛点
→ 测试痛点
→ 只有当人们关心时才构建
```

## 我应该使用什么工具？

```
Brand24
Airtable
Make
OpenAI / ChatGPT API
Tally
Carrd, Framer, Lovable, Bolt, 或 v0
```

确保你不使用粗糙的爬虫，确保它是官方API和经过批准的工具。不要使用违反平台规则的爬虫。这不是一个好主意。

Reddit的数据API条款限制了用户内容的使用方式，包括在未经许可的情况下使用Reddit内容来训练AI模型，商业使用可能需要单独协议。

X的API提供对公开对话的程序性访问，但它现在使用按使用付费的定价方式，预先购买积分并随着API请求的进行而扣除。

YouTube对初学者来说更为简洁，因为其数据API有官方的评论端点。`commentThreads.list`返回评论线程，每次调用费用为1个配额单位，YouTube项目通常以每天10,000个单位的默认日配额开始。

## 你最终将拥有什么

一个显示以下内容的仪表板：

```
原始痛点信号
AI摘要
痛点评分
买家细分
绕路方法
竞争对手
反复出现的痛点集群
商业想法
登陆页面角度
手动MVP想法
构建 / 观察 / 忽略 的判断
```

一份每周报告，如：

```
本周最强机会：
独立招聘人员浪费时间撰写候选人摘要。

证据：
在Reddit、X和YouTube评论中有12个强痛点信号。

最佳引言：
"我花了好几个小时把混乱的筛选笔记整理成可以发给客户的东西。"

推荐测试：
登陆页面 + 向20名招聘人员发送私信 + 手动摘要服务。
```

# 阶段1：选择一个市场开始

不要从每一个市场开始，选择一个。

示例：

```
独立招聘人员
房产中介
物理治疗师
加密货币研究员
新闻简报作者
小型物业管理人员
私人教练
电商运营者
YouTuber
独立顾问
```

以及一个工作流程：

```
撰写客户摘要
创建每周报告
处理客户支持
管理租户维修
研究加密货币项目
撰写社交媒体帖子
追收发票
制定膳食计划
跟进潜在客户
```

示例：

```
买家：独立招聘人员
工作流程：将筛选电话笔记转化为适合发给客户的候选人摘要
```

# 阶段2：创建你的Airtable数据库

打开Airtable。

创建一个名为：**AI痛点挖掘机器**的新数据库

创建这些表：

```
1. 原始信号
2. 痛点集群
3. 商业想法
4. 实验
5. 客户访谈
6. 每周报告
```

## 表1：原始信号

这是每一个Reddit帖子、X帖子、YouTube评论、评论、论坛评论或博客提及的去处。

创建这些字段：

```
发现日期
来源
来源URL
匹配关键词
原始文本
作者/账号
买家细分
工作流程
清洁引言
痛点
根本原因
当前绕路方法
提及的竞争对手
购买意向信号
痛点严重程度 /10
紧迫性 /10
频率 /10
支付意愿 /10
AI自动化潜力 /10
整体信号评分 /100
信号质量
状态
人工审核
备注
```

使用这些字段类型：

```
发现日期 = 日期
来源 = 单选
来源URL = URL
原始文本 = 长文本
清洁引言 = 长文本
痛点 = 长文本
评分 = 数字
信号质量 = 单选
状态 = 单选
人工审核 = 复选框
```

对于**来源**，添加：

```
Reddit
X
YouTube
TikTok
LinkedIn
Facebook
论坛
评论网站
博客
新闻
其他
```

对于**状态**，添加：

```
新建
需要AI
AI已分析
高信号
低信号
已拒绝
已聚类
已用于测试
```

对于**信号质量**，添加：

```
低
中
高
```

## 表2：痛点集群

这将反复出现的信号归类在一起。

字段：

```
集群名称
买家细分
工作流程
核心痛点
证据数量
发现的来源
最佳引言
常见绕路方法
提及的竞争对手
平均信号评分
机会评分 /100
手动MVP想法
登陆页面角度
判断结果
备注
```

判断结果选项：

```
构建测试
观察
忽略
需要更多研究
```

## 表3：商业想法

字段：

```
想法名称
买家
解决的问题
提案
手动MVP版本
后续软件版本
定价假设
分发渠道
主要风险
机会评分 /100
状态
```

状态选项：

```
想法
测试中
已验证
已放弃
已转向
```

## 表4：实验

字段：

```
实验名称
商业想法
登陆页面URL
表单URL
行动号召
流量来源
访客数
注册数
表单完成数
预约通话数
手动MVP试用数
付费试点数
转化备注
判断结果
```

## 表5：客户访谈

字段：

```
姓名
职位
公司
电子邮件
买家细分
问题已确认？
当前绕路方法
痛苦程度 /10
预算证明
愿意尝试手动MVP？
愿意付费？
最佳引言
需要跟进？
备注
```

## 表6：每周报告

字段：

```
周起始日期
顶部痛点集群
最佳机会
关键证据
推荐测试
构建 / 观察 / 忽略 判断
报告文本
```

# 阶段3：设置你的社交监听工具

现在打开Brand24或另一个社交监听工具。

创建一个新项目。

命名为：**招聘人员痛点挖掘**

或者你正在研究的任何市场。

你的目标是收集人们在抱怨工作流程的公开提及。

## 添加关键词

从10到20个关键词开始。

对于招聘人员示例：

```
"candidate summary"
"candidate summaries"
"screening call notes"
"recruiter notes"
"recruiter admin"
"recruitment CRM too expensive"
"alternative to recruitment CRM"
"recruiter spreadsheet"
"client-ready candidate summary"
"recruiter notes to client"
"recruiter manual admin"
"recruitment admin takes too long"
```

你想要那些能揭示痛点的短语。

更好的："candidate summaries" "takes hours"  
更差的："recruiting"

## 添加痛点修饰词

创建另一个关键词组，包含如下短语：

```
"takes hours"
"manual"
"frustrating"
"annoying"
"too expensive"
"alternative to"
"does anyone know a tool"
"how do you manage"
"spreadsheet"
"copy paste"
"wasting time"
```

最好的搜索结合了：买家 + 工作流程 + 痛点修饰词

示例："recruiter" "candidate summaries" "takes hours"

## 设置来源过滤器

从这些来源开始：

```
Reddit
X
YouTube
论坛
评论
博客
新闻
```

将LinkedIn、Facebook和私人社区列为"谨慎使用"。它们可能有用，但从权限和信号质量的角度来看，它们更混乱。

# 阶段4：将提及导入Airtable

你有三个选项。先从选项A开始，然后转到B或C。

## 选项A：手动导出

先用这个。

每天一次：

1. 打开Brand24。
2. 进入你的提及信息流。
3. 按相关来源过滤。
4. 打开每个有用的提及。
5. 复制有用的文本。
6. 将其粘贴到Airtable的**原始信号**表中。
7. 将状态设置为"需要AI"。

## 选项B：电子邮件提醒导入Airtable

一旦你知道你的关键词足够好，就使用这个。

设置：

```
Brand24提醒邮件
→ Gmail
→ Make
→ Airtable原始信号
```

在Gmail中：

- 创建一个名为"痛点信号"的标签。
- 为你的Brand24提醒邮件创建一个过滤器。
- 自动应用"痛点信号"标签。

在Make中：

- 创建一个新场景。
- 添加Gmail作为触发器。
- 选择"监听邮件"。
- 按"痛点信号"标签过滤。
- 添加Airtable。
- 选择"创建记录"。
- 选择你的数据库：AI痛点挖掘机器。
- 选择你的表：原始信号。
- 将邮件主题/正文映射到Airtable字段。
- 将状态设置为"需要AI"。

这给你一个可工作的自动化收集器。

## 选项C：API/Webhook收集

以后再用这个。

高级路径：

```
Brand24 API或webhook
→ Make webhook
→ Airtable
```

或者：

```
Reddit API
X API
YouTube API
→ Make / n8n / 自定义脚本
→ Airtable
```

除非你了解你想要的数据，否则不要从这里开始。

API版本更强大，但逻辑是相同的。

# 阶段5：构建AI分析自动化

现在让AI分析每个信号。

在Airtable中，在原始信号中创建一个名为：**需要AI**的视图

过滤器：状态 = 需要AI

现在打开Make。

创建一个新场景：

```
Airtable监听记录
→ OpenAI生成响应
→ Airtable更新记录
```

Make的Airtable模块可以监听视图中新创建或更新的记录，其OpenAI模块可以从提示中生成响应。

**Make步骤1：Airtable触发器**

模块：Airtable > 监听记录  
选择：
- 数据库：AI痛点挖掘机器
- 表：原始信号
- 视图：需要AI

这意味着Make监听需要分析的信号。

**Make步骤2：OpenAI分析**

粘贴此提示：

```
You are analysing public customer conversations for startup discovery.

Your job is to extract commercial pain from the text below.

Important rules:
- Do not invent evidence.
- Only use what is present in the text.
- If the text is vague, score it low.
- Ignore generic chatter.
- Prioritise specific workflow pain, buying intent, ugly workarounds, competitor dissatisfaction, urgency, and evidence of willingness to pay.
- Do not include personal data unless essential.
- Keep quotes short.

Return the output using this exact format:

Buyer Segment:
Workflow:
Clean Quote:
Pain Point:
Root Cause:
Current Workaround:
Competitor Mentioned:
Buying Intent Signal:
Pain Severity /10:
Urgency /10:
Frequency /10:
Willingness To Pay /10:
AI Automation Potential /10:
Overall Signal Score /100:
Signal Quality:
Recommended Status:
Notes:

Scoring guidance:
- 0 to 30 = weak signal
- 31 to 60 = possible signal
- 61 to 80 = strong signal
- 81 to 100 = excellent signal

Raw text:
{{Raw Text}}
```

将`{{Raw Text}}`替换为上一步中的Airtable字段。

**Make步骤3：更新Airtable**

更新同一条记录。

将AI输出映射到字段中。

如果起初解析每个字段感觉太难，可以这样做：在Airtable中创建一个名为**AI分析**的长文本字段，然后将完整的AI输出放在那里。

# 阶段6：人工审核

不要让AI做最终决定。

创建一个名为：**需要人工审核**的Airtable视图

过滤器：
- 状态 = AI已分析
- 整体信号评分 大于 60
- 人工审核 未选中

每天审核这个视图。

问：

- 买家清晰吗？
- 痛点具体吗？
- 绕路方法丑陋吗？
- 有购买意向吗？
- 这可能会反复发生吗？
- 我能手动解决这个问题吗？
- AI能改善这个过程吗？

然后设置：
- 人工审核 = 已选中
- 状态 = 高信号 或 低信号 或 已拒绝

这是你的判断力提高的地方。

AI可以挖掘。  
你来决定什么是金子。

# 阶段7：每周对痛点进行聚类

一旦你有30到100个高信号，对它们进行分组。

创建一个名为：**本周高信号**的视图

过滤器：
- 状态 = 高信号
- 发现日期 = 最近7天内

将这些记录复制到ChatGPT中，或者以后在Make中自动化这个过程。

使用此提示：

```
You are a startup research analyst.

I am giving you high-quality customer pain signals.

Your job is to cluster them into repeated business opportunities.

Do not invent anything.
Only use the evidence provided.

For each cluster, return:

1. Cluster name
2. Buyer segment
3. Workflow
4. Core pain
5. Evidence count
6. Best customer quotes
7. Current workarounds
8. Competitors mentioned
9. Why existing solutions seem inadequate
10. Urgency level
11. Willingness-to-pay evidence
12. Manual MVP idea
13. Landing page test idea
14. Opportunity score out of 100
15. Verdict: build test / watch / ignore

Here are the signals:

[PASTE SIGNALS]
```

然后在痛点集群表中创建记录。

# 阶段8：对每个机会评分

使用此评分系统。

- 数量和重复性：20
- 痛苦严重程度：20
- 紧迫性：10
- 绕路方法的丑陋程度：10
- 买家意向：10
- 与现有工具的差距：15
- 货币化可行性：10
- 构建可行性：5

然后应用扣分项：

- 重大法律/平台风险：-15
- 买家身份薄弱：-10
- 分发路径薄弱：-10
- 仅靠炒作的趋势：-10

使用此提示：

```
You are my brutally honest startup opportunity scorer.

Score this pain cluster out of 100.

Use this scoring model:

- Volume and recurrence: 20
- Pain severity: 20
- Urgency: 10
- Workaround ugliness: 10
- Buyer intent: 10
- Gap vs existing tools: 15
- Monetisation plausibility: 10
- Build feasibility: 5

Apply deductions:
- Major legal or platform risk: minus 15
- Weak buyer identity: minus 10
- Weak distribution path: minus 10
- Hype-only trend with thin evidence: minus 10

Output:

1. Total score
2. Why it scored this way
3. Evidence supporting the score
4. Evidence against the score
5. Biggest assumption
6. Manual MVP version
7. Landing page test
8. Recommended next step
9. Verdict: build test / watch / ignore

Pain cluster:

[PASTE PAIN CLUSTER]
```

只测试评分70分以上的集群。

任何低于70分的都进入观察列表。

# 阶段9：将一个集群转化为商业想法

选择一个强集群。

不要选五个。

使用此提示：

```
You are a positioning strategist.

Turn this pain cluster into 10 sharp business offers.

Pain cluster:
[PASTE CLUSTER]

Customer quotes:
[PASTE QUOTES]

Current workaround:
[PASTE WORKAROUND]

Competitors or alternatives:
[PASTE COMPETITORS]

Use this format:

I help [specific buyer] achieve [specific outcome] without [painful thing] by using [new mechanism].

For each offer, include:
- Buyer
- Outcome
- Pain removed
- New mechanism
- Why it might work
- Weakness

Then choose the strongest offer.

Rules:
- Be specific.
- Avoid hype.
- Avoid vague words like optimise, streamline, empower, transform, or revolutionise.
- Use customer language.
```

# 阶段10：创建登陆页面测试

还不要构建产品。

构建一个测试页面。

使用Carrd、Framer、Lovable、Bolt、v0或Webflow。

登陆页面结构：

- 主标题
- 问题要点
- 适合谁
- 旧方式 vs 新方式
- 如何运作
- 手动测试版/早期访问行动号召
- 验证表单
- 常见问题

使用此提示：

```
Create landing page copy for this validation test.

Target buyer:
[INSERT BUYER]

Problem:
[INSERT PROBLEM]

Customer quotes:
[INSERT QUOTES]

Current workaround:
[INSERT WORKAROUND]

Offer:
[INSERT OFFER]

Primary CTA:
Apply for the manual beta

Rules:
- Be honest that this is early access or a manual beta.
- Use customer language.
- Do not use fake testimonials.
- Do not make unsupported claims.
- Keep it clear, specific, and conversion-focused.
- Write in plain British English.
- Avoid hype words.

Include:

1. Hero headline
2. Subheadline
3. CTA button text
4. Pain bullets
5. Who this is for
6. Old way vs new way
7. How it works
8. What you get
9. FAQ
10. Final CTA
11. Validation form questions
```

# 阶段11：创建验证表单

使用Tally。

表单不应该只是收集邮件地址。

问一些能证明痛点的问题。

问题：

1. 最能描述你的是什么？
2. 你今天是如何解决这个问题的？
3. 这个问题多久发生一次？
4. 最烦人的部分是什么？
5. 这每周要花你多少时间？
6. 你已经尝试过任何工具了吗？
7. 那些工具未能解决什么问题？
8. 你会尝试手动测试版吗？
9. 如果这解决了问题，你会付费吗？
10. 你愿意接受一个15分钟的通话吗？
11. 电子邮件地址

# 阶段12：手动驱动流量

这是大多数人躲避的地方。

你需要真实的人类。

发送20到50条消息。

使用LinkedIn、X、Reddit、你的网络或小众社区。

# 阶段13：之后添加直接API

一旦系统运行良好，再添加直接API。

这是我添加它们的顺序。

**YouTube API**

使用它从你的细分市场的视频中提取评论。

**X API**

当你想要更好的实时社交痛点时使用这个。

**Reddit API**

在subreddit中搜索问题短语。

提取帖子标题和评论。

不要用Reddit内容训练模型。

遵守删除/商业使用规则。

---

**你已经构建好了！！！**

没有人想听的部分：

这个系统不会消除对品味的需求。  
它不会消除判断力。  
它不会消除销售。  
它不会消除客户对话。

**要点：**

每个人都在尝试把AI当作一台想法机器。

那是弱版本。

更强的版本是把AI当作一个痛点雷达。

重要的是：

- 不要向AI要随机的创业想法。构建一个从真实对话中找到反复出现的客户痛点的系统。
- 不要像地鼠一样爬取数据。使用官方API、经过批准的监控工具和干净的收集方法。
- 不要仅仅从投诉中构建。对机会进行评分，测试登陆页面，与买家交谈，先销售手动版本。

**现在就去找那个100倍回报的想法！！！**
