from PIL import Image, ImageDraw, ImageFont


SCALE = 3
W, H = 917, 585


def sc(v):
    if isinstance(v, tuple):
        return tuple(int(x * SCALE) for x in v)
    return int(v * SCALE)


def font(path, size, index=0):
    return ImageFont.truetype(path, sc(size), index=index)


FONT_HEITI_MEDIUM = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_HEITI_LIGHT = "/System/Library/Fonts/STHeiti Light.ttc"
FONT_MENLO = "/System/Library/Fonts/Menlo.ttc"

title_font = font(FONT_HEITI_MEDIUM, 18)
title_small_font = font(FONT_HEITI_MEDIUM, 17)
body_font = font(FONT_HEITI_LIGHT, 12)
body_small_font = font(FONT_HEITI_LIGHT, 11)
note_font = font(FONT_HEITI_LIGHT, 11)
label_font = font(FONT_MENLO, 7)
caps_font = font(FONT_MENLO, 8)
label_cn_font = font(FONT_HEITI_LIGHT, 8)
caps_cn_font = font(FONT_HEITI_LIGHT, 9)


def centered_text(draw, xy, text, fnt, fill, anchor="mm"):
    draw.text(sc(xy), text, font=fnt, fill=fill, anchor=anchor)


def dashed_line(draw, start, end, fill, width=1, dash=5, gap=4):
    x1, y1 = start
    x2, y2 = end
    dx, dy = x2 - x1, y2 - y1
    dist = (dx * dx + dy * dy) ** 0.5
    if dist == 0:
        return
    ux, uy = dx / dist, dy / dist
    pos = 0
    while pos < dist:
        seg = min(dash, dist - pos)
        sx, sy = x1 + ux * pos, y1 + uy * pos
        ex, ey = x1 + ux * (pos + seg), y1 + uy * (pos + seg)
        draw.line([sc((sx, sy)), sc((ex, ey))], fill=fill, width=sc(width))
        pos += dash + gap


def arrow(draw, start, end, fill="#1f1f1f", width=1.4, head=10):
    draw.line([sc(start), sc(end)], fill=fill, width=sc(width))
    x1, y1 = start
    x2, y2 = end
    if abs(x2 - x1) >= abs(y2 - y1):
        direction = 1 if x2 >= x1 else -1
        pts = [(x2, y2), (x2 - direction * head, y2 - head / 2), (x2 - direction * head, y2 + head / 2)]
    else:
        direction = 1 if y2 >= y1 else -1
        pts = [(x2, y2), (x2 - head / 2, y2 - direction * head), (x2 + head / 2, y2 - direction * head)]
    draw.polygon([sc(p) for p in pts], fill=fill)


def dashed_rounded_rect(draw, box, radius, outline, fill, width=1.4, dash=5, gap=5):
    draw.rounded_rectangle(sc(box), radius=sc(radius), fill=fill)
    x1, y1, x2, y2 = box
    # Dashes are close enough to the original when drawn on the straight spans.
    dashed_line(draw, (x1 + radius, y1), (x2 - radius, y1), outline, width, dash, gap)
    dashed_line(draw, (x2, y1 + radius), (x2, y2 - radius), outline, width, dash, gap)
    dashed_line(draw, (x2 - radius, y2), (x1 + radius, y2), outline, width, dash, gap)
    dashed_line(draw, (x1, y2 - radius), (x1, y1 + radius), outline, width, dash, gap)
    # Light corner strokes keep the rounded shape readable without overcomplicating the dash pattern.
    draw.arc(sc((x1, y1, x1 + 2 * radius, y1 + 2 * radius)), 180, 270, fill=outline, width=sc(width))
    draw.arc(sc((x2 - 2 * radius, y1, x2, y1 + 2 * radius)), 270, 360, fill=outline, width=sc(width))
    draw.arc(sc((x2 - 2 * radius, y2 - 2 * radius, x2, y2)), 0, 90, fill=outline, width=sc(width))
    draw.arc(sc((x1, y2 - 2 * radius, x1 + 2 * radius, y2)), 90, 180, fill=outline, width=sc(width))


img = Image.new("RGB", (sc(W), sc(H)), "#fbfaf8")
draw = ImageDraw.Draw(img)

# Outer soft border
draw.rounded_rectangle(sc((0, 0, W - 1, H - 3)), radius=sc(8), outline="#e8ded0", width=sc(1), fill="#fbfaf8")

# Boxes
dashed_rounded_rect(draw, (66, 52, 302, 147), 14, "#6d213d", "#f7e7ef", width=1.4, dash=5, gap=5)
draw.rounded_rectangle(sc((438, 46, 811, 153)), radius=sc(14), fill="#f8ecd8", outline="#c87818", width=sc(2))
draw.rounded_rectangle(sc((476, 230, 773, 314)), radius=sc(12), fill="#101010", outline="#101010", width=sc(1))
draw.rounded_rectangle(sc((252, 392, 488, 520)), radius=sc(14), fill="#eaf4df", outline="#245217", width=sc(2))
draw.rounded_rectangle(sc((614, 392, 850, 520)), radius=sc(14), fill="#e6f3ff", outline="#0c3f6e", width=sc(2))

# Connectors
dashed_line(draw, (302, 103), (425, 103), "#222222", width=1.2, dash=5, gap=4)
draw.polygon([sc((428, 103)), sc((417, 98)), sc((417, 108))], fill="#222222")
centered_text(draw, (364, 86), "经由 SKILLS.md", label_cn_font, "#4a3d39")
arrow(draw, (624, 153), (624, 220), width=1.2)
draw.line([sc((624, 314)), sc((624, 350))], fill="#222222", width=sc(1.2))
draw.line([sc((370, 350)), sc((732, 350))], fill="#222222", width=sc(1.2))
arrow(draw, (370, 350), (370, 381), width=1.2)
arrow(draw, (732, 350), (732, 381), width=1.2)

# Top-left box
centered_text(draw, (184, 72), "可选", label_cn_font, "#6d213d")
centered_text(draw, (184, 95), "你的 AI 代理", title_small_font, "#442033")
centered_text(draw, (184, 117), "CLAUDE · CODEX · OPENCLAW", caps_font, "#67304a")
centered_text(draw, (184, 135), "通过 SKILLS.md 接入", note_font, "#442033")

# Brain box
centered_text(draw, (624, 74), "大脑", label_cn_font, "#5a3b20")
centered_text(draw, (624, 101), "Airtap AI Cloud", title_font, "#392414")
centered_text(draw, (624, 126), "大脑 · 记忆 · 流程", caps_cn_font, "#724511")
centered_text(draw, (624, 141), "决定何时该做什么", note_font, "#6a421a")

# AutoPilot
centered_text(draw, (624, 262), "双手", label_cn_font, "#a9a9a9")
centered_text(draw, (624, 287), "AutoPilot", font(FONT_HEITI_MEDIUM, 22), "#ffffff")
centered_text(draw, (624, 304), "执行 · 点击 · 滚动 · 输入", caps_cn_font, "#bcbcbc")

# Cloud phone
centered_text(draw, (370, 424), "云手机", title_small_font, "#163d13")
centered_text(draw, (370, 451), "云端专用手机", body_font, "#1f3d1b")
centered_text(draw, (370, 469), "持续在线 · App 保持登录", body_font, "#1f3d1b")
centered_text(draw, (370, 496), "免设置 · 即开即用", caps_cn_font, "#1f3d1b")

# Physical devices
centered_text(draw, (732, 424), "实体设备", title_small_font, "#103b63")
centered_text(draw, (732, 451), "你的真实设备，你的应用", body_small_font, "#103b63")
centered_text(draw, (732, 470), "已安装 AutoPilot App", body_small_font, "#103b63")
centered_text(draw, (732, 496), "ANDROID · iOS · TV · PC", caps_font, "#103b63")

img = img.resize((W, H), Image.Resampling.LANCZOS)
img.save("architecture-zh.png", quality=95)
