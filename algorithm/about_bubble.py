# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
冒泡排序
'''


def bubble_sort(lst):
    if not lst or len(lst) == 1:
        return lst
    for out in range(0, len(lst) - 1):
        for inner in reversed(range(out + 1, len(lst))):
            if lst[inner] < lst[inner - 1]:
                lst[inner], lst[inner - 1] = lst[inner - 1], lst[inner]


if __name__ == '__main__':
    lst = [12, 23, -45, 0, 1, 2, 3]
    bubble_sort(lst)
    print(lst)
