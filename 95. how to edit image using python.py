from PIL import Image
img1=Image.open(r"C:\Users\ACER\Desktop\keshav\car.jpg")
img1.save(r'C:\Users\ACER\Desktop\keshav\car.png')
img1.show()
max_size=(250,255)
img1.thumbnail(max_size)
img1.save(r'C:\Users\ACER\Desktop\keshav\smallcar.jpg')
img2=Image.open(r"C:\Users\ACER\Desktop\keshav\smallcar.jpg")
img2.show()
from PIL import ImageEnhance # module for shrpness,contrast,color,brightness etc
img3=Image.open(r"C:\Users\ACER\Desktop\keshav\car.jpg")
enhancer=ImageEnhance.Sharpness(img3)
enhancer.enhance(500)# this method will give new sharpness to image
img3.save(r"C:\Users\ACER\Desktop\keshav\newimage.jpg")
new_image=Image.open(r"C:\Users\ACER\Desktop\keshav\newimage.jpg")
new_image.show()
from PIL import ImageFilter
img1.filter(ImageFilter.GaussianBlur())
img1.save(r"C:\Users\ACER\Desktop\keshav\blurryimg.jpg")
blur=Image.open(r"C:\Users\ACER\Desktop\keshav\blurryimg.jpg")
blur.show()
