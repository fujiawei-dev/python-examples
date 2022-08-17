"""
Date: 2022.01.31 14:59
Description: 一张图去除中间一部分
LastEditors: Rustle Karl
LastEditTime: 2022.01.31 14:59
"""

from PIL import Image

image_path = "main.png"

image = Image.open(image_path)

image_width, image_height = image.size

part1 = image.crop((0, 0, image_width, 150))
part2 = image.crop((0, 420, image_width, image_height))

image_new = Image.new(
    "RGB",
    (image_width, part1.size[1] + part2.size[1]),
    (255, 255, 255),
)

image_new.paste(part1)
image_new.paste(part2, (0, part1.size[1]))
image_new.show()
