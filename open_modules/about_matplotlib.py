# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
matplotlib 用于绘制数组的2D图形库
实例代码地址： https://matplotlib.org/stable/gallery/index.html
pip install matplotlib
'''

import numpy as np
from matplotlib import pyplot as plt


def test01():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    # 绘制出的图形，y轴范围是[1:4]，x轴范围是[0:3]
    # 当传入一个单维数组时，默认是作为y轴序列
    plt.show()


def test02():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    # 同时指定了x轴和y轴
    plt.show()


def test03():
    # 以红色的点来绘制，而不是连续线段
    # ro中r=red，o=圆点
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
    # 指定坐标轴范围：x轴[0:6]，y轴[0:20]
    plt.axis([0, 6, 0, 20])
    plt.show()


def test04():
    # 生成时间序列，范围[0:5]，步长0.2
    t = np.arange(0, 5, 0.2)
    # 同时绘制三条曲线："r--"-红色虚线,"bs"-蓝色方块,"g^"-绿色三角
    plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")
    plt.show()


def test05():
    x = np.arange(0, 5, 0.001)
    # 以下也是在同一坐标系绘制多条曲线
    # 同时演示了多种方式指定曲线属性，更多属性见：matplotlib.lines.Line2D
    plt.plot(x, x**2, linewidth=2.0)
    plt.plot(x, x**3, linewidth=2.0, color="blue")
    plt.step(x, x**4, color="red", linewidth=2.0)
    plt.show()


def f001(t):
    return np.exp(-t) * np.cos(2 * np.pi**t)


def test06():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    # 在同一个图形绘制多张子图
    plt.figure(1)
    # 第一张子图，211表示将绘制区域分割为2行1列，并且在第一个坐标系绘图
    plt.subplot(211)
    plt.plot(t1, f001(t1), "bo", t2, f001(t2), "k")

    # 第二张子图，212表示将绘制区域分割为2行1列，并且在第一个坐标系绘图
    plt.subplot(212)
    plt.plot(t2, np.cos(2 * np.pi * t2), "r--")
    plt.show()


def test07():
    # 第一个图形
    plt.figure(1)
    # 2, 1, 1=211
    plt.subplot(2, 1, 1)
    plt.plot([1, 2, 3])
    plt.subplot(212)
    plt.plot([4, 5, 6])

    # 第二个图形
    plt.figure(2)
    plt.plot([4, 5, 6])

    # 将第一幅图窗口前置为当前窗口
    plt.figure(1)
    # 选择第一幅子图并设置表名称
    plt.subplot(211)
    plt.title("Easy as 1, 2, 3")
    plt.show()


def test08():
    # 输出matplatlib字体配置文件路径
    # print(matplotlib.matplotlib_fname())
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)
    # 设置画布大小为600*650
    plt.figure(figsize=(6, 6.5))
    # 绘制直方图
    n, bins, patches = plt.hist(x, 50, density=True, stacked=True, facecolor="g", alpha=0.75)

    # 设置坐标名，表头名等信息
    plt.xlabel("Smarts（聪明度）")
    plt.ylabel("Probability（占比）")
    plt.title("Histogram of IQ")
    # 在坐标(60, .025)位置设置文本
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    # 打开网格
    plt.grid(True)
    plt.rcParams["font.style"] = "italic"
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = "SimHei"
    # 正确显示减号
    plt.rcParams["axes.unicode_minus"] = True
    plt.show()


def test09():
    x = np.arange(0, 5, 0.02)
    plt.plot(x, np.cos(2 * np.pi * x), "r--")
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = "SimHei"
    plt.rcParams["font.size"] = 15
    plt.rcParams["axes.unicode_minus"] = True
    plt.xlabel("横轴：时间", color="green")
    plt.ylabel("纵轴：振幅")
    plt.title(r"正弦波实例 $y=cos(2\pi x)$")
    plt.axis([-1, 6, -2, 2])
    # 在图上设置标注信息
    # xy=标注的坐标，xytext=标注文本的坐标，facecolor=箭头颜色，shrink=缩放比例，width=箭头线条宽度
    plt.annotate(r"$\mu=100$", xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor="black", shrink=0.1, width=3))
    plt.grid(True)
    plt.show()


def test10():
    t = np.arange(0.0, 1.0 + 0.01, 0.01)
    s = np.cos(4 * np.pi * t) + 2
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = "SimHei"
    plt.xlabel(r"textbf{time} (s)")
    plt.ylabel(r"textit{voltage} (mV)", fontsize=16)
    # title设置一个比较复杂的数据公式
    # color也支持#FF00FF 16进制表示方式
    plt.title(r"TeX is Number "
              r"$displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
              fontsize=16, color='gray')
    plt.plot(t, s)
    # 设置子图位置
    plt.subplots_adjust(top=0.8)
    plt.show()


def test11():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, men_means, width, label='Men', color="#FFFF00")
    rects2 = ax.bar(x + width / 2, women_means, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    for rect in rects1:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    test01()
