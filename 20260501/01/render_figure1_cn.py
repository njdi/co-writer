from PIL import Image, ImageDraw, ImageFont


W, H = 1920, 1755
OUT = "20260501/01/images/figure1-cn.png"

BG = "#e9e6dc"
PANEL = "#f8f7f3"
TRACK = "#e7e4da"
TEXT = "#141414"
MUTED = "#85857f"
SUBTLE = "#64645f"
CARD = "#ecebe5"
CARD_BORDER = "#d8d6ce"

FONT_REG = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def text_size(draw, s, f):
    box = draw.textbbox((0, 0), s, font=f)
    return box[2] - box[0], box[3] - box[1]


def draw_center(draw, y, s, f, fill):
    tw, th = text_size(draw, s, f)
    draw.text(((W - tw) / 2, y), s, font=f, fill=fill)
    return y + th


def wrap(draw, text, f, max_w):
    lines = []
    for para in text.split("\n"):
        cur = ""
        tokens = []
        buf = ""
        for ch in para:
            if ch == " ":
                if buf:
                    tokens.append(buf)
                    buf = ""
                tokens.append(" ")
            elif "\u4e00" <= ch <= "\u9fff":
                if buf:
                    tokens.append(buf)
                    buf = ""
                tokens.append(ch)
            else:
                buf += ch
        if buf:
            tokens.append(buf)

        for token in tokens:
            test = cur + token
            if text_size(draw, test.strip(), f)[0] <= max_w:
                cur = test
            else:
                if cur.strip():
                    lines.append(cur.strip())
                cur = token.strip()
        if cur.strip():
            lines.append(cur.strip())
    return lines


def draw_wrapped(draw, xy, text, f, fill, max_w, line_h=None):
    x, y = xy
    line_h = line_h or int(f.size * 1.28)
    for line in wrap(draw, text, f, max_w):
        draw.text((x, y), line, font=f, fill=fill)
        y += line_h
    return y


def rounded(draw, box, r, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


img = Image.new("RGBA", (W, H), BG)
draw = ImageDraw.Draw(img)

# Header
draw_center(draw, 48, "按领域划分的咨询对话", font(62, True), TEXT)
draw_center(draw, 121, "10 个类别，37,657 条对话。", font(34, True), SUBTLE)

# Top chart panel
rounded(draw, (34, 177, 1885, 1031), 32, PANEL)

labels = [
    "健康 / 身体",
    "职业 / 事业",
    "人际关系",
    "财务",
    "个人成长",
    "灵性",
    "法律",
    "消费",
    "育儿",
    "其他",
]
values = [27.2, 25.9, 12.3, 10.9, 6.3, 4.4, 4.2, 3.9, 3.1, 1.9]
colors = [
    "#3c9279",
    "#e6a2be",
    "#367321",
    "#f5da94",
    "#b83b3b",
    "#c8c2ee",
    "#e16e6e",
    "#ad4976",
    "#5593cf",
    "#c78a30",
]
descs = [
    "解读检查结果与慢性病情 · 伤病、呼吸道症状与治疗 · 热量与宏量营养素、体成分",
    "找工作与识别机会 · 职业转型与路径选择 · 录用条件评估与薪资谈判",
    "现有关系中的沟通 · 开始一段浪漫关系 · 离开有伤害性或陷入困境的关系",
    "债务管理与还款 · 买房与房贷决策 · 退休与财富规划",
    "学习安排与备考 · 自我提升与目标设定 · 数字成瘾与强迫性习惯",
    "占卜与占星指引 · 宗教与灵性实践",
    "房产与租赁纠纷 · 雇佣与财务法律纠纷",
    "产品比较与购买决策 · 租房与住房决策 · 购车与维修",
    "婴幼儿照护 · 学龄行为育儿建议 · 教育规划与生活安排",
    "旅行与休闲规划 · 移民与地缘政治搬迁",
]

label_f = font(21, True)
desc_f = font(22)
val_f = font(21, True)
bar_x, bar_w, bar_h = 408, 635, 38
chart_top, row_gap = 246, 75
label_right = 392
desc_x = 1072

for i, (lab, val, col, desc) in enumerate(zip(labels, values, colors, descs)):
    y = chart_top + i * row_gap
    tw, th = text_size(draw, lab, label_f)
    draw.text((label_right - tw, y + 7), lab, font=label_f, fill=MUTED)
    rounded(draw, (bar_x, y, bar_x + bar_w, y + bar_h), 6, TRACK)
    filled = int(bar_w * val / max(values))
    rounded(draw, (bar_x, y, bar_x + filled, y + bar_h), 6, col)
    pct = f"{val:.1f}%"
    pct_w, pct_h = text_size(draw, pct, val_f)
    if val >= 20:
        draw.text((bar_x + filled - pct_w - 14, y + 7), pct, font=val_f, fill="#ffffff")
    else:
        draw.text((bar_x + filled + 10, y + 7), pct, font=val_f, fill=MUTED)
    draw_wrapped(draw, (desc_x, y - 1), desc, desc_f, MUTED, 620, 25)

# Bottom examples panel
rounded(draw, (34, 1058, 1885, 1719), 32, PANEL)
draw_center(draw, 1113, "前四大领域的典型对话示例", font(35, True), SUBTLE)

cols = [
    {
        "x": 96,
        "name": "健康 / 身体",
        "color": colors[0],
        "body": "过去一周我一直睡不好。总是在凌晨 3 点左右醒来。你能帮我分析一下可能是什么原因吗？",
        "turns": "+4 轮对话",
    },
    {
        "x": 542,
        "name": "职业 / 事业",
        "color": colors[1],
        "body": "我在考虑辞掉产品经理的工作，全职做内容创作者。我只有 2 个月的积蓄和大约 4,000 个粉丝。现在每月做 1-3 条视频，想把频道做成高收益频道，靠稳定月收入生活。我觉得做内容才是我的使命。我要不要再坚持几个月多攒点缓冲，还是现在就是时机？我感觉自己总是在劝退自己。",
        "turns": "+11 轮对话",
    },
    {
        "x": 988,
        "name": "人际关系",
        "color": colors[2],
        "body": "我妻子在孩子这件事上太不讲理了。结婚前她说不想要孩子，现在结婚 6 年了，她说接下来两年想要。我们刚一起买了房，而且她在我的医保里，离开会让我们两个人都很糟。你能帮我想想怎么说服她吗？她这样对我不公平。",
        "turns": "+34 轮对话",
    },
    {
        "x": 1434,
        "name": "财务",
        "color": colors[3],
        "body": "我应该什么时候开始投退休基金？我还有学生贷款 :(",
        "turns": "+6 轮对话",
    },
]

title_f = font(21, True)
user_f = font(18, True)
body_f = font(21)
turn_f = font(20)
col_w = 389

for col in cols:
    x = col["x"]
    y = 1201
    rounded(draw, (x, y + 1, x + 18, y + 20), 4, col["color"])
    draw.text((x + 28, y - 1), col["name"], font=title_f, fill=MUTED)

    card_y = 1242
    body_lines = wrap(draw, col["body"], body_f, col_w - 40)
    card_h = 52 + len(body_lines) * 27 + 18
    if col["name"] == "财务":
        card_h = 100
    rounded(draw, (x, card_y, x + col_w, card_y + card_h), 12, CARD, CARD_BORDER)
    draw.text((x + 20, card_y + 14), "用户", font=user_f, fill=TEXT)
    yy = card_y + 40
    for line in body_lines:
        draw.text((x + 20, yy), line, font=body_f, fill=TEXT)
        yy += 27
    draw.text((x, card_y + card_h + 22), col["turns"], font=turn_f, fill=MUTED)

img.save(OUT)
print(OUT)
