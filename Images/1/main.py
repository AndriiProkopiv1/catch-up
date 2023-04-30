from PIL import Image


with Image.open("original.jpg") as original:
    original.show()
    print(original.size)
    print(original.format)
    print(original.mode)

    bw = original.convert("L")
    bw.show()

    pic_blur = original.filter(ImageFilter.BLUR)
    pic_blur.show()

    left = original.transpose(Image.ROTATE_90)
    left.show()

    right = original.transpose(Image.ROTATE_270)
    right.show()