# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
matplotlib 用于绘制数组的2D图形库
实例代码地址： https://matplotlib.org/stable/gallery/index.html
pip install matplotlib
'''

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from matplotlib import pyplot as plt


def test01():
    '''
    曲线图
    :return:
    '''
    a = np.linspace(0, 10, 100)
    b = np.exp(-a)
    plt.plot(a, b)
    plt.show()


def test02():
    '''
    直方图
    :return:
    '''
    x = np.random.normal(size=200)
    plt.hist(x, bins=30, color="y")
    plt.show()


def test03():
    '''
    散点图
    :return:
    '''
    a = np.random.random(100)
    b = np.random.random(100)
    plt.scatter(a, b)
    plt.show()


def test04():
    '''
    3D图
    :return:
    '''
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    x = np.arange(-5, 5, 0.25)
    y = np.arange(-5, 5, 0.25)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x**2 + y**2)
    z = np.sin(r)
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm)
    plt.show()


if __name__ == "__main__":
    test04()
