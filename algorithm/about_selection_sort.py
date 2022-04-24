#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
选择排序
'''


def selection_sort(lst):
    if not lst or len(lst) == 1:
        return lst
    for i in range(0, len(lst) - 1):
        k = i
        # 每次子循环，都从未排序序列中选择最小的值
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[k]:
                k = j
        if k != i:
            lst[i], lst[k] = lst[k], lst[i]
    return lst


if __name__ == '__main__':
    lst = [12, 23, -45, 0, 1, 2, 3]
    selection_sort(lst)
    print(lst)
