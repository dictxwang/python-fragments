# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
matplotlib 用于绘制数组的2D图形库
实例代码地址： https://matplotlib.org/stable/gallery/index.html
pip install matplotlib
'''

from matplotlib import pyplot as plt


def test_01():

    values = []
    fp = open("data/matplotlib_03_01.txt", mode="r")
    for line in fp.readlines():
        line = line.strip("\n")
        values.append(int(line))
    fp.close()

    plt.plot(values)
    plt.ylabel("WebSocket Delay (micros)")
    plt.show()

def test_02():

    values = []
    fp = open("data/matplotlib_03_02.txt", mode="r")
    for line in fp.readlines():
        line = line.strip("\n")
        values.append(int(line))
    fp.close()

    plt.plot(values)
    plt.ylabel("WebSocket Delay (micros)")
    plt.show()


if __name__ == '__main__':
    test_02()
