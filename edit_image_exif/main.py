"""
Date: 2022.07.26 20:45:03
LastEditors: Rustle Karl
LastEditTime: 2022.07.26 21:21:46
"""

# 1 pillow
# 这种方法可能有问题，可以确定的是，如果写入中文数据，即使是资源管理器都无法识别，
# 如果是英文，则其他程序可能也无法识别。

from PIL import Image
from PIL.ExifTags import TAGS

image_path = "test.jpg"

# Create a new image for testing
image = Image.new("RGB", (100, 100), "white")
image.save(image_path)

# Open the image
image = Image.open(image_path)

# Get basic metadata
metadata = {
    "Image.Size": image.size,
    "Image.Height": image.height,
    "Image.Width": image.width,
    "Image.Format": image.format,
    "Image.Mode": image.mode,
    "Image.Animated": getattr(image, "is_animated", False),
    "Image.Frames": getattr(image, "n_frames", 1),
}

# Extract EXIF data
exif_data = image.getexif()

if exif_data:
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        # metadata[tag_name] = value
        print(tag_name, value)
else:
    # https://exiftool.org/TagNames/EXIF.html
    exif_data.update(
        {
            0x010E: "desc",
            0x9C9B: "desc",
            0x9286: "desc",
            0x9C9E: "desc",
            0x9C9F: "desc",
        }
    )

image.save(image_path, exif=exif_data)

# 2 pyexiv2
# 这种方法比较完美

from pyexiv2 import Image

image = Image(image_path)

image.read_exif()
image.modify_exif(
    {
        "Exif.Image.ImageDescription": "测试",
        "Exif.Image.ExifTag": "2176",
        "Exif.Image.XPTitle": "测试",
        "Exif.Image.XPComment": "测试",
        "Exif.Image.XPKeywords": "测试",
        "Exif.Image.XPSubject": "测试",
    }
)
