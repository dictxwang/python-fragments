# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
插入排序：最坏时间复杂度 n^2
'''
import random


def insertion_sort(lst):
    total_swap = 0
    if not lst or len(lst) == 1:
        return total_swap

    for j in range(1, len(lst)):
        total_swap += 1
        # 选取当前待排序的元素
        key = lst[j]
        i = j - 1
        # 将待排序元素和已排序的序列元素进行比较
        # 如果待排序元素大于已排序元素，将已排序元素向后移一位，将其位置空出来
        while i >= 0 and lst[i] > key:
            total_swap += 1
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = key
    return total_swap


if __name__ == '__main__':

    lst = []
    for i in range(0, 1000):
        lst.append(random.randint(10, 50000))
    total_swap = insertion_sort(lst)
    print("total_swap: ", total_swap)  # 251000+
