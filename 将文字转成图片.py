# -*- codeing = utf-8 -*-
# @Time : 2021/10/27 13:56
# @Author: 朱科
# @File : 将文字转成图片.py
# @Software: PyCharm


import os
import pygame
from PIL import Image, ImageFont, ImageDraw


def str_pic(s,file=None):
    path = 'str_pic.png'
    # 此方法生成的图片不是矢量图
    pygame.init()
    # 当前目录下要有微软雅黑的字体文件msyh.ttc,或者去c:\Windows\Fonts目录下找
    font = pygame.font.Font(os.path.join(r'c:\Windows\Fonts', 'simsun.ttc'), 14)
    rtext = font.render(s, True, (0, 0, 0), (255, 255, 255))
    pygame.image.save(rtext, path)
    # pygame.image.close()
    if file!=None and not os.path.exists(file) :
        os.mkdir(file)
    return os.path.join(os.getcwd(), path) if file==None else os.path.join(os.getcwd(),file,path)


def str_pic2(text, file=None):
    name = 'create_img.png'
    fontSize = 30
    lines = text.split('\n')
    im = Image.new("RGB", (90, len(lines) * (fontSize + 5)), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    fontPath = r"C:\Windows\Fonts\STKAITI.TTF"
    # font = ImageFont.truetype(r"C:\Windows\Fonts\AdobeHeitiStd-Regular.otf", 25)
    font = ImageFont.truetype(fontPath, fontSize)
    dr.text((0, 0), text, font=font, fill='green')
    if file!=None and not os.path.exists(file):#两个条件不能交换
        os.mkdir(file)
    pic_path= os.path.join(os.getcwd(),name) if file==None else os.path.join(os.getcwd(),file,name)
    im.save(pic_path)
    im.close()
    return pic_path
    # im.show()
if __name__ == '__main__':
    # str_pic('哈哈','22.png')
    str_pic2('吃菌哈哈','bb')
