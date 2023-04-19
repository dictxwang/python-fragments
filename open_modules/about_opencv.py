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
    以灰度方式读取图片
    cv2.IMREAD_GRAYSCALE=0
    :return:
    '''
    img = cv2.imread("data/lenna.png", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("图片-灰度显示", img)
    cv2.waitKey()


def test02():
    '''
    保存图片，键盘交互
    :return:
    '''
    img = cv2.imread("data/lenna.png", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("灰度显示-另存", img)
    key = cv2.waitKey()
    if key == ord("y"):
        # 另存图片
        cv2.imwrite("data/opencv_test_02_out.png", img)
    cv2.destroyAllWindows()


def test03():
    '''
    通过matplotlib显示灰度图片
    :return:
    '''
    img = cv2.imread("data/lenna.png", 0)
    plt.imshow(img, cmap="gray", interpolation="bicubic")
    plt.xticks([])
    plt.yticks([])
    plt.show()


def test04():
    '''
    opencv与matplotlib图片显示的通道转换问题
    opencv以BGR模式加载，matplotlib以RGB模式加载
    :return:
    '''
    img = cv2.imread("data/lenna.png")  # 默认以彩色方式加载图片 cv2.IMREAD_COLOR = 1
    cv2.imshow("BGR", img)
    cv2.waitKey(0)

    # 直接打开cv2加载的图片，颜色不对
    plt.imshow(img)
    plt.title("BGR")
    plt.show()


def test05():
    '''
    图像通道的转换 BGR -> RGB
    :return:
    '''
    img = cv2.imread("data/lenna.png")
    b, g, r = cv2.split(img)

    img2 = cv2.merge([r, g, b])
    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.title("BGR")

    plt.subplot(2, 2, 2)
    plt.imshow(img2)
    plt.title("RGB")

    img3 = cv2.merge([g, r, b])
    plt.subplot(2, 2, 3)
    plt.imshow(img3)
    plt.title("GRB")

    img4 = cv2.merge([g, g, g])
    plt.subplot(2, 2, 4)
    plt.imshow(img4)
    plt.title("GGG")
    plt.show()


def test06():
    '''
    展示单通道效果
    :return:
    '''
    img = cv2.imread("data/lenna.png", 1)
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    plt.subplot(1, 4, 1)
    plt.title("RGB")
    plt.imshow(img2, "gray")

    plt.subplot(1, 4, 2)
    plt.title("R-Channel")
    plt.imshow(r, "gray")

    plt.subplot(1, 4, 3)
    plt.title("G-Channel")
    plt.imshow(g, "gray")

    plt.subplot(1, 4, 4)
    plt.title("B-Channel")
    plt.imshow(b, "gray")
    plt.show()


def test07():
    '''
    通道的叠加修改
    :return:
    '''
    img = cv2.imread("data/fruit.jpg", 1)
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])

    plt.subplot(1, 3, 1)
    plt.title("RGB")
    plt.imshow(img2)

    # red通道减去blue通道
    real_r = r - b
    plt.subplot(1, 3, 2)
    plt.title("R-Channel")
    plt.imshow(real_r, "gray")

    # 阈值处理，过滤掉干扰
    ret, threshold_r = cv2.threshold(real_r, 100, 150, cv2.THRESH_BINARY)
    plt.subplot(1, 3, 3)
    plt.title("Threshold-Image")
    plt.imshow(threshold_r, "gray")
    plt.show()


def test08():
    '''
    通道转换：BGR -> RGB，通过cvtColor的方式
    :return:
    '''
    img = cv2.imread("data/apple.jpg")
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.subplot(1, 2, 1)
    plt.title("BGR")
    plt.imshow(img)
    plt.subplot(1, 2, 2)
    plt.title("RGB")
    plt.imshow(img2)
    plt.show()


def test09():
    '''
    显示自定义的灰度级别图
    这种方式显示的不是256级别的灰度图，而是以自定义的最大值为最高级别
    :return:
    '''
    img = np.array([[0, 1, 1, 0, 0],
                    [3, 4, 0, 2, 1],
                    [3, 2, 1, 0, 2],
                    [2, 1, 1, 0, 3],
                    [2, 3, 3, 4, 4]])
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.imshow(img, cmap="gray")
    plt.colorbar()
    plt.show()


def test10():
    '''
    opencv和matplotlib显示灰度图的差别对比
    cv2显示的才是真实的灰度图
    :return:
    '''
    img = cv2.imread("data/xingqiu.jpg", 0)
    cv2.imshow("image", img)
    plt.imshow(img, cmap="gray")
    plt.show()
    cv2.waitKey()


def test11():
    '''
    matplotlib正确显示灰度图的方法
    :return:
    '''
    img = cv2.imread("data/xingqiu.jpg", 0)
    # 将单通道转换成三通道
    threeChannel = np.concatenate((np.expand_dims(img, axis=2),
                                   np.expand_dims(img, axis=2),
                                   np.expand_dims(img, axis=2)), axis=-1)
    cv2.imshow("image", img)
    plt.imshow(threeChannel)
    plt.show()
    cv2.waitKey()


def test12():
    '''
    分离RBG三通道灰度图（使用标准的颜色图）
    :return:
    '''
    img = cv2.imread("data/rgb_circle.jpg")
    b, g, r = cv2.split(img)
    # 需要构造有一个与image形状相同的零矩阵
    zeros = np.zeros(img.shape[:2], dtype="uint8")

    # 需要通过零矩阵叠加，去掉不属于当前通道的信息
    # 如果是使用matplotlib显示，需要将BRG转换成RGB
    mb = cv2.merge([zeros, zeros, b])
    mg = cv2.merge([zeros, g, zeros])
    mr = cv2.merge([r, zeros, zeros])
    plt.subplot(1, 5, 1)
    plt.title("RGB")
    plt.imshow(cv2.merge([r, g, b]))

    plt.subplot(1, 5, 2)
    plt.title("R-Channel")
    # 圆圈是纯色，显示效果是绿色和蓝色圆圈会变成黑色
    # 因为这一步只保留红色通道，而绿色和蓝色在红色通道的值全为0
    # 如果不是纯色的图片，则不会是纯黑色，因为其在红色通道值仍然不为0
    plt.imshow(mr)

    plt.subplot(1, 5, 3)
    plt.title("G-Channel")
    plt.imshow(mg)

    plt.subplot(1, 5, 4)
    plt.title("B-Channel")
    plt.imshow(mb)

    mm = cv2.merge([r, g, b])
    plt.subplot(1, 5, 5)
    plt.title("Merge")
    plt.imshow(mm)
    plt.show()


def test13():
    '''
    叠加alpha通道
    '''
    img = cv2.imread("data/xingqiu.jpg")
    img_bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    b, g, r, a = cv2.split(img_bgra)
    a = np.ones(b.shape, dtype=b.dtype) * 255
    a[:, :int(b.shape[0] / 2)] = 100  # 改变右半边的透明度

    img_merge = cv2.merge((b, g, r, a))
    cv2.imwrite("data/xingqiu_alpha.png", img_merge)


def test14():
    '''
    图像翻转
    '''
    img = cv2.imread("data/fruit.jpg")
    h, w = img.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 45, 1.0)  # 参数90表示逆时针旋转90°

    # 计算旋转后的长和宽
    rotated_h = int((w * np.abs(M[0, 1]) + (h * np.abs(M[0, 0]))))
    rotated_w = int((h * np.abs(M[0, 1]) + (w * np.abs(M[0, 0]))))
    M[0, 2] += (rotated_w - w) // 2
    M[1, 2] += (rotated_h - h) // 2

    # 执行旋转
    rotated_img = cv2.warpAffine(img, M, (rotated_w, rotated_h))
    cv2.imshow("rotated image", rotated_img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def test15():
    '''
    图片抠图
    '''
    img = cv2.imread("data/lenna.png")

    bboxes = [
        [200, 200, 200, 200],
        [100, 100, 100, 100],
        [190, 80, 90, 300]
    ]
    bbox_index = np.zeros([*img.shape[:2]]).astype(bool)
    for bbox in bboxes:
        bbox_index[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]] = True
    img[np.where(~bbox_index)] = 0
    cv2.imshow("bk_img", img)
    cv2.waitKey()


if __name__ == "__main__":
    # test01()
    # test02()
    # test03()
    # test04()
    # test05()
    # test06()
    # test07()
    # test08()
    # test09()
    # test10()
    # test11()
    # test12()
    # test13()
    # test14()
    test15()
