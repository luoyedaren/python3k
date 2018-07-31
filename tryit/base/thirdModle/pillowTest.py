from PIL import Image, ImageFilter

im = Image.open('1.jpg')  # type: Image.Image
w, h = im.size
print(w, h)
im.thumbnail((w // 2, h // 2))

im.save('thumbnail.jpg', 'jpeg')

im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
