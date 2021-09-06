# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
有关排序算法的应用
'''


def quick_sort(lst):
    if not lst or len(lst) <= 1:
        return lst
    middle_val = lst[len(lst) // 2]
    left = [x for x in lst if x < middle_val]
    middle = [x for x in lst if x == middle_val]
    right = [x for x in lst if x > middle_val]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    lst = [10, 3, 2, 7, 8, 3, 2, 1, 0, 5]
    print(quick_sort(lst))
