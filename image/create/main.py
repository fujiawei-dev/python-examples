from PIL import Image

image = Image.new("RGB", (50, 50))

image_path = "main.png"
image.save(image_path)
