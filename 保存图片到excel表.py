# -*- codeing = utf-8 -*-
# @Time : 2021/10/26 14:34
# @Author: 朱科
# @File : 保存图片到excel表.py
# @Software: PyCharm


import os
import xlwings as xw
import qrcode
import pygame
from PIL import Image
import shutil
from 将文字转成图片 import str_pic2, str_pic


def generate_save_pic(data, file=None, version=2, box_size=6, border=4):
    name = '1.png'
    qr = qrcode.QRCode(version=version, error_correction=qrcode.ERROR_CORRECT_L,
                       box_size=box_size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    pic = qr.make_image(fill_color='green', back_color='white')
    pic_path = mkdir(file, name)
    pic.save(pic_path)
    pic.close()
    return pic_path


def mkdir(file, name):
    if file != None and not os.path.exists(file):  # 两个条件不能交换
        os.mkdir(file)
    pic_path = os.path.join(os.getcwd(), name) if file == None else os.path.join(os.getcwd(), file, name)
    return pic_path


def generate_pic_paste_icon(pic_path, icon_path):
    name = 'paste.png'
    pic_image = Image.open(pic_path)
    icon_image = Image.open(icon_path)
    # 获取pic尺寸
    pic_w, pic_h = pic_image.size
    icon_w, icon_h = icon_image.size
    # 设置icon大小
    factor = 6
    size_w = int(pic_w / factor)
    size_h = int(pic_h / factor)
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h

    # 重新设置icon尺寸
    icon = icon_image.resize((icon_w, icon_h), Image.ANTIALIAS)
    # 计算坐标
    w = int((pic_w - icon_w) / 2)
    h = int((pic_h - icon_h) / 2)
    # 粘上图片
    pic_image.paste(icon, (w, h), mask=None)
    # pic_image.show()
    save_path = os.path.join(os.path.dirname(pic_path), name)
    pic_image.save(save_path)
    pic_image.close()
    return save_path


def pic_save_to_excel(file, sht='Sheet1', isVercode=True):
    picture = 'pic'#图片暂存文件夹

    # 打开表
    xb = xw.Book(file)
    # 打开工作薄
    sht = xb.sheets[sht]
    try:
        url_list = sht.range('A1').expand('down').value  # 选取第一列的值  这里有个BUg,当这列只有一个值时，len(url_list)=3
        verifycode_list = sht.range('B1').expand('down').value  # 选取第二列的值

        for i in range(len(url_list)):
            icon_path, pic_save_path, temp_path = '', '', ''
            finally_pic_path = generate_save_pic(url_list[i], picture)
            pic_save_path=finally_pic_path
            if isVercode:
                icon_path = str_pic2(str(verifycode_list[i]), picture)
                temp_path = generate_pic_paste_icon(finally_pic_path, icon_path)
                finally_pic_path = temp_path
            pic = Image.open(finally_pic_path)
            # 获取二维码图片大小
            _width, _height = pic.size
            # 设置表的单元格大小
            rng = sht.range('C{}'.format(i + 1))
            rng.column_width = (_width + 2)/5#行高和列宽单位有误差
            rng.row_height = _height + 2
            # 图片居中显示
            left = rng.left + (rng.column_width*5 - _width) / 2
            top = rng.top + (rng.row_height - _height) / 2
            # 插入表
            sht.pictures.add(finally_pic_path, left=left, top=top, width=_width, height=_height)
            pic.close()
            os.remove(finally_pic_path)
            if isVercode:
                os.remove(icon_path)
                os.remove(pic_save_path)
            # rng.autofit()  # 自动调整单元格大小，  须在填入内容再调用
        xb.save()
        xb.close()
    except TypeError as e:
        print('{}没有可操作内容'.format(sht))


if __name__ == '__main__':
    file = r"C:\Users\65606\Desktop\new251.xlsx"
    # pic_save_to_excel(file, 'Sheet1',False)
    xb = xw.Book(file)
    # 打开工作薄
    sht = xb.sheets['Sheet1']
    a=sht.range('C1').expand('down').value
    print(len(a))

