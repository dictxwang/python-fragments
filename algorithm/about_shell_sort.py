# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import random

'''
希尔排序：对插入排序的一种优化，关键点是步长的选择发生了变化
'''


def shell_sort(lst):
    # 通过改变步长，可以极大缩小交换次数
    # 当gap初始值是1时，就退化成插入排序
    gap = len(lst) // 2
    total_swap = 0
    while gap > 0:
        for j in range(gap, len(lst), gap):
            total_swap += 1
            key = lst[j]
            i = j - gap
            while i >= 0 and lst[i] > key:
                total_swap += 1
                lst[i + gap] = lst[i]
                i -= gap
            lst[i + gap] = key
        gap = gap // 2
    return total_swap


if __name__ == '__main__':

    lst = []
    for i in range(0, 1000):
        lst.append(random.randint(10, 50000))
    total_swap = shell_sort(lst)
    print("total_swap: ", total_swap)  # 15300+
