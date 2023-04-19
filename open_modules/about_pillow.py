#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "wangqiang"

'''
图像处理模块 pillow
pip install pillow
'''
import PIL
from PIL import Image


def open_and_show():
    img = Image.open("data/lenna.png")
    img.show()

    print("width: ", img.width)
    print("height: ", img.height)
    print("size: ", img.size)
    print("mode: ", img.mode)
    print("format: ", img.format)
    print("is_animated: ", img.is_animated)
    print("readonly: ", img.readonly)
    print("info: ", img.info)


def rotate_1():
    img = Image.open("data/fruit.jpg")
    rotated = img.rotate(90, expand=True)  # expand=True 防止旋转出现黑边
    rotated.show()


def rotate_2():
    img = Image.open("data/fruit.jpg")
    rotated = img.transpose(Image.ROTATE_90)  # 使用transpose防止出现黑边
    rotated.show()


if __name__ == '__main__':
    # open_and_show()
    # rotate_1()
    rotate_2()
