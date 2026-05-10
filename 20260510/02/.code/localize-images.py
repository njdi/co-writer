from __future__ import annotations

from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "images"
FONT_REG = "/System/Library/Fonts/STHeiti Light.ttc"
FONT_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_MONO = "/System/Library/Fonts/STHeiti Medium.ttc"


def font(size: int, bold: bool = False, mono: bool = False):
    return ImageFont.truetype(FONT_MONO if mono else (FONT_BOLD if bold else FONT_REG), size)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt) -> tuple[int, int]:
    if not text:
        return (0, 0)
    box = draw.multiline_textbbox((0, 0), text, font=fnt, spacing=4)
    return box[2] - box[0], box[3] - box[1]


def wrap_by_width(draw: ImageDraw.ImageDraw, text: str, fnt, max_w: int) -> str:
    lines: list[str] = []
    for raw in text.split("\n"):
        cur = ""
        for ch in raw:
            trial = cur + ch
            if draw.textlength(trial, font=fnt) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = ch
        lines.append(cur)
    return "\n".join(lines)


def center_text(draw, box, text, fnt, fill, spacing=4):
    x1, y1, x2, y2 = box
    w, h = text_size(draw, text, fnt)
    draw.multiline_text((x1 + (x2 - x1 - w) / 2, y1 + (y2 - y1 - h) / 2), text, font=fnt, fill=fill, align="center", spacing=spacing)


def left_text(draw, xy, text, fnt, fill, max_w=None, spacing=6):
    if max_w:
        text = wrap_by_width(draw, text, fnt, max_w)
    draw.multiline_text(xy, text, font=fnt, fill=fill, spacing=spacing)


def box(draw, xy, fill, outline, radius=14, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw, start, end, fill=(150, 150, 150), width=3):
    draw.line([start, end], fill=fill, width=width)
    x1, y1 = start
    x2, y2 = end
    if abs(x2 - x1) > abs(y2 - y1):
        sign = 1 if x2 > x1 else -1
        pts = [(x2, y2), (x2 - 12 * sign, y2 - 8), (x2 - 12 * sign, y2 + 8)]
    else:
        sign = 1 if y2 > y1 else -1
        pts = [(x2, y2), (x2 - 8, y2 - 12 * sign), (x2 + 8, y2 - 12 * sign)]
    draw.polygon(pts, fill=fill)


def save(im: Image.Image, name: str):
    im.save(IMG / name, quality=94, subsampling=0)


def img03():
    W, H = 492, 1199
    im = Image.new("RGB", (W, H), "#202020")
    d = ImageDraw.Draw(im)
    white = "#eeeeee"
    grey = "#bfbfbf"
    mono = font(8, mono=True)
    mono_b = font(9, mono=True)

    def ascii_box(x, y, w, h, title, lines):
        d.rectangle((x, y, x + w, y + h), outline=white, width=1)
        d.text((x + 8, y + 7), title, font=mono_b, fill=white)
        d.line((x + 8, y + 28, x + w - 8, y + 28), fill=white, width=1)
        yy = y + 36
        for line in lines:
            d.text((x + 8, yy), line, font=mono, fill=white)
            yy += 11

    ascii_box(16, 10, 196, 92, "外部：信号层", ["X书签、文章", "转录稿、私信、回复", "竞品帖子", "用途：改写、研究+构思"])
    ascii_box(264, 10, 196, 92, "内部：知识图谱", ["个人OS、笔记", "日记、语音备忘录", "已发布内容存档", "用途：原创、再加工"])
    arrow(d, (246, 105), (246, 136), white, 1)
    ascii_box(17, 147, 454, 82, "基础层", ["策略   定位、受众、支柱、来源清单", "声音   声音档案、避免烂内容文档", "存储   收件箱、想法、钩子、证明、反馈日志", "模块   作者技能、参考资料、模板"])
    arrow(d, (246, 230), (246, 257), white, 1)
    ascii_box(17, 262, 454, 47, "想法门", ["选择路线；写入 content-object.md"])
    labels = [
        ("原创", ["来自第二大脑", "无外部来源"]),
        ("再加工", ["延展自有内容", "换形式，骨架不变"]),
        ("改写", ["外部素材", "保留什么", "注明出处"]),
        ("研究+构思", ["探索+角度", "不直接出稿", "存入想法库"]),
    ]
    xs = [64, 158, 252, 356]
    for x, (t, lines) in zip(xs, labels):
        arrow(d, (x + 12, 310), (x + 12, 328), white, 1)
        ascii_box(x - 47, 329, 92, 91, t, lines)
    arrow(d, (246, 421), (246, 452), white, 1)
    ascii_box(112, 465, 238, 103, "运行文件夹（每个内容对象一个）", [
        "content-object.md   路线/状态/下一步",
        "idea.md             想法门决策",
        "brief.md            作者交接包",
        "draft-package.md    草稿+验证输出",
        "feedback.md         24h/72h学习",
    ])
    arrow(d, (246, 568), (246, 600), white, 1)
    ascii_box(38, 603, 195, 91, "作者（Opus 4.7）", ["→ 品味", "→ 节奏", "→ 压缩", "→ 声音", "→ 真正的草稿"])
    ascii_box(260, 603, 195, 91, "编排者（GPT-5.5）", ["→ 层间路由", "→ 打包上下文", "→ 决定交付内容", "→ 跑验证器", "→ 交给发布层"])
    arrow(d, (246, 695), (246, 728), white, 1)
    ascii_box(90, 741, 310, 80, "验证器 + 作者审核", ["对照避免烂内容文档检查", "可收藏性、评分0-12", "低于8分退回重写", "通过后进入调度队列"])
    arrow(d, (246, 821), (246, 852), white, 1)
    ascii_box(90, 865, 310, 70, "发布层", ["X、领英、Threads、Instagram", "TikTok、YouTube、Bluesky、Reddit", "自托管；已调度或已发布"])
    arrow(d, (246, 935), (246, 968), white, 1)
    ascii_box(90, 980, 310, 82, "反馈循环", ["24h  浏览、回复、书签率", "72h  书签、保存率、私信跟进", "赢家 → 示例库", "输家 → 声音规则 + 禁用模式"])
    d.text((183, 1078), "输出时持续更新", font=mono, fill=white)
    arrow(d, (246, 1062), (246, 1096), white, 1)
    ascii_box(90, 1104, 310, 60, "存储（写回基础层）", ["赢家、输家、声音规则", "禁用模式、钩子、证明", "下一包内容比上一包更准"])
    center_text(d, (0, 1170, W, 1194), "每一次循环，都让下一次更锋利", mono, grey)
    d.text((382, 1177), "@shannholmberg", font=font(8, mono=True), fill=grey)
    save(im, "img-03.jpg")


def img04():
    W, H = 1550, 488
    im = Image.new("RGB", (W, H), "#000000")
    d = ImageDraw.Draw(im)
    cards = [
        ("曝光量", "1200万", "↑ 1千%", "#62c48b"),
        ("互动率", "3.4%", "↓ -66%", "#e06a82"),
        ("互动数", "41.63万", "↑ 539%", "#62c48b"),
        ("主页访问", "1.7万", "↑ 241%", "#62c48b"),
        ("点赞", "6.42万", "↑ 178%", "#62c48b"),
        ("转发", "4900", "↑ 1千%", "#62c48b"),
        ("书签", "12.06万", "↑ 2.9万%", "#62c48b"),
        ("分享", "1.79万", "↑ 5.6万%", "#62c48b"),
    ]
    fw, fh = 350, 190
    for i, (title, val, pct, col) in enumerate(cards):
        row, col_i = divmod(i, 4)
        x, y = 17 + col_i * 385, 28 + row * 225
        box(d, (x, y, x + fw, y + fh), "#191a1f", "#30333d", 16, 2)
        d.text((x + 33, y + 38), title, font=font(30, True), fill="#c8c9cf")
        d.text((x + 33, y + 102), val, font=font(58, True), fill="#eeeeef")
        d.text((x + 173, y + 126), pct, font=font(28, True), fill=col)
    save(im, "img-04.jpg")


def img05():
    W, H = 1440, 1306
    im = Image.new("RGB", (W, H), "#20201f")
    d = ImageDraw.Draw(im)
    center_text(d, (0, 28, W, 70), "“值得收藏”的内容到底是什么", font(28, True), "#f2f2f2")
    center_text(d, (0, 76, W, 110), "书签，是读者对未来的自己许下的一个小承诺", font(24), "#d0d0d0")
    box(d, (77, 134, 1317, 284), "#403c88", "#827cd4", 16, 2)
    center_text(d, (77, 148, 1317, 276), "“我以后还会用到它”\n面向未来价值的一票 · 门槛远高于点赞\n拿到书签的帖子，会在发布很久后继续出现在信息流里", font(26, True), "#e8e8e8", 8)
    arrow(d, (697, 284), (697, 331), "#d6d6d6", 4)
    center_text(d, (0, 338, W, 370), "发布前测试：你的草稿像下面这9种格式之一吗？", font(25, True), "#555555")
    items = [
        ("清单", "可打勾 · 有边界\n未来的你会想\n再跑一遍"),
        ("蓝图", "某件具体事情的\n可运行版本\n拿来改一改就能用"),
        ("文件夹结构", "你如何组织\n某类具体工作\n读者能直接照搬"),
        ("模板", "填空式\n结构已经替你\n完成一半工作"),
        ("框架", "一种思考问题的方式\n能套用到\n很多场景"),
        ("分步工作流", "先做A再做B再做C\n不用做选择\n照着走就行"),
        ("证明 + 结论", "结果截图\n+ 从中学到什么\n可信度 + 经验"),
        ("前后对比", "展示变化\n读者能想象\n自己也这么做"),
        ("可复用心智模型", "一种视角\n永久改变你\n看事情的方式"),
    ]
    x0s = [77, 497, 917]
    y0s = [377, 558, 739]
    for idx, (t, body) in enumerate(items):
        x, y = x0s[idx % 3], y0s[idx // 3]
        box(d, (x, y, x + 400, y + 161), "#205947", "#63a28d", 12, 2)
        center_text(d, (x, y + 22, x + 400, y + 62), t, font(28, True), "#d7e6dd")
        center_text(d, (x + 20, y + 66, x + 380, y + 156), body, font(25), "#add6c4", 7)
    d.line((77, 962, 1317, 962), fill="#343434", width=2)
    center_text(d, (0, 976, W, 1008), "发布门", font(23, True), "#555555")
    box(d, (77, 1014, 657, 1166), "#205947", "#63a28d", 12, 2)
    center_text(d, (77, 1030, 657, 1155), "看起来像9种之一？\n可以发布 · 继续打磨格式\n让它更像值得保存的东西", font(26, True), "#d7e6dd", 8)
    box(d, (737, 1014, 1317, 1166), "#7b341e", "#c77b58", 12, 2)
    center_text(d, (737, 1030, 1317, 1155), "不像任何一种？\n通常不该发布\n重做成9种之一", font(26, True), "#f4d0c1", 8)
    center_text(d, (0, 1218, W, 1260), "未来价值 = 未来信息流存在感 · 书签会在发布很久后继续复利", font(25), "#565656")
    save(im, "img-05.jpg")


def img06():
    W, H = 954, 1396
    im = Image.new("RGB", (W, H), "#22211f")
    d = ImageDraw.Draw(im)
    center_text(d, (0, 42, W, 68), "一张图看懂这套系统", font(22, True), "#f2f2f2")
    center_text(d, (0, 75, W, 102), "每条内容都是一个对象，从想法到发布都带着自己的状态", font(18), "#dedede")
    center_text(d, (0, 108, W, 132), "上下文来自两个地方", font(18, True), "#565656")
    box(d, (54, 131, 459, 264), "#78371f", "#b76b50", 12, 2)
    left_text(d, (88, 154), "外部 · 信号层", font(21, True), "#f2d3c5")
    left_text(d, (88, 184), "X书签 · 文章 · 转录稿\n私信 · 回复 · 竞品帖子\n供给：改写 + 研究/构思", font(17), "#e0b8a7")
    box(d, (475, 131, 880, 264), "#403c88", "#817bd3", 12, 2)
    left_text(d, (510, 154), "内部 · 知识图谱", font(21, True), "#e4e1ff")
    left_text(d, (510, 184), "个人OS · 笔记 · 日记\n语音备忘录 · 内容存档\n供给：原创 + 再加工", font(17), "#c7c3f3")
    arrow(d, (255, 264), (467, 302), "#414141", 2)
    arrow(d, (675, 264), (485, 302), "#414141", 2)
    box(d, (94, 302, 840, 403), "#6b420e", "#b5803d", 12, 2)
    center_text(d, (94, 316, 840, 390), "策略 + 声音 + 存储\n定位 · 声音档案 · 避免烂内容主文档\n想法 · 钩子 · 证明库 · 反馈日志\n在来源和作者之间做精选上下文层", font(17, True), "#f2c574", 6)
    arrow(d, (467, 403), (467, 435), "#9a9a9a", 3)
    box(d, (174, 434, 760, 515), "#225b49", "#5d9f8c", 12, 2)
    center_text(d, (174, 448, 760, 505), "生产负责人\n打开运行文件夹 · 通过想法门路由 · 执行门控", font(19, True), "#cfe7dd", 6)
    center_text(d, (0, 524, W, 550), "创建一个内容对象运行文件夹", font(16), "#656565")
    center_text(d, (0, 558, W, 583), "想法门：四条路线", font(18, True), "#565656")
    route = [("原创", "来自你"), ("再加工", "延展自有内容"), ("改写", "外部视角"), ("研究+构思", "暂不出稿")]
    xs = [54, 267, 480, 694]
    colors = ["#225b49", "#403c88", "#78371f", "#4b4b47"]
    for x, (t, b), c in zip(xs, route, colors):
        box(d, (x, 582, x + 198, 640), c, "#777777", 8, 1)
        center_text(d, (x, 589, x + 198, 635), f"{t}\n{b}", font(17, True), "#e8e8e8", 5)
    arrow(d, (467, 640), (467, 679), "#9a9a9a", 3)
    box(d, (94, 678, 840, 988), "#6b420e", "#b5803d", 12, 2)
    left_text(d, (129, 700), "运行文件夹 · 每个内容对象一个\nruns/active/2026-05-bookmark-flywheel/", font(18, True), "#f3cf8e")
    steps = ["已捕获", "想法审核", "简介就绪", "起草中", "验证", "作者审核", "已批准", "已调度", "已发布", "反馈24h", "反馈72h", "已学习"]
    for i, s in enumerate(steps):
        x = 122 + (i % 4) * 187
        y = 756 + (i // 4) * 69
        box(d, (x, y, x + 160, y + 48), "#724712", "#b5803d", 6, 1)
        center_text(d, (x, y, x + 160, y + 48), s, font(16, True), "#f0c56e")
        if i % 4 != 3:
            arrow(d, (x + 160, y + 24), (x + 182, y + 24), "#b5803d", 2)
    center_text(d, (94, 952, 840, 978), "content-object.md 追踪状态 · idea.md · brief.md · draft-package.md · feedback.md", font(15), "#b79868")
    arrow(d, (467, 988), (467, 1020), "#9a9a9a", 3)
    box(d, (94, 1019, 840, 1121), "#403c88", "#817bd3", 12, 2)
    center_text(d, (94, 1038, 840, 1106), "存储\n赢家 · 输家 · 声音规则 · 禁用模式 · 钩子 · 证明\n下一次起草前，运行文件夹先读取这份共享记忆", font(17, True), "#d9d6ff", 6)
    d.line((54, 1148, 880, 1148), fill="#303030", width=2)
    center_text(d, (0, 1158, W, 1184), "运行文件夹周围还有什么", font(16, True), "#555555")
    parts = [("策略", "定位 · 支柱\n受众 · 来源清单\n仅手动编辑"), ("声音", "声音档案\n避免烂内容\n起草前必读"), ("存储", "收件箱 · 工作板\n想法 · 钩子 · 证明\n反馈日志"), ("模块 + 工作流", "作者技能 · 代码\n验证清单\n调度交接")]
    for i, (t, b) in enumerate(parts):
        x = 54 + i * 213
        c = ["#403c88", "#78371f", "#6b420e", "#225b49"][i]
        box(d, (x, 1185, x + 198, 1291), c, "#777777", 8, 1)
        center_text(d, (x, 1196, x + 198, 1284), f"{t}\n{b}", font(16, True), "#eee", 6)
    center_text(d, (0, 1330, W, 1362), "每个对象读取共享部分 · 通过门控推进 · 发布后把学习写回系统", font(16), "#555555")
    save(im, "img-06.jpg")


def img07():
    W, H = 1384, 1332
    im = Image.new("RGB", (W, H), "#22211f")
    d = ImageDraw.Draw(im)
    center_text(d, (0, 36, W, 72), "四条内容路线", font(30, True), "#f5f5f5")
    center_text(d, (0, 82, W, 118), "起草前，想法门先判断这到底是哪一种内容", font(26), "#d9d9d9")
    box(d, (369, 137, 1011, 249), "#6b420e", "#c08a42", 14, 2)
    center_text(d, (369, 154, 1011, 236), "想法门\n只做一个决定：这是什么类型的内容？", font(28, True), "#f3c979", 8)
    xs = [69, 381, 693, 1005]
    colors = ["#225b49", "#403c88", "#78371f", "#4b4b47"]
    heads = ["1. 原创", "2. 再加工", "3. 改写", "4. 研究+构思"]
    for x, c, h in zip(xs, colors, heads):
        arrow(d, (690, 249), (x + 153, 319), "#505050", 2)
        box(d, (x, 319, x + 306, 393), c, "#999999", 9, 1)
        center_text(d, (x, 319, x + 306, 393), h, font(27, True), "#eeeeee")
    rows = [
        [("来自你", "第二大脑 · 笔记\n日记 · 语音备忘录\n盘了很久的想法"),
         ("自有内容", "已有文章\n跑出来的帖子\n有延展性的系列"),
         ("外部信号", "值得回应的推文\n值得拆解的文章\n带框架的转录稿"),
         ("话题探索", "研究规律\n生成角度\n暂时没有固定来源")],
        [("依赖基础层", "定位 · 证明库\n支柱 · 无外部来源\n高品味投入"),
         ("骨架是你的", "改变形式\n文章拆成串\n爆款自引回复"),
         ("通过你的视角", "保留什么 · 标注什么\n适用哪些声音规则\n检查避免烂内容"),
         ("输出不是帖子", "一个打磨过的想法\n或一组角度\n回写到想法库")],
    ]
    for r, row in enumerate(rows):
        y = 420 + r * 202
        for x, c, (t, b) in zip(xs, colors, row):
            box(d, (x, y, x + 306, y + 160), c, "#777777", 8, 1)
            center_text(d, (x, y + 18, x + 306, y + 58), t, font(27, True), "#eeeeee")
            center_text(d, (x + 12, y + 62, x + 294, y + 153), b, font(24), "#d6d6d6", 7)
    for x in xs[:3]:
        arrow(d, (x + 153, 782), (x + 153, 845), "#9a9a9a", 3)
    d.rounded_rectangle((1157, 187, 1322, 833), radius=6, outline="#555555", width=2)
    box(d, (69, 848, 1000, 961), "#6b420e", "#c08a42", 14, 2)
    center_text(d, (69, 868, 1000, 945), "开始起草\n前三条路线进入起草 · 每条都带自己的简介、参考资料和检查门", font(27, True), "#f3c979", 8)
    d.line((69, 998, 1311, 998), fill="#333333", width=2)
    center_text(d, (0, 1012, W, 1044), "为什么要有这道门", font(24, True), "#555555")
    box(d, (69, 1049, 650, 1200), "#444642", "#888888", 12, 1)
    center_text(d, (69, 1070, 650, 1184), "没有想法门\n草稿会混淆来源\n声音会漂 · 署名会乱", font(26, True), "#dedede", 8)
    box(d, (729, 1049, 1310, 1200), "#6b420e", "#c08a42", 12, 2)
    center_text(d, (729, 1070, 1310, 1184), "有想法门\n每条路线都有自己的检查\n交付的草稿更干净", font(26, True), "#f3c979", 8)
    center_text(d, (0, 1275, W, 1310), "前面只做一个决定 · 后面少改三遍", font(24), "#555555")
    save(im, "img-07.jpg")


def img08():
    W, H = 2048, 1354
    im = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(im)
    dark = "#202532"
    orange = "#f06f1d"
    blue = "#2b86f6"
    purple = "#8c55f0"
    grey = "#b8b8b8"
    d.ellipse((785, 22, 1055, 118), outline=orange, width=4)
    center_text(d, (785, 22, 1055, 118), "主题", font(32, True), dark)
    arrow(d, (920, 118), (920, 198), "#5b6372", 5)
    box(d, (720, 200, 1120, 315), "#ffffff", orange, 12, 4)
    center_text(d, (720, 214, 1120, 302), "编排者\n路由到合适代理", font(27, True), dark, 6)
    agents = [
        ("研究者", ["搜索X上的推文", "拉取书签和时间线", "分析头部账号", "研究写作风格", "", "把结果存进", "研究数据库", "", "输出：研究库"]),
        ("想法生成器", ["把研究变成想法", "从13种钩子公式中挑选", "补充关键点和角度", "链接回来源推文", "", "套用文案框架", "PAS、AIDA、BAB", "", "输出：结构化想法"]),
        ("作者", ["匹配我的声音和语气", "选择最佳钩子公式", "套用帖子格式模板", "运行质量清单", "", "把完成稿推送到", "调度工具", "", "输出：可发布稿"]),
    ]
    ax = [16, 568, 1099]
    for i, (title, lines) in enumerate(agents):
        x = ax[i]
        d.text((x, 382), title, font=font(24), fill="#7a7a7a")
        d.rounded_rectangle((x, 412, x + 465, 914), radius=8, outline=grey, width=3)
        d.rounded_rectangle((x + 25, 442, x + 445, 522), radius=12, outline=blue, fill="#dcebff", width=4)
        center_text(d, (x + 25, 442, x + 445, 522), title, font(34, True), dark)
        yy = 550
        for line in lines:
            if line:
                d.text((x + 50, yy), line, font=font(23), fill=dark)
            yy += 31
        arrow(d, (920, 315), (x + 235, 413), "#5b6372", 4)
    arrow(d, (483, 668), (568, 668), blue, 4)
    d.text((480, 640), "研究", font=font(18), fill=blue)
    arrow(d, (1033, 668), (1099, 668), blue, 4)
    d.text((1044, 640), "想法", font=font(18), fill=blue)
    d.rounded_rectangle((1720, 620, 2035, 773), radius=20, outline=orange, width=4)
    center_text(d, (1720, 635, 2035, 758), "已发布\n草稿已准备好\n等待审核", font(25, True), dark, 9)
    arrow(d, (1565, 668), (1720, 668), orange, 5)
    d.text((1593, 640), "草稿", font=font(18), fill=orange)
    circles = [
        (275, 1090, "研究数据库\n推文 +\n分析"),
        (810, 1100, "代理记忆\n跨会话\n持续保留"),
        (1340, 1070, "声音档案\n语气 +\n内容支柱"),
    ]
    for cx, cy, label in circles:
        d.ellipse((cx - 170, cy - 100, cx + 170, cy + 100), outline=purple, width=4)
        center_text(d, (cx - 150, cy - 82, cx + 150, cy + 82), label, font(25, True), dark, 8)
        arrow(d, (cx, cy - 100), (cx, 914), purple, 4)
    d.text((96, 1238), "想法生命周期：", font=font(23), fill=dark)
    states = ["草稿", "就绪", "已批准", "已写完"]
    for i, s in enumerate(states):
        x = 106 + i * 250
        col = orange if i == 3 else blue
        d.rounded_rectangle((x, 1272, x + 200, 1342), radius=10, outline=col, width=4)
        center_text(d, (x, 1272, x + 200, 1342), s, font(25, True), dark)
        if i < 3:
            arrow(d, (x + 200, 1307), (x + 250, 1307), "#5b6372", 4)
    d.text((1270, 120), "@shannholmberg", font=font(22), fill="#666666")
    save(im, "img-08.jpg")


def img09():
    W, H = 1036, 1498
    im = Image.new("RGB", (W, H), "#22211f")
    d = ImageDraw.Draw(im)
    center_text(d, (0, 28, W, 60), "V1 起步方案 · 6步 · 1-2小时", font(22, True), "#f5f5f5")
    center_text(d, (0, 66, W, 92), "你不会一次做完 · 但你会真正启动 · 这才是唯一有价值的状态", font(17), "#d6d6d6")
    steps = [
        ("1", "搭结构", "搭好文件夹结构", "六个顶层目录：strategy · voice · stores · runs · modules · workflows\nruns/ 里面放 active/ 和 archive/\n其余先空着，后面边跑边填"),
        ("2", "策略", "写策略 · 3个文件 · 每个3-5行", "positioning.md · audience.md · pillars.md\npillars = 3-4个你有资格持续讲的话题\naudience = 一个具体的人，不是一个人群标签"),
        ("3", "声音", "写声音锚点", "voice-profile.md → 5条你遵守的规则 · 5种你避免的模式 · 2-3篇参考帖\navoid-slop.md → 先列8个已知烂模式，每次翻车就补一条\nstores/proof/ → 10个具体证明：数字、名字、已交付项目\n每个代理起草前都先读 voice + avoid-slop"),
        ("4", "想法", "把10个想法丢进 stores/inbox.md", "一半应该来自你这个月已经说过的话\n私信、电话、对话里都算\n不要现场编，去偷你自己真实的想法"),
        ("5", "运行文件夹", "为一个想法打开一个运行文件夹", "runs/active/2026-05-{your-slug}/\ncontent-object.md → id · status · format · pillar\nbrief.md → 作者上下文包\n把简介交给写作模型；系统从这一刻真正开始跑"),
        ("6", "闭环", "读草稿 · 闭环", "模型把 draft-package.md 返回到同一个运行文件夹\n对照验证器 + 避免烂内容文档检查\n通过 + 入队；或带着一条具体意见退回\n发布后 → 写 feedback.md → 归档文件夹"),
    ]
    colors = ["#225b49", "#225b49", "#403c88", "#78371f", "#6b420e", "#6b420e"]
    y = 98
    for i, (num, side, title, body) in enumerate(steps):
        c = colors[i]
        box(d, (75, y, 160, y + 128), c, "#659f8b", 9, 1)
        center_text(d, (75, y + 24, 160, y + 103), f"{num}\n{side}", font(17, True), "#dfeee8", 8)
        box(d, (173, y, 938, y + 128), c, "#659f8b" if i < 3 else "#b5803d", 9, 1)
        left_text(d, (201, y + 22), title, font(20, True), "#f1f1f1")
        left_text(d, (201, y + 55), body, font(15), "#d1d1d1", 700, 5)
        if i < len(steps) - 1:
            arrow(d, (118, y + 128), (118, y + 158), "#8a8a8a", 2)
        y += 158
    d.line((75, 1176, 938, 1176), fill="#333333", width=2)
    center_text(d, (0, 1188, W, 1218), "1-2小时后，你会得到什么", font(18, True), "#555555")
    box(d, (75, 1223, 938, 1403), "#444642", "#888888", 9, 1)
    tree = "my-content-system/\n├── strategy/ — positioning · audience · pillars\n├── voice/ — voice-profile · avoid-slop\n├── stores/ — inbox · proof · feedback\n├── runs/active/2026-05-your-slug/ — content-object · brief · draft-package · feedback\n├── modules/ — writer skill · references · templates\n└── workflows/ — idea-to-published · verifier · scheduler · feedback loop"
    left_text(d, (113, 1251), tree, font(16, mono=True), "#d7d7d7", 800, 5)
    center_text(d, (0, 1450, W, 1478), "前期1-2小时 · 之后每周省下数小时 · 下一稿从上下文里开始，而不是从零开始", font(16), "#555555")
    save(im, "img-09.jpg")


def img10():
    W, H = 1526, 382
    im = Image.new("RGB", (W, H), "#202020")
    d = ImageDraw.Draw(im)
    white = "#eeeeee"
    def panel(x, y, w, h, title, lines):
        d.rectangle((x, y, x + w, y + h), outline=white, width=2)
        d.text((x + 22, y + 18), title, font=font(25, True, mono=True), fill=white)
        d.line((x + 22, y + 58, x + w - 22, y + 58), fill=white, width=2)
        yy = y + 105
        for line in lines:
            d.text((x + 24, yy), f"→ {line}", font=font(24, True, mono=True), fill=white)
            yy += 34
    panel(22, 53, 687, 282, "作者（OPUS 4.7）", ["品味", "节奏", "压缩", "声音", "真正的草稿"])
    panel(792, 53, 687, 282, "编排者（GPT-5.5）", ["在层与层之间路由", "为作者打包正确上下文", "决定交付哪些信息", "运行验证器", "交接到发布层"])
    save(im, "img-10.jpg")


def img11():
    W, H = 1200, 1096
    im = Image.new("RGB", (W, H), "#111111")
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 38), fill="#2c2c2c")
    d.text((18, 9), "npm install", font=font(14), fill="#d8d8d8")
    d.text((278, 9), "claude-opus-4.7 · C:\\Users", font=font(14), fill="#d8d8d8")
    d.text((544, 9), "Windows PowerShell", font=font(14, True), fill="#ffffff")
    d.text((13, 66), "HERMES-AGENT", font=font(72, True, mono=True), fill="#ffd21e")
    box(d, (18, 178, 1176, 856), "#0f0f0f", "#b56a3a", 4, 2)
    d.text((160, 206), "Hermes Agent v0.13.0（2026.5.7） · upstream 80775d75 · local e0c03def（+19个提交）", font=font(15, True, mono=True), fill="#f0c75c")
    mascot = ["      .:::::.", "   .:::::::::::.", "  :::::::::::::::", "  :::  HERMES :::", "   ':::::::::::'", "      ':::::'"]
    yy = 265
    for line in mascot:
        d.text((70, yy), line, font=font(22, True, mono=True), fill="#e2a136")
        yy += 30
    d.text((44, 560), "claude-opus-4.7", font=font(16, True, mono=True), fill="#e2a136")
    x = 362
    d.text((x, 225), "可用工具", font=font(17, True, mono=True), fill="#e2a136")
    tools = [
        "browser: browser_back, browser_click, ...",
        "browser-cdp: browser_cdp, browser_dialog",
        "clarify: clarify",
        "code_execution: execute_code",
        "cronjob: cronjob",
        "delegation: delegate_task",
        "discord: discord",
        "discord_admin: discord_admin",
        "（另有18个工具集...）",
    ]
    yy = 252
    for t in tools:
        d.text((x, yy), t, font=font(16, mono=True), fill="#d4a061")
        yy += 22
    d.text((x, 430), "可用技能", font=font(17, True, mono=True), fill="#e2a136")
    skills = [
        "autonomous-ai-agents: claude-code, codex, hermes-agent, opencode",
        "creative: architecture-diagram, ascii-art, ascii-video, ...",
        "data-science: jupyter-live-kernel",
        "devops: kanban-orchestrator, kanban-worker, webhook-sub...",
        "email: himalaya",
        "gaming: minecraft-modpack-server, pokemon-player",
        "general: dogfood, yuanbao",
        "github: codebase-inspection, github-auth, github-code-r...",
        "mcp: native-mcp",
        "media: gif-search, heartmula, songsee, spotify, youtub...",
        "note-taking: obsidian",
        "productivity: airtable, google-workspace, linear, maps...",
        "research: arxiv, blogwatcher, llm-wiki, polymarket",
        "smart-home: openhue",
        "software-development: debugging-hermes-tui-commands, ...",
    ]
    yy = 462
    for s in skills:
        d.text((x, yy), s, font=font(15, mono=True), fill="#e4d7bf" if yy % 44 else "#a96b48")
        yy += 22
    d.text((362, 810), "18个工具 · 84个技能 · /help 查看命令", font=font(16, mono=True), fill="#a96b48")
    d.text((362, 834), "[!] 落后16个提交 — 运行 hermes update 更新", font=font(16, True, mono=True), fill="#f3d079")
    d.text((12, 896), "欢迎使用 Hermes Agent！输入消息，或用 /help 查看命令", font=font(17, True, mono=True), fill="#f0f0f0")
    d.text((34, 922), "提示：agent.api_max_retries（默认3）控制失败API调用在报错前重试多少次。", font=font(15, mono=True), fill="#7f5a35")
    d.text((34, 966), "[!] tirith 安全扫描器已启用但不可用 —— 将仅使用模式匹配扫描命令", font=font(16, True, mono=True), fill="#d8a43c")
    d.rectangle((14, 986, 420, 1015), fill="#233042")
    d.text((25, 990), "$ claude-opus-4.7 | ctx -- [      ] -- | 1s | 0s", font=font(15, True, mono=True), fill="#f8f8f8")
    d.line((0, 1048, W, 1048), fill="#b56a3a", width=2)
    d.text((13, 1062), "› █", font=font(22, mono=True), fill="#f8f8f8")
    save(im, "img-11.jpg")


def img12():
    W, H = 2048, 1768
    im = Image.new("RGB", (W, H), "#0d0d0e")
    d = ImageDraw.Draw(im)
    d.text((147, 22), "postiz", font=font(28, True), fill="#ffffff")
    nav = [
        (428, "AI代理CLI（OpenClaw）"),
        (745, "开发文档"),
        (905, "渠道⌄"),
        (1092, "新闻"),
        (1212, "博客"),
        (1322, "价格"),
    ]
    for x, n in nav:
        d.text((x, 31), n, font=font(20, True), fill="#ffffff")
    box(d, (1547, 7, 1672, 72), "#0d0d0e", "#ffffff", 28, 2)
    center_text(d, (1547, 7, 1672, 72), "登录", font(21, True), "#ffffff")
    box(d, (1684, 7, 1892, 72), "#ffffff", "#ffffff", 28, 2)
    center_text(d, (1684, 7, 1892, 72), "免费开始  »", font(21, True), "#111111")
    awards = ["当日产品\n第1名", "本周产品\n第1名", "本月产品\n第1名"]
    for i, a in enumerate(awards):
        center_text(d, (720 + i * 190, 168, 875 + i * 190, 244), a, font(15, True), "#ffffff", 2)
    center_text(d, (0, 270, W, 455), "用 AI 代理\n自动运营你的社媒", font(76, True), "#ffffff", 10)
    d.line((1160, 462, 1442, 445), fill="#ee57ff", width=5)
    d.line((1195, 480, 1505, 468), fill="#ee57ff", width=5)
    center_text(d, (0, 518, W, 626), "自动规划、生成并调度到30多个社媒平台\n然后在可视化日历里统一审核和编辑。\n接入你的 OpenClaw / Claude", font(31), "#e6e6e6", 9)
    platforms = ["IG", "YT", "G", "Dr", "in", "rd", "TT", "f", "P", "Th", "X", "Sl", "DC", "M", "BS", "GH", "W", "TG", "VK", "DEV", "M", "WP"]
    for i, p in enumerate(platforms):
        px = 700 + (i % 11) * 53
        py = 666 + (i // 11) * 55
        d.rounded_rectangle((px, py, px + 42, py + 42), radius=8, fill=["#e84f60", "#f04432", "#3c82f6", "#f06bb5", "#2b75bd", "#ff5b30", "#111", "#3d75f6", "#d9273e", "#000", "#111"][i % 11])
        center_text(d, (px, py, px + 42, py + 42), p, font(17, True), "#ffffff")
    box(d, (814, 803, 1216, 879), "#ffffff", "#ffffff", 35, 2)
    center_text(d, (814, 803, 1216, 879), "免费试用7天  »", font(27, True), "#111111")
    center_text(d, (0, 984, W, 1016), "我需要代理式调度     ●     我需要普通调度", font(18), "#ffffff")
    d.rounded_rectangle((138, 1051, 1890, 1800), radius=30, fill="#7743f5")
    d.rectangle((138, 1180, 1890, 1768), fill="#7842f5")
    center_text(d, (0, 1112, W, 1165), "编辑并打磨你的帖子", font(42, True), "#ffffff")
    d.rounded_rectangle((270, 1210, 1770, 1775), radius=25, fill="#171717", outline="#8d77d7", width=8)
    d.rounded_rectangle((390, 1320, 1110, 1700), radius=14, fill="#0f0f10")
    d.rounded_rectangle((1130, 1320, 1660, 1700), radius=14, fill="#0f0f10")
    d.text((420, 1342), "创建帖子", font=font(22, True), fill="#ffffff")
    d.text((1158, 1342), "帖子预览", font=font(22, True), fill="#ffffff")
    d.text((420, 1545), "每天做一点，比偶尔冲刺更有效 ——\n关键是持续。每天几分钟，长期也能滚出结果。", font=font(19), fill="#ffffff")
    d.text((1208, 1404), "Daniel Hamilton", font=font(18, True), fill="#ffffff")
    d.text((1148, 1450), "每天做一点，比偶尔冲刺更有效 ——\n关键是持续。每天几分钟，长期也能滚出结果。", font=font(17), fill="#ffffff")
    d.rounded_rectangle((1148, 1534, 1490, 1692), radius=10, fill="#efc8c8")
    center_text(d, (1148, 1534, 1490, 1692), "配图预览", font(25, True), "#6b4b4b")
    save(im, "img-12.jpg")


if __name__ == "__main__":
    for fn in [img03, img04, img05, img06, img07, img08, img09, img10, img11, img12]:
        fn()
