# 引入第三方库，PIL安装注意坑
from PIL import Image

#创建一张新图片
image = Image.new('RGB', (160, 90), (0, 0, 255))   #mode, size, color
image.show()

# 查看图片信息
im = Image.open("../out/default.jpg")
im.show()

im2 = im.convert('1')
im2.show()
im2.save("../out/im2.png")

print(im.format, im.size, im.mode, im.getbands(),im.info)
#     JPEG   (1920, 1080)   RGB    通道('R', 'G', 'B')


# 滤波器:将多个输入像素映射为一个输出像素
im_resize = im.resize((256,256))
print ( im_resize.size)



im_resize0 = im.resize((256,256), Image.BILINEAR)
print (im_resize0.size)


im.thumbnail((200, 100),Image.BILINEAR)
print(im.size)

#im.save("new.jpg", "JPEG")
