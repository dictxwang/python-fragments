# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
pip install opencv-python==3.4.2.16
pip install opencv-contrib-python==3.4.2.16
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt


def test01():
    '''
    怀旧特效，按照下面的通道值转换公式进行
    r_new=0.393*r+0.769*g+0.189*b;
    g_new=0.349*r+0.686*g+0.168*b;
    b_new=0.272*r+0.534*g+0.131*b;
    :return:
    '''
    img = cv2.imread("data/lenna.png")
    b1, g1, r1 = cv2.split(img)
    # 获取图片的行列
    rows, cols = img.shape[:2]
    # 新建目标图像
    dst = np.zeros((rows, cols, 3), dtype="uint8")
    for i in range(rows):
        for j in range(cols):
            b = img[i][j][0]
            g = img[i][j][1]
            r = img[i][j][2]
            r_new = 0.393 * r + 0.769 * g + 0.189 * b
            g_new = 0.349 * r + 0.686 * g + 0.168 * b
            b_new = 0.272 * r + 0.534 * g + 0.131 * b
            r_new = 255 if r_new > 255 else r_new
            g_new = 255 if g_new > 255 else g_new
            b_new = 255 if b_new > 255 else b_new
            dst[i, j] = np.uint8((b_new, r_new, g_new))
    b, g, r = cv2.split(dst)
    plt.subplot(1, 2, 1)
    plt.title("original")
    plt.imshow(cv2.merge([r1, g1, b1]))
    plt.subplot(1, 2, 2)
    plt.title("old")
    plt.imshow(cv2.merge([r, g, b]))
    plt.show()


def test02():
    '''
    素描特效处理
    :return:
    '''
    img = cv2.imread("data/lenna.png")
    # 图像灰度处理
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 高斯滤波降噪（降低噪点，并对图片进行平滑过渡）
    gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
    # canny算子（用作图像边缘检测）
    canny = cv2.Canny(gaussian, 50, 150)
    # 阈化值处理
    ret, result = cv2.threshold(canny, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    b, g, r = cv2.split(img)
    plt.subplot(2, 3, 1)
    plt.title("Original-Image")
    plt.imshow(cv2.merge([r, g, b]))
    plt.subplot(2, 3, 2)
    plt.title("Gray-Image")
    plt.imshow(gray, cmap="gray")
    plt.subplot(2, 3, 3)
    plt.title("Sketch-Image")
    plt.imshow(result, cmap="gray")

    # 将灰度图和变换和的素描图横向向拼接后显示
    plt.subplot(2, 3, 4)
    plt.title("Gray-Result")
    plt.imshow(np.hstack((gray, result)), cmap="gray")
    plt.show()


def test03():
    '''
    光照特效处理(围绕中心点光照增强)
    :return:
    '''
    img = cv2.imread("data/lenna.png")
    rows, cols = img.shape[:2]

    center_x = int(rows / 2 - 20)
    center_y = int(cols / 2 + 20)
    radius = min(center_x, center_y)
    strength = 100

    dst = np.zeros((rows, cols, 3), dtype="uint8")
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt(np.power((center_y - j), 2) + np.power((center_x - i), 2))
            b = img[i, j][0]
            g = img[i, j][1]
            r = img[i, j][2]
            if distance < radius:
                result = (int)(strength * (1 - distance / radius))
                b = b + result
                g = g + result
                r = r + result
                b = min(255, max(0, b))
                g = min(255, max(0, g))
                r = min(255, max(0, r))
            dst[i, j] = np.uint8((b, g, r))
    b0, g0, r0 = cv2.split(img)
    b1, g1, r1 = cv2.split(dst)
    plt.subplot(1, 2, 1)
    plt.title("Original-Image")
    plt.imshow(cv2.merge([r0, g0, b0]))
    plt.subplot(1, 2, 2)
    plt.title("Light-Image")
    plt.imshow(cv2.merge([r1, g1, b1]))
    plt.show()


def test04():
    '''
    光照特效处理(开窗模式)
    :return:
    '''
    img = cv2.imread("data/lenna.png")
    h, w, c = img.shape
    dst = np.zeros((h, w, c), dtype="uint8")
    strength = 50
    for i in range(h):
        for j in range(w):
            b = img[i, j][0]
            g = img[i, j][1]
            r = img[i, j][2]
            if 100 < i < 200 and 200 < j < 400 and b > 40:
                b = min(255, b + strength)
                g = min(255, g + strength)
                r = min(255, r + strength)
            dst[i, j][0] = b
            dst[i, j][1] = g
            dst[i, j][2] = r
    b0, g0, r0 = cv2.split(img)
    b1, g1, r1 = cv2.split(dst)
    plt.subplot(1, 2, 1)
    plt.title("Original-Image")
    plt.imshow(cv2.merge([r0, g0, b0]))
    plt.subplot(1, 2, 2)
    plt.title("Light-Image")
    plt.imshow(cv2.merge([r1, g1, b1]))
    plt.show()


def test05():
    '''
    图片整体变暗/变亮
    :return:
    '''
    img = cv2.imread("data/lenna.png")
    rows, cols = img.shape[:2]
    strength = 50
    bright = np.copy(img)
    dark = np.copy(img)
    for i in range(rows):
        for j in range(cols):
            bb = min(255, img[i, j][0] + strength)
            bg = min(255, img[i, j][1] + strength)
            br = min(255, img[i, j][2] + strength)
            bright[i, j] = np.uint8((bb, bg, br))
            db = max(0, img[i, j][0] - strength)
            dg = max(0, img[i, j][1] - strength)
            dr = max(0, img[i, j][2] - strength)
            dark[i, j] = np.uint8((db, dg, dr))
    b0, g0, r0 = cv2.split(img)
    b1, g1, r1 = cv2.split(bright)
    b2, g2, r2 = cv2.split(dark)
    plt.subplot(1, 3, 1)
    plt.title("Original-Image")
    plt.imshow(cv2.merge([r0, g0, b0]))
    plt.subplot(1, 3, 2)
    plt.title("Bright-Image")
    plt.imshow(cv2.merge([r1, g1, b1]))
    plt.subplot(1, 3, 3)
    plt.title("Dark-Image")
    plt.imshow(cv2.merge([r2, g2, b2]))
    plt.show()


def test06():
    '''
    流年特效处理（将蓝色B通道的值开根号在乘以一个权重值）
    :return:
    '''
    img = cv2.imread("data/fruit.jpg")
    rows, cols = img.shape[:2]
    dst = np.copy(img)
    for i in range(rows):
        for j in range(cols):
            b = np.sqrt(dst[i, j][0]) * 12
            dst[i, j][0] = min(255, b)
    b0, g0, r0 = cv2.split(img)
    b1, g1, r1 = cv2.split(dst)
    plt.subplot(1, 2, 1)
    plt.title("Original-Image")
    plt.imshow(cv2.merge([r0, g0, b0]))
    plt.subplot(1, 2, 2)
    plt.title("LongTime-Image")
    plt.imshow(cv2.merge([r1, g1, b1]))
    plt.show()


def test07():
    '''
    滤镜效果（LUT方式滤镜）
    LUT： Look Up Table
    :return:
    '''
    # 加载LUT图片（不同的LUT图会呈现不同的效果）
    f = cv2.imread("data/lvjing2.png")
    img = cv2.imread("data/lenna.png")
    rows, cols = img.shape[:2]
    dst = np.zeros((rows, cols, 3), dtype="uint8")
    for i in range(rows):
        for j in range(cols):
            b, g, r = img[i, j]
            # 通过原图的bgr计算对应的标准色坐标
            x = int(g / 4 + int(b / 32) * 64)
            y = int(r / 4 + int((b % 32) / 4) * 64)
            fb, fg, fr = f[x, y]
            dst[i, j] = np.uint8((fb, fg, fr))

    b0, g0, r0 = cv2.split(img)
    b1, g1, r1 = cv2.split(dst)
    plt.subplot(1, 2, 1)
    plt.title("Original-Image")
    plt.imshow(cv2.merge([r0, g0, b0]))
    plt.subplot(1, 2, 2)
    plt.title("Filter-Image")
    plt.imshow(cv2.merge([r1, g1, b1]))
    plt.show()


if __name__ == "__main__":
    # test01()
    # test02()
    # test03()
    test04()
    # test05()
    # test06()
    # test07()
