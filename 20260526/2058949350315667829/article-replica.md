# 我如何把 Claude Code 用成自己的投资研究分析师

**作者：** leopardracer ([@leopardracer](https://x.com/leopardracer))  
**日期：** 2026年5月26日  
**来源：** [How I Set Up Claude Code as My Investment Research Analyst](https://x.com/leopardracer/status/2058949350315667829)

如果你是搞金融的，大概有过这么一刻：你瞄了一眼 Claude Code，然后默默把视线移开了。

一个黑乎乎的终端，几行看不懂的命令。一看就是给工程师用的，跟你这种整天泡在电子表格和年报里的人，好像没什么关系。

我以前也是这么想的。可现在，我整个投资研究的活儿，已经在 Claude Code 上跑了六十天——筛选、抓数据、建模型、写报告、盯组合，全在上面。有意思的是，大概到第三天，那个终端就不吓人了；到第十天，我干脆不再打开 Claude 来做研究了。

有件事当初没人跟我讲，我想讲给你听：你想写代码，它就是写代码的工具；你想做饭，它就是做饭的工具；你想购物，它就是购物的工具。而你要是真心扑在金融上，它一样能是做金融的工具。

说白了，名字里那个"code"，是这个产品最容易把人劝退的地方。

这篇文章，就是我当年第一天最想有人塞给我的那份上手指南。读完它，你会装好 Claude Code，搭起一个会越用越厚的研究知识库，再外接三个工具，让它能伸手够到实时网络、能开浏览器、能查你自己的笔记本。

如果你看过配套那段视频，应该对它的样子有个印象。这篇会讲得更细一些——具体的提示词、文件怎么放，还有那几条让整套东西真正转起来的规矩。

我们先从一个想法说起，正是它，彻底改了我对这件事的看法。

## Claude 和 Claude Code：那个没人跟你讲清楚的区别

Claude 和 ChatGPT 是聊天机器人。你问一句，它答一句；你再问，它再答。挺有用，但也就到这儿了——你们之间，就是一场对话。

Claude Code 不一样。打个比方，它是长了手的 Claude。

这话什么意思？想想你让 ChatGPT 帮忙做研究的样子。你可以让它筛几只股票，可以把财报贴进去让它做个 DCF，可以把草稿丢给它让它润润色。可这些都是一步一步的，而你呢，始终夹在中间，在聊天框和正经活儿之间不停地复制、粘贴。

可一个真实的研究流程是什么样？你得先筛一遍整个股票池，按几个标准列出候选，再套上公司内部那套框架，挑出两只来；然后把两家的财报拉出来，建模型，做压力测试，算出内在价值，写成一份股票研究报告，交给资深分析师审一遍，最后发出去。

这么长一条链，聊天机器人只能陪你走其中一步。Claude Code 能从头跑到尾。

你把最终目标交给它就行。要开浏览器，它自己开；要抓数据，它自己抓。它会写文件、读文件，活儿允许的话还能同时铺开五件事一起干。只有真碰上需要你拍板的地方，它才回头问你一句。其余时间，这些活儿是在你忙别的的时候，悄悄替你做掉的。

这就是"手"的意思。ChatGPT 是一个你跟它聊天的大脑；Claude Code 是一个替你把活儿干完的大脑。

有句话我老是想起：聪明又勤快的人，靠多做来多成；而真正通透的人，靠少做来多成。Claude Code 干的就是"帮你少做"这件事。咱们嘴上说的"研究工作"，仔细一看，大半其实是收集数据、排格式、复制、粘贴、来回切标签页。Claude Code 把这些杂活儿从你手里端走，只把真正得你亲自来的那部分留下。

钥匙就在这儿。这篇文章剩下的全部内容，无非是教你怎么把它装好、调好。

## 第一步：装上 Claude Code（这步最省事）

如果你更想看着整个过程在屏幕上跑一遍——包括下一节 Playwright 和 Firecrawl 的安装——我录了段 16 分钟的演示，从头到尾都覆盖了：

先去 Anthropic 官网的 Claude Code 页面。你会看到两条安装命令，一条给 Mac，一条给 Windows，复制适合你机器的那条就行。

官方设置文档在这儿：https://code.claude.com/docs/en/quickstart

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmZkMGMwNDNiNTBhYzA1ZTk0ZWVkN2E0Yzc0YjA3Y2RfNDFkM2FmNzYzYWYzMjE5YThkZWEzMDU3NGRkMjU3ZDVfSUQ6NzY0NDAwMjAzMTI2Mjg3ODkzMV8xNzc5NzU3OTM2OjE3Nzk4NDQzMzZfVjM)

Mac 用户打开 Terminal，Windows 用户打开 PowerShell。把命令粘进去，回车，等一分钟。装完了。

接着输入 `claude` 再回车，Claude Code 的输入框就出来了。你直接拿大白话跟它说话就行，想问啥问啥。比如打一句"嗨，我是新手，该从哪儿开始？"，它就会告诉你。

就这么简单。安装到此为止。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzYwYjQzZDdkOGFlMzRhOTY2YjRhZjMxOGQwOTYxNjVfMDYxMTRmZTIwMmJhZmE2ZDEwY2VmOWMzODY0MDE5NzVfSUQ6NzY0NDAwMjA0MDg2Nzc2OTU1N18xNzc5NzU3OTM2OjE3Nzk4NDQzMzZfVjM)

往下走之前，还有一样东西要装：Cursor。

官方页面在这儿：https://cursor.com/home

别误会，Cursor 不是用来替代终端的，它是这套系统其余部分安家的地方。等下一节你搭 Obsidian 知识库时，会把那个仓库当成一个文件夹，在 Cursor 里打开。到时候 raw、wiki、output 几个文件夹都排在侧边栏里，Claude Code 就在旁边一个面板里干活。文件什么时候被建出来、改了哪儿、又被索引进去，你在同一个窗口里全看得见。从这往后，你搭的所有东西，都在这一个地方发生。

你要是还想用普通终端，当然也行。我有时也用，特别是想盯着 Claude Code 慢慢啃一件复杂活儿的时候。但日常真正干活的地方还是 Cursor——因为只有在这里，知识库、对话和工具,你能一眼全看到。

Claude Code 光是装上，确实有用，但它还不是让这套系统转起来的关键。装它两分钟就够了，真正能改变你研究方式的设置，是接下来这部分。

### 一个可选项：要是你不想买 Claude 订阅

往下之前插一句。后面的内容，都默认你有个 Claude 订阅，Pro 或者 Max 都行。要是你没有，又不想为了试个水就专门买一个，有个能顶上的替代品叫 MiniMax M2，它能当成替换引擎接进 Claude Code，花的钱大概只有原来的百分之七。把它配好，再回来从下一节接着读，后面的一切用起来都一模一样。

## 第二步：把 Obsidian 变成 Claude Code 的记忆

Claude Code 本身是没记性的。每开一次新会话，它都从一张白纸开始。你周一跟它聊得再投机，关掉终端，周二它就什么都不记得了。做编程的活儿，这没啥；可做研究，麻烦就来了。研究这东西是会一点点攒起来的——你三月份给一家半导体公司记的笔记，到了十一月还得找得到才行，最好还能跟你这大半年攒下的行业理解摆在一块儿。

Obsidian 解决的就是这个。它是个免费小工具，能把你电脑上的一个文件夹，变成一座属于你自己的研究图书馆。每条笔记都是一个纯文本文件。你能把笔记互相挂上钩，按主题归进不同文件夹，还能一下子搜遍整座库。没有数据库，没有云，也不怕被谁绑死。你的研究就老老实实待在自己机器上，存在随便哪个文本编辑器都能打开的文件里。

妙就妙在：Claude Code 能读写的，正是这同一个文件夹。一旦配好，Obsidian 就成了 Claude Code 的长期记忆。你等于给它派了个"图书管理员"的活儿：你收集来的东西，它替你归档；你读过的内容，它替你总结；不同主题里相关的想法，它替你挂上钩；往后你每问一个问题，它都先去这座库里翻。日子一久，这座库越来越聪明——因为它给你的每一个答案，转头又被归档了回去。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODljYTk5MjgyZTA2YTA2NmM3NzEyOTE0YWVjZDJhMWVfNDJmNzdiNmViNTk2ZWQ2OTE3YmIzYWIxNjcxNDQyOWNfSUQ6NzY0NDAwMjA1MDY5NDY2MzM0OV8xNzc5NzU3OTM2OjE3Nzk4NDQzMzZfVjM)

下面就讲怎么把它搭起来。

### 装好 Obsidian，建一个仓库

去 obsidian.md 下载 Obsidian。个人用免费，Mac、Windows、Linux 都能跑。

打开它，点"创建新仓库"。说穿了，仓库就是你电脑上专门放 Obsidian 笔记的一个文件夹。名字随便取（我的就叫 Vault）。位置挑个你记得住的，搁在 Documents 文件夹下某处就行。点完，Obsidian 会打开这个空荡荡的仓库。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTE4NjYxNDIxZDIyYTM1MTcyN2FhNGZkNDNkODljNDdfMGRmNzdlZTc5M2NkZTMwZWExMjZmOTcyYzBiNTdlMmVfSUQ6NzY0NDAwMjA1Njc5NzkxNjM3Nl8xNzc5NzU3OTM2OjE3Nzk4NDQzMzZfVjM)

接着，在 Cursor 里打开同一个仓库文件夹。文件 → 打开文件夹 → 选中你那个仓库。你应该能看到文件夹的名字出现在 Cursor 侧边栏里，现在还是空的。从这儿往后，一切都在这里发生。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDE2ZTYzMjc2MzJkNTZkNTAzNTBhY2JhY2I1NTM3YjRfMDJjYzgyYjNiNGRiYTM4NGJkNzk4NzMxMzY3ZmFkYzNfSUQ6NzY0NDAwMjA2NTg2NjA5OTkyNV8xNzc5NzU3OTM2OjE3Nzk4NDQzMzZfVjM)

### 把文件夹结构搭出来

在 Cursor 里打开 Claude Code（用侧边栏面板还是终端，随你）。把下面这段提示词一字不差地粘进去：

```
为我的知识库创建这个文件夹结构：

- raw/ — 这是我的收件箱，我会把源材料丢进这里
- wiki/ — 这是你的地盘，你会在这里写和维护一切
- 在 wiki/ 里创建一个 _master-index.md，标题为"Knowledge Base Index"，
    并附一条说明，写着"主题将在创建时列在这里。"
- output/ — 这是查询结果和报告存放的地方

只创建这些文件夹和那一个文件。其他暂时什么都不要做。
```

Claude Code 会建好三个文件夹和一个文件。打开 Obsidian，你就能在侧边栏里看到它们。这就是你的骨架。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTRmYjZkNGE0ZWI2ZWY2MDI1NWFiMjVkY2I0YWU0ZmZfNzFhYTJiYWVjODAzODFiZGU1YTljZDM5MDgxMzdmZGFfSUQ6NzY0NDAwMjA3Mjc4MjcwMzgyOF8xNzc5NzU3OTM3OjE3Nzk4NDQzMzdfVjM)

三个文件夹，各管一摊。raw/ 是收件箱，凡是你想让系统学的东西，都往里丢：文章、访谈记录、截图、随手记的笔记。wiki/ 是图书管理员的地盘，Claude Code 在这儿写结构化的总结，按主题归好，再维护一份把全部内容串起来的主索引。output/ 是放成品的地方：研究报告、查询答案，还有那些你想跟图书馆本身分开存的分析。

### 规矩手册（CLAUDE.md）

这是整套系统里最要紧的一个文件。CLAUDE.md 就是一本规矩手册，每次你在这个仓库里打开 Claude Code，它都先把这本手册从头读一遍。规矩你只写一次，它就一直照办。没有这个文件，Claude Code 不过是个挺聪明的帮手；有了它，Claude Code 才是个守规矩的图书管理员。

在仓库的根目录建一个文件，就叫 CLAUDE.md（注意，不是塞进那三个文件夹里头，而是跟它们并排放着）。把下面这段粘进去：

```
这个文件告诉你如何在每次会话中维护这个知识库。

## 知识库规则

- 这是一个由 LLM 维护的知识库。你是图书管理员。
- wiki/ 文件夹是你的地盘 —— 你写和维护它里面的一切。
  我很少直接编辑 wiki 文件。
- raw/ 是收件箱。当我把文件丢进这里，你在一个"compile"步骤里
  把它们处理进 wiki。
- wiki/_master-index.md 是入口点。它列出每个主题文件夹，
  附一行描述。始终保持它最新。
- 每个主题在 wiki/ 里有自己的子文件夹（例如 wiki/ai-agents/），
  带自己的 _index.md，列出该主题下所有文章并附简短描述。
- 始终用 [[wiki links]] 来连接跨主题的相关概念。
- 编译原始材料时：
  1. 读取原始文件
  2. 决定它属于哪个主题（或创建一个新主题）
  3. 写一篇带关键要点和相关链接的 wiki 文章
  4. 更新该主题的 _index.md
  5. 更新 wiki/_master-index.md
  6. 如果一个原始文件跨多个主题，在两边都创建文章并交叉链接
- 文章保持简洁 —— 用要点而非段落。
- 每篇 wiki 文章里都包含一个 ## Key Takeaways 小节。
- output/ 用于查询结果和生成的报告。
- 回答问题时，先读 _master-index.md 来导航，然后
  钻进相关主题的 _index.md，再读具体文章。
- 当我说"compile"时，把 raw/ 里所有还没编译的东西
  处理进 wiki。
- 当我说"audit"或"lint"时，审查 wiki 里的不一致、
  断链、空缺，并提出改进建议。
```

存好这个文件。从此以后，每开一次会话，Claude Code 都先把这本手册读一遍。

### 每天往里喂料：Web Clipper

Web Clipper 页面：obsidian.md/clipper

你得有个法子，能把文章弄进 raw/ 文件夹，又不用一遍遍复制粘贴。办法就是给浏览器装一个 Obsidian Web Clipper 扩展（Chrome、Brave、Edge、Firefox 都支持）。

打开 Web Clipper 设置，把你的仓库加进去，再去 Templates 里改一下 Default 模板：

```
Vault: 选择你的仓库
Note location: raw
Note name: {{date|date:"YYYY-MM-DD"}}-{{title|safe_name}}
```

这下，你在网上读到的任何文章，点一下，就变成收件箱里一个干干净净的 markdown 文件。一份财报电话会记录、一篇 FT 的报道、一段 10-K 摘录、一篇 Substack 帖子——都用同一个动作剪下来。

还有个可选的小插件值得一提：在 Obsidian 里装上 Local Images Plus（设置 → 社区插件 → 浏览 → 搜"Local Images Plus"）。往后你打开一条剪下来的笔记，它会把文章里每张图都下载进你的仓库。这样哪天原网页挂了，你的库还是完好的。

### 每天的活儿：四个动词

都配好之后，每天的活儿就归成四个动词。

**剪（Clip）。** 看到值得留的东西，在浏览器里点一下，它就掉进 raw/。你不用想它该往哪儿放，也不用写总结，剪下来就完事。

**编（Compile）。** 一周一次，或者收件箱一满，就打开 Claude Code 敲一句：

```
把 raw/ 里的所有东西编译进 wiki。对每个文件：
1. 读它并识别核心主题
2. 在 wiki/ 里创建或找到合适的主题文件夹
3. 写一篇带总结、关键要点和 [[wiki links]] 的 wiki 文章，
   链接到任何相关概念
4. 更新该主题的 _index.md
5. 更新 wiki/_master-index.md

在相关的地方跨主题交叉链接。
```

Claude Code 会一篇篇读你剪下来的文章，判断它归哪个主题，写成一条结构清楚的总结笔记，归进对的文件夹，再把索引更新好。等你喝完一杯咖啡，收件箱空了，库又厚了一圈。

**查（Query）。** 拿问题去问这座库。简单的："上个月我剪的那份贝恩半导体报告，关键结论是啥？"要串着看的："中国汽车出口放缓，跟我最近读的那些大宗商品需求的东西，有没有关系？"还有那种把答案再存回库里的综合问题："把 wiki 里的内容都过一遍，印度特种化学品的看多理由和看空理由各是什么？把答案存成一篇新的 wiki 文章，并链回你引用的来源。"

最后那种问法，才是让整套系统越滚越大的关键一招。你问的每个问题都变成一条新笔记，每条笔记又都链回它的出处。你每用一回，这座库就更聪明一分。

**审（Audit）。** 一个月一次，敲一句："审一遍这个 wiki。把不一致的地方、断掉的链接、缺的交叉引用、覆盖不到的空白都找出来。先别动手改，给我一份报告就行。"Claude Code 会把整座库走一遍，告诉你哪儿开始含糊了。至于改不改、改哪儿，你说了算。

整套系统，就是这么回事。收件箱、图书管理员、图书馆、输出口。四个文件夹，一本规矩手册，四个动词。

说到底，这件事比看上去要紧的地方在于：这套系统本身，就是一种纪律。装 Obsidian 和 Claude Code，谁都会装。可你的研究之所以能越攒越多、而不是一路漏光，靠的正是那本规矩手册逼出来的一致性——每次剪藏都用同一种方式归档，每份总结都长一个样，每次查询都能调动你读过的一切。这套系统跑满六十天后，我随口问 Claude Code 一句"这个季度我在仓位管理上学到了点啥"，不到一分钟，就能拿到一个实打实的答案，里头引的，还是些我自己都快忘了曾经剪过的文章。

接下来，我们再给它加上一双手，让它能伸出图书馆，够到外面那个活生生的网络。

## 第三步：给 Claude Code 一双能上网的手（Playwright + Firecrawl）

你刚搭好的知识库很厉害，可它也是个封闭的——你喂它什么，它才知道什么。真要做研究，你得让 Claude Code 能伸到实时网络里去：从筛选器里拉一张资产负债表，扒一个投资者关系页面，搜一搜你正盯着的那家公司最新的备案文件。接下来这两个工具，干的就是这个。

Playwright 让 Claude Code 能开一个真浏览器；Firecrawl 让它能大批量地搜网、扒网。两个都免费、都开源，各两分钟就装好。打个比方你就懂了：一个图书管理员只读你带回家的书，另一个还能自己跑到城那头的图书馆，把你要的东西取回来——这两个工具，就是这两者之间的差别。

### Playwright：那个浏览器

Playwright 是微软出的一个浏览器自动化工具。装好之后，Claude Code 就能开浏览器、跳到任意页面、点按钮、填表单、登账号、读屏幕上的内容——全程不用你碰一下鼠标。

对金融这行来说，数据藏在交互背后的地方特别多，这时它就派上用场了。比方说，一个非得你设满十个筛选条件才肯出结果的筛选器；一个把季度数字塞在下拉菜单里的投资者关系页面；一个非得你先点掉免责声明才让你下文件的监管门户。凡是因为"对面认定得是个真人操作"而把普通抓取器挡在门外的地方，Playwright 都能让 Claude Code 装成那个真人。

要装它，就在你的仓库里打开 Claude Code，粘这段进去：

```
我想安装微软的 Playwright CLI，这样你就能代表我驱动浏览器。
仓库在 https://github.com/microsoft/playwright-cli。
请为我的 [Mac / Windows] 机器一步一步带我走完安装，
对新手友好，并运行你需要运行的命令。
```

Claude Code 会替你装好，中间有什么提示也会带着你一步步过，弄完了告诉你一声。装完想试试？问个简单的就行："开个浏览器，去 screener.in，告诉我首页上有什么。"要是装对了，一个浏览器窗口会弹出来，跳到那个页面，然后 Claude Code 把它看到的内容回给你。

### Firecrawl：那个网络抓取器

Firecrawl 干的活儿不太一样。Playwright 是一个手把手操作的浏览器，Firecrawl 则是一条又快又自动的路子：从任意网页里把干净的正文拉出来，或者跑一次网络搜索，把排在前头的结果正文一并拿回来。它会把找到的东西，转成 Claude Code 能直接读的、干干净净的 markdown 文件。

有个用法，金融人一看就明白：你想从 Finviz 拉最近两周的内幕交易数据；你想从某家公司的 IR 页面扒一份年报；你想搜"印度特种化学品的最新新闻"，把前十篇文章拉进知识库。这三件事，Firecrawl 各一条命令就办了。

要装它：

```
我想安装 Firecrawl CLI，这样你就能代表我搜索和抓取网络。
官方文档在 https://docs.firecrawl.dev/sdks/cli。
请为我的 [Mac / Windows] 机器一步一步带我走完安装，
对新手友好，并给我每一条我需要运行的命令。
```

装好之后，Firecrawl 就成了 Claude Code 在终端里随手能调的一件工具，你不用每回都亲自喊它。一碰上需要上网才能干的活儿，Claude Code 自己就认出来"手边有 Firecrawl"，顺手就用上了。

### 实际跑起来是什么样

下面是我上周真跑过的一条提示词。当时的情况是：我想把钱分到五只标的上，可看好的名单上只有两只，还差三只。

```
我在筛选要部署资金的标的。去 finviz.com，拉取美国上市公司
最近两周的内幕交易数据。分析这些数据，找强烈买入信号。
给我一份前 10 的观察名单，每只标的都附上理由。
也标出危险信号和要避开的标的。
```

Claude Code 问我能不能用 Firecrawl，我说行。它就去了 Finviz，把数据拉下来、理顺，跑了一遍买入信号的判断，又拿基本面交叉对了一遍，最后端回来一份排好序的十只标的清单。每只都配着一段论点、一份内幕买入记录（谁买的、啥时候买的、买了多少）、几条关键风险，外加一张总结评分卡。从头到尾，三分钟。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjlkNWYzZmI5NjRjZGZjMDY2YzAxMjA1NjQyMjhiMjZfMDk2Y2Q0MDgwNWJjYTI4ZmNlZjRiOGVlZjcwMjczYjZfSUQ6NzY0NDAwMjA4MjU2NzY1NDYxMl8xNzc5NzU3OTM3OjE3Nzk4NDQzMzdfVjM)

这事儿要让我自己手动来，少说也得一个半小时，而且在 Finviz 和 Excel 之间倒腾数据，难免抄错几个数。Claude Code 连终端都没出，就干完了。

### 关于权限，说一句

每回 Claude Code 想用个工具——比如 Firecrawl 或 Playwright——或者想改个文件、跑条命令，它都会先问你一声。默认就是这样：每隔几步弹一个"行还是不行"。你刚上手时，这挺有用；可一旦你信得过这套系统了，就嫌它烦了。

有个开关叫 `--dangerously-skip-permissions`，把它一开，这些提示就全没了。这时候 Claude Code 想用什么工具、想改你仓库里哪个文件、想跑什么命令，都不再回头问你。这名字听着是有点吓人——它本来也该吓人，因为你这等于是把整个工作目录的钥匙，全交到了 Claude Code 手里。

这开关我开着跑了六十天。啥事没出：没误删过文件，没跑过不该跑的命令，安全上也没出过岔子。唯一变的是，我不用再守在终端前等着点"行"了，丢给它一个任务，转身就走。等我端着咖啡回来，活儿干完了。

这之所以靠得住，靠的还是那本规矩手册。CLAUDE.md 把 Claude Code 该干啥、边界在哪都写明白了；再加上它只能碰你打开的那个仓库文件夹、碰不到你整台机器——风险其实比这开关的名字听起来小得多。我的建议是：头一周先开着权限跑，你好看清它都在干些什么；等你摸清了它的路数，再把权限关掉，放手让它干。

当然，这是个人选择。有人愿意一直开着权限，那也完全没问题。两种用法，系统照样转得动。

## 这六十天，我学到了什么

上面这套设置，前后大概一个钟头。可它搭出来的这套系统，我跑了六十天，到现在还在慢慢摸索怎么用得更顺。

有几件事，挺出乎我意料的。

头一件，是那个终端多快就不像个编程工具了。第一周还没过完，我往 Claude Code 里打字，就跟往 ChatGPT 里打字一个样了——大白话，不用命令，不用语法。大家老挂在嘴边的那种"怕"，第一天是真有，到第三天就没影了。你要是个搞金融的，正卡在"要不要试"这道坎上，那我告诉你：你犯愁的这个事儿，撑不过第一次会话。

第二件，是当你不再把自己当成"一个用聊天机器人的人"，而开始把自己当成"一个调度工作流的人"，会发生什么。这个转变挺微妙，可它一变，下游全跟着变了。你不再让 Claude Code"帮你"做某一件小事，而是把整摊活儿一股脑甩给它：把这些标的筛一遍，过一遍这套框架，给活下来的那几只拉财报，建模型，每只再写一页纸。你把最终目标交给它，转身就走。活儿在后台慢慢跑，你回来时，迎接你的是一整文件夹的成品。

第三件，是我才意识到，从前我的研究漏掉了多少。用这套系统之前，我的研究散得到处都是：Notion 里有，Apple Notes 里有，浏览器书签里有，五个不同文件夹里下的 PDF 里也有，还有个我难得打开的 Substack 草稿夹。同一个想法，我能重新"发现"两遍，有时甚至三遍。Obsidian 知识库把这事给了结了。现在我读的一切都落到一个地方，被 Claude Code 归进对的主题，等六个星期后我问起相关的问题，它又给我翻出来。什么都不漏，东西就这么一点点攒厚。

还有个工具值得你知道：NotebookLM。它是谷歌托管的研究工具，解决的问题跟 Obsidian 不一样。Obsidian 是你的图书馆；NotebookLM 更像是专门为某一个研究对象支起的工作台——一家公司、一个行业、或者一摞备案文件。你把材料传上去，它就只在这堆材料里头，给你有出处、带引用的答案。还有个 Python 封装，能让你从 Claude Code 里头直接查一个 notebook。这意味着你能搭出这么一个流程：在同一条提示词里，Claude Code 既从你的 Obsidian 图书馆里取料，又从一个专门的 NotebookLM 材料集里取料。

## 接下来还有什么

这篇文章是一个系列里的第一块。地基既然打好了，后面几篇会一头扎进具体的金融工作流：一个完整的、从头到尾都在 Claude Code 里跑的股票研究流程；一个市场出事之后、帮你把客户电话排出先后的财富管理流程；一个每月一次的会计审计流程；还有一个跑在虚拟服务器上、一有事就主动给你发消息的组合监控系统。这些，每一个都建在你刚搭好的这套系统上头。

要是你想等这个系列陆续更新时第一时间读到后面的内容，那你读着这篇，就已经站对地方了。

你想写代码，它就是写代码的工具；你想做饭，它就是做饭的工具；你想购物，它就是购物的工具。而你要是真心扑在金融上，它就是眼下你能装进自己机器里的、最趁手的研究工具。你花在这套设置上的那一个钟头，就是你的研究从"一路漏光"转向"越攒越厚"的那一个钟头。

就是这么回事。

要是这篇对你有用——欢迎关注我的 telegram 频道：https://t.me/+ygATQAt9sUM1N2U6
