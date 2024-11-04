from PIL import Image, ImageDraw
import numpy as np

# GIF 的大小和帧数
width, height = 1125, 522
num_frames = 20

frames = []
for i in range(num_frames):
    # 创建一个空白的图像
    img = Image.new('RGB', (width, height), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 添加一些简单的内容，例如颜色渐变
    color = int(255 * (i / num_frames))
    draw.rectangle([0, 0, width, height], fill=(color, color, 255 - color))

    # 保存每一帧
    frames.append(img)

# 将帧保存为GIF
frames[0].save('soutput.gif', save_all=True, append_images=frames[1:], loop=0, duration=100)
