from PIL import Image

img = Image.open("gmail.png")
img.save("gmail.ico", format="ICO")
