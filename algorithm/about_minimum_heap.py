#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "wangqiang"

'''
最小堆的实现
数组表示法：子节点下标//2，正好是父节点下标；第一个叶子节点下标是count//2
    当前节点下标*2+1是其左子节点下标，当前节点下标*2+2是其右子节点下标
'''


class MinHeap:

    def __init__(self, lst):
        self._data = []
        self._count = 0

        for v in lst:
            self._data.append(v)
            self._count += 1

        for i in range(self._count - 1, -1, -1):
            self.sift_up(i)

    def sift_up(self, index):
        latest = index

        left = index * 2 + 1
        right = index * 2 + 2
        if left < self._count and self._data[left] < self._data[latest]:
            # 左子节点小于当前节点，与左子节点交换
            latest = left
        if right < self._count and self._data[right] < self._data[latest]:
            # 右子节点小于当前节点，与右子节点交换
            latest = right
        if latest != index:
            self._data[index], self._data[latest] = self._data[latest], self._data[index]
            self.sift_up(latest)

    def print(self):
        print(self._data)


if __name__ == '__main__':
    lst = [10, 20, 9, 4, 5, 30, 2, 2, -10, 50, 100, 340]
    min_heap = MinHeap(lst)
    min_heap.print()
