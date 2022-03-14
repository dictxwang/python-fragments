# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
快速排序
'''


def quick_sort(lst):
    if not lst:
        return lst
    middle_val = lst[len(lst) // 2]
    left = [x for x in lst if x < middle_val]
    middle = [x for x in lst if x == middle_val]
    right = [x for x in lst if x > middle_val]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    lst = [23, 1, 4, 56, -19, 30, 100, 0]
    lst = quick_sort(lst)
    print(lst)
