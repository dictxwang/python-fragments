#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "wangqiang"

'''
利用最小堆排序
'''

def minimum_heap_sort(lst):

    def sift_up(current, end):

        latest = current
        left = current * 2 + 1
        right = current * 2 + 2

        if left < end and lst[left] < lst[latest]:
            latest = left
        if right < end and lst[right] < lst[latest]:
            latest = right
        if latest != current:
            lst[latest], lst[current] = lst[current], lst[latest]
            sift_up(latest, end)

    # 先建立最小堆
    for i in range(len(lst) - 1, -1, -1):
        sift_up(i, len(lst))
    print(lst)

    # 通过遍历重建最小堆，实现排序
    # 这里排完序是逆序的，这样便于树重建的实现
    for i in range(len(lst) - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        sift_up(0, i)

    # 再进行一次逆序处理
    for i in range(0, len(lst) // 2):
        lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]


if __name__ == '__main__':
    lst = [2, 1, 7, 6, 51, 200, -12, 340, 20, -12, 340]
    minimum_heap_sort(lst)
    print(lst)
