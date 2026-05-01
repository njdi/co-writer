from PIL import Image, ImageDraw, ImageFont


BG = "#e9e6dc"
PANEL = "#f8f7f3"
TEXT = "#141414"
MUTED = "#85857f"
SUBTLE = "#62625d"
AXIS = "#8a8a84"
ERR = "#3f3f3c"

FONT_REG = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def size(draw, text, f):
    box = draw.textbbox((0, 0), text, font=f)
    return box[2] - box[0], box[3] - box[1]


def center(draw, width, y, text, f, fill):
    tw, th = size(draw, text, f)
    draw.text(((width - tw) / 2, y), text, font=f, fill=fill)
    return y + th


def center_in(draw, x0, x1, y, text, f, fill):
    tw, th = size(draw, text, f)
    draw.text((x0 + (x1 - x0 - tw) / 2, y), text, font=f, fill=fill)
    return y + th


def right(draw, x, y, text, f, fill):
    tw, _ = size(draw, text, f)
    draw.text((x - tw, y), text, font=f, fill=fill)


def rounded(draw, box, r, fill):
    draw.rounded_rectangle(box, radius=r, fill=fill)


def line(draw, xy, fill, width=2):
    draw.line(xy, fill=fill, width=width)


def render_figure2():
    w, h = 1920, 1080
    img = Image.new("RGBA", (w, h), BG)
    draw = ImageDraw.Draw(img)

    center(draw, w, 45, "各领域的谄媚行为", font(64, True), TEXT)
    center(draw, w, 121, "被评为谄媚的对话占比", font(35, True), SUBTLE)
    rounded(draw, (34, 187, 1885, 1038), 32, PANEL)

    labels = [
        "灵性",
        "人际关系",
        "个人成长",
        "其他",
        "职业 / 事业",
        "法律",
        "财务",
        "育儿",
        "健康 / 身体",
        "消费",
    ]
    values = [37.9, 24.8, 8.3, 8.3, 7.0, 7.0, 3.7, 3.6, 2.9, 2.9]
    colors = [
        "#c8c2ee",
        "#367321",
        "#b83b3b",
        "#c78a30",
        "#e6a2be",
        "#e16e6e",
        "#f5da94",
        "#5593cf",
        "#3c9279",
        "#ad4976",
    ]

    label_f = font(21, True)
    value_f = font(21, True)
    avg_f = font(20, True)
    x0, x1 = 408, 1435
    max_val = 38.0
    y0, step, bar_h = 282, 75, 39

    avg = 8.9
    avg_x = x0 + (x1 - x0) * avg / max_val
    line(draw, (avg_x, 245, avg_x, 987), AXIS, 2)
    draw.text((avg_x + 12, 242), "平均 8.9%", font=avg_f, fill=MUTED)

    for i, (lab, val, col) in enumerate(zip(labels, values, colors)):
        y = y0 + i * step
        right(draw, 392, y + 8, lab, label_f, MUTED)
        bw = int((x1 - x0) * val / max_val)
        rounded(draw, (x0, y, x0 + bw, y + bar_h), 5, col)
        draw.text((1564, y + 8), f"{val:.1f}%", font=value_f, fill=MUTED)

    img.save("20260501/01/images/figure2-cn.png")


def draw_error_bar(draw, x_start, x_end, y):
    line(draw, (x_start, y, x_end, y), ERR, 2)
    line(draw, (x_start, y - 7, x_start, y + 7), ERR, 2)
    line(draw, (x_end, y - 7, x_end, y + 7), ERR, 2)


def draw_model_panel(draw, box, title, rows):
    x0, y0, x1, y1 = box
    rounded(draw, box, 32, PANEL)
    center_in(draw, x0, x1, y0 + 67, title, font(35, True), SUBTLE)

    label_f = font(20, True)
    value_f = font(20, True)
    tick_f = font(19, True)
    bar_h = 45
    axis_x0, axis_x1 = x0 + 297, x0 + 823
    label_right = x0 + 282
    value_x = x0 + 795
    scale_max = 25.0
    ys = [y0 + 216, y0 + 291, y0 + 366, y0 + 441]

    for (name, val, col, err0, err1), y in zip(rows, ys):
        right(draw, label_right, y + 9, name, label_f, MUTED)
        bw = int((axis_x1 - axis_x0) * val / scale_max)
        rounded(draw, (axis_x0, y, axis_x0 + bw, y + bar_h), 6, col)
        ex0 = axis_x0 + (axis_x1 - axis_x0) * err0 / scale_max
        ex1 = axis_x0 + (axis_x1 - axis_x0) * err1 / scale_max
        draw_error_bar(draw, ex0, ex1, y + bar_h / 2)
        draw.text((value_x, y + 10), f"{val:.1f}%", font=value_f, fill=MUTED)

    axis_y = y0 + 540
    line(draw, (axis_x0, axis_y, axis_x1, axis_y), AXIS, 3)
    for tick in [0, 5, 10, 15, 20, 25]:
        tx = axis_x0 + (axis_x1 - axis_x0) * tick / scale_max
        line(draw, (tx, axis_y, tx, axis_y + 14), AXIS, 3)
        label = f"{tick}%"
        tw, _ = size(draw, label, tick_f)
        draw.text((tx - tw / 2, axis_y + 20), label, font=tick_f, fill=MUTED)


def render_figure3():
    w, h = 1920, 880
    img = Image.new("RGBA", (w, h), BG)
    draw = ImageDraw.Draw(img)

    center(draw, w, 47, "各模型的谄媚行为", font(64, True), TEXT)
    center(draw, w, 123, "被评为谄媚的回答占比（1-2 级），越低越好。", font(35, True), SUBTLE)

    names = [
        "Claude Sonnet 4.6",
        "Claude Opus 4.6",
        "Claude Opus 4.7",
        "Claude Mythos Preview",
    ]
    cols = ["#3c75ad", "#f2b34e", "#3c9279", "#db7654"]
    left_rows = [
        (names[0], 12.3, cols[0], 8.1, 17.5),
        (names[1], 10.7, cols[1], 6.8, 15.8),
        (names[2], 4.8, cols[2], 2.6, 8.9),
        (names[3], 2.2, cols[3], 0.8, 5.5),
    ]
    right_rows = [
        (names[0], 15.5, cols[0], 12.6, 18.8),
        (names[1], 12.1, cols[1], 9.3, 15.5),
        (names[2], 8.7, cols[2], 6.5, 11.0),
        (names[3], 4.9, cols[3], 3.0, 6.9),
    ]

    draw_model_panel(draw, (39, 195, 950, 849), "人际关系对话", left_rows)
    draw_model_panel(draw, (972, 195, 1883, 849), "全部咨询对话", right_rows)

    img.save("20260501/01/images/figure3-cn.png")


if __name__ == "__main__":
    render_figure2()
    render_figure3()
    print("20260501/01/images/figure2-cn.png")
    print("20260501/01/images/figure3-cn.png")
