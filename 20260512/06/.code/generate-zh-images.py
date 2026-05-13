from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
import random


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images"
FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"

BG = (17, 17, 17)
WHITE = (218, 224, 236)
MUTED = (154, 160, 170)
ORANGE = (214, 114, 0)
ORANGE_TXT = (255, 136, 82)
BLUE = (84, 169, 245)
GREEN = (69, 172, 91)
TEAL = (111, 178, 168)
PINK = (255, 133, 139)
PURPLE = (176, 139, 255)
DARK_BLUE = (18, 33, 40)
DARK_GREEN = (8, 41, 31)
DARK_ORANGE = (32, 20, 7)
DARK_PURPLE = (45, 34, 66)
DARK_RED = (63, 35, 36)
DARK_GRAY = (29, 32, 34)
LIGHT_BAR = (221, 226, 238)

random.seed(7)


def font(size, index=0):
    return ImageFont.truetype(FONT, size=size, index=index)


def canvas(w, h):
    return Image.new("RGB", (w, h), BG)


def measure(draw, text, f):
    if not text:
        return 0, 0
    b = draw.multiline_textbbox((0, 0), text, font=f, spacing=8, align="center")
    return b[2] - b[0], b[3] - b[1]


def fit_font(draw, text, max_w, max_h, start, min_size=22):
    size = start
    while size >= min_size:
        f = font(size)
        w, h = measure(draw, text, f)
        if w <= max_w and h <= max_h:
            return f
        size -= 2
    return font(min_size)


def wrap_text(draw, text, f, max_w):
    lines = []
    current = ""
    for ch in text:
        if ch == "\n":
            lines.append(current)
            current = ""
            continue
        trial = current + ch
        if draw.textbbox((0, 0), trial, font=f)[2] <= max_w or not current:
            current = trial
        else:
            lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return "\n".join(lines)


def centered(draw, box, text, color=WHITE, size=40, max_lines=True, spacing=8):
    x1, y1, x2, y2 = box
    max_w = x2 - x1 - 28
    max_h = y2 - y1 - 20
    f = font(size)
    if max_lines:
        text = wrap_text(draw, text, f, max_w)
    f = fit_font(draw, text, max_w, max_h, size)
    if max_lines:
        text = wrap_text(draw, text, f, max_w)
    tw, th = measure(draw, text, f)
    draw.multiline_text(
        (x1 + (x2 - x1 - tw) / 2, y1 + (y2 - y1 - th) / 2 - 2),
        text,
        font=f,
        fill=color,
        spacing=spacing,
        align="center",
    )


def text(draw, xy, s, size, color=WHITE, anchor="la"):
    draw.text(xy, s, font=font(size), fill=color, anchor=anchor)


def rough_rect(draw, box, outline, fill=None, width=5, radius=34, passes=2):
    x1, y1, x2, y2 = box
    for _ in range(passes):
        j = [random.randint(-3, 3) for _ in range(4)]
        draw.rounded_rectangle(
            (x1 + j[0], y1 + j[1], x2 + j[2], y2 + j[3]),
            radius=radius,
            outline=outline,
            fill=fill if _ == 0 else None,
            width=width,
        )


def line(draw, points, color=WHITE, width=5):
    for _ in range(2):
        pts = [(x + random.randint(-2, 2), y + random.randint(-2, 2)) for x, y in points]
        draw.line(pts, fill=color, width=width)


def arrow(draw, start, end, color=WHITE, width=5):
    line(draw, [start, end], color, width)
    sx, sy = start
    ex, ey = end
    ang = math.atan2(ey - sy, ex - sx)
    length = 28
    a1 = ang + math.pi * 0.82
    a2 = ang - math.pi * 0.82
    p1 = (ex + length * math.cos(a1), ey + length * math.sin(a1))
    p2 = (ex + length * math.cos(a2), ey + length * math.sin(a2))
    line(draw, [p1, end, p2], color, width)


def save(img, name):
    img.save(OUT / name, quality=94, subsampling=1)


def img01():
    img = canvas(1594, 1040)
    d = ImageDraw.Draw(img)
    text(d, (30, 28), "智能体工作流配方", 48)
    text(d, (32, 92), "把混乱流程变成智能体可执行的系统", 28)
    boxes = {
        "trigger": (8, 270, 394, 438),
        "context": (532, 270, 918, 438),
        "rules": (1057, 270, 1446, 438),
        "draft": (8, 550, 394, 718),
        "approve": (532, 550, 918, 718),
        "learn": (1057, 550, 1446, 718),
    }
    labels = {
        "trigger": ("触发", "什么会启动它？"),
        "context": ("上下文", "它必须知道什么？"),
        "rules": ("规则", "什么是允许的？"),
        "draft": ("产出", "它应该生成什么？"),
        "approve": ("审批", "人类在哪里判断？"),
        "learn": ("学习", "下次如何改进？"),
    }
    for k, b in boxes.items():
        rough_rect(d, b, TEAL, DARK_GREEN, radius=34)
        centered(d, (b[0] + 16, b[1] + 16, b[2] - 16, b[1] + 72), labels[k][0], TEAL, 35)
        centered(d, (b[0] + 16, b[1] + 66, b[2] - 16, b[3] - 16), labels[k][1], TEAL, 30)
    arrow(d, (394, 354), (468, 354), TEAL)
    arrow(d, (918, 354), (995, 354), TEAL)
    arrow(d, (1249, 438), (1249, 535), TEAL)
    arrow(d, (394, 634), (468, 634), TEAL)
    arrow(d, (918, 634), (995, 634), TEAL)
    rough_rect(d, (194, 744, 1377, 836), WHITE, None, width=4, radius=16)
    centered(d, (210, 752, 1360, 830), "如果这些框填不出来，你还没有真正的人工智能工作流。", WHITE, 34)
    rough_rect(d, (30, 920, 1460, 1018), LIGHT_BAR, LIGHT_BAR, width=0, radius=16)
    centered(d, (50, 920, 1440, 1018), "智能体会暴露你到底有没有流程。", (6, 8, 11), 36)
    save(img, "img-01-zh.jpg")


def img02():
    img = canvas(1856, 1128)
    d = ImageDraw.Draw(img)
    text(d, (928, 140), "人工智能辅助与人工智能原生", 56, anchor="ma")
    left = (155, 294, 878, 916)
    right = (1020, 294, 1742, 916)
    rough_rect(d, left, ORANGE, DARK_ORANGE, radius=62)
    rough_rect(d, right, BLUE, DARK_BLUE, radius=62)
    text(d, (516, 345), "人工智能辅助型公司", 42, ORANGE_TXT, anchor="ma")
    text(d, (1382, 345), "人工智能原生公司", 42, BLUE, anchor="ma")
    for y, s in [(464, "聊天助手标签页"), (585, "混乱文档"), (707, "人类分发工作")]:
        b = (286, y, 750, y + 91)
        rough_rect(d, b, WHITE, None, width=4, radius=20)
        centered(d, b, s, WHITE, 34)
    for y, s in [(444, "干净数据层"), (559, "智能体工作流"), (674, "人类审批点"), (790, "反馈循环")]:
        b = (1150, y, 1614, y + 86)
        rough_rect(d, b, WHITE, None, width=4, radius=18)
        centered(d, b, s, WHITE, 32)
    text(d, (928, 1004), "使用人工智能，不等于让公司能被人工智能使用。", 34, MUTED, anchor="ma")
    save(img, "img-02-zh.jpg")


def img03():
    img = canvas(1586, 1192)
    d = ImageDraw.Draw(img)
    text(d, (793, 74), "新的组织结构图", 58, anchor="ma")
    top = (256, 232, 1265, 402)
    rough_rect(d, top, WHITE, None, radius=28)
    centered(d, top, "人类：战略、品味、判断、信任", WHITE, 38)
    arrow(d, (760, 402), (760, 486), WHITE)
    boxes = [
        ((65, 496, 480, 591), "支持智能体"),
        ((558, 496, 973, 591), "销售智能体"),
        ((1050, 496, 1465, 591), "研究智能体"),
        ((65, 646, 480, 741), "财务智能体"),
        ((558, 646, 973, 741), "运营智能体"),
        ((1050, 646, 1465, 741), "法务智能体"),
    ]
    for b, s in boxes:
        rough_rect(d, b, BLUE, DARK_BLUE, radius=18)
        centered(d, b, s, WHITE, 31)
    for x in [275, 760, 1245]:
        arrow(d, (x, 792), (x, 864), GREEN)
    base = (65, 865, 1465, 1032)
    rough_rect(d, base, GREEN, DARK_GREEN, radius=34)
    centered(d, (90, 888, 1440, 945), "共享上下文层", WHITE, 35)
    centered(d, (90, 940, 1440, 1012), "客户数据｜标准流程｜定价｜权限｜品牌语气｜决策日志", WHITE, 31)
    text(d, (793, 1100), "未来的组织结构，路由员更少，审核者更多。", 34, MUTED, anchor="ma")
    save(img, "img-03-zh.jpg")


def img04():
    img = canvas(1914, 1094)
    d = ImageDraw.Draw(img)
    text(d, (957, 128), "人工智能原生技术栈", 60, anchor="ma")
    layers = [
        ((807, 292, 1164, 376), "持续学习", GREEN, DARK_GREEN, 28),
        ((746, 402, 1266, 486), "人类审核", BLUE, DARK_BLUE, 31),
        ((645, 508, 1366, 594), "智能体工作流", ORANGE, DARK_ORANGE, 33),
        ((545, 618, 1468, 704), "权限 + 政策", PINK, DARK_RED, 33),
        ((444, 726, 1570, 811), "结构化知识", PURPLE, DARK_PURPLE, 33),
        ((344, 834, 1669, 920), "干净数据", WHITE, DARK_GRAY, 33),
    ]
    for b, s, c, fill, sz in layers:
        rough_rect(d, b, c, fill, radius=18)
        centered(d, b, s, WHITE, sz)
    text(d, (957, 1010), "买工具得不到智能体杠杆；让业务可读才得到。", 36, MUTED, anchor="ma")
    save(img, "img-04-zh.jpg")


def img05():
    img = canvas(1730, 1164)
    d = ImageDraw.Draw(img)
    text(d, (865, 104), "人工智能原生机会地图", 56, anchor="ma")
    frame = (216, 233, 1416, 892)
    rough_rect(d, frame, WHITE, None, radius=56)
    line(d, [(816, 234), (816, 892)], (70, 84, 80), 2)
    line(d, [(216, 564), (1416, 564)], (70, 84, 80), 2)
    text(d, (98, 560), "重复性", 34, anchor="mm")
    text(d, (816, 955), "工作流复杂度", 34, anchor="ma")
    centered(d, (345, 315, 636, 430), "太简单，容易商品化", MUTED, 34)
    centered(d, (345, 690, 636, 805), "痛感还不够", MUTED, 34)
    centered(d, (955, 286, 1245, 396), "人工智能原生金矿", GREEN, 46)
    centered(d, (910, 465, 1290, 699), "保险运营\n招聘\n合规\n支持\n医疗管理\n法务接收", GREEN, 30)
    centered(d, (950, 725, 1265, 825), "复杂，但不可重复", MUTED, 35)
    text(d, (865, 1028), "寻找那些足够重复、适合智能体，也足够复杂、让老牌企业很慢的工作。", 32, MUTED, anchor="ma")
    save(img, "img-05-zh.jpg")


def img06():
    img = canvas(1870, 1006)
    d = ImageDraw.Draw(img)
    text(d, (935, 142), "错误问题与正确问题", 58, anchor="ma")
    left = (130, 320, 814, 700)
    right = (1044, 320, 1825, 700)
    rough_rect(d, left, ORANGE, DARK_ORANGE, radius=54)
    rough_rect(d, right, BLUE, DARK_BLUE, radius=54)
    centered(d, left, "哪里可以加人工智能？", WHITE, 52)
    centered(d, right, "如果智能体先完成所有工作的初稿，这家公司会如何运作？", WHITE, 46)
    arrow(d, (830, 510), (1030, 510), WHITE, 5)
    text(d, (472, 796), "功能", 48, ORANGE_TXT, anchor="ma")
    text(d, (1450, 796), "一家新公司", 48, BLUE, anchor="ma")
    text(d, (935, 945), "第一个问题给你功能；第二个问题给你一家新公司。", 34, MUTED, anchor="ma")
    save(img, "img-06-zh.jpg")


def img07():
    img = canvas(2048, 1075)
    d = ImageDraw.Draw(img)
    text(d, (70, 54), "改造前后的工作流", 66)
    text(d, (70, 247), "改造前", 50, ORANGE_TXT)
    y = 348
    before = ["客户请求", "收件箱", "人工搜索", "群聊提问", "找文档", "审批", "回复"]
    x = 88
    for s in before:
        b = (x, y, x + 200, y + 118)
        rough_rect(d, b, ORANGE, DARK_ORANGE, radius=22)
        centered(d, b, s, WHITE, 23)
        if s != before[-1]:
            arrow(d, (x + 200, y + 59), (x + 236, y + 59), ORANGE, 4)
        x += 256
    text(d, (70, 665), "改造后", 50, BLUE)
    y = 758
    after = ["客户请求", "智能体上下文", "政策检查", "草稿和行动", "人工审批", "回复", "学习循环"]
    x = 72
    for s in after:
        b = (x, y, x + 220, y + 126)
        rough_rect(d, b, BLUE, DARK_BLUE, radius=24)
        centered(d, b, s, WHITE, 24)
        if s != after[-1]:
            arrow(d, (x + 220, y + 63), (x + 262, y + 63), BLUE, 4)
        x += 260
    text(d, (1024, 1008), "魔法不在智能体，而在于移除迷宫。", 38, MUTED, anchor="ma")
    save(img, "img-07-zh.jpg")


for fn in [img01, img02, img03, img04, img05, img06, img07]:
    fn()
