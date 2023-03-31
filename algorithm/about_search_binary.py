# -*- coding: utf8 -*-
__author__ = 'wangqiang'

"""
二分查找：二分查找的前提是待查找序列是有序的
"""


def do_binary_search(lst, pattern, start, end):
    """
    二分查找
    :param lst: 待查找序列（切片）
    :param pattern: 查找元素
    :param start: 起始查找下标
    :param end: 结束查找下标
    :return:
    """
    if not lst or start > end:
        return -1
    middle_index = (end - start + 1) // 2 + start
    middle_value = lst[middle_index]
    if middle_value == pattern:
        return middle_index
    elif middle_value > pattern:
        # 继续在左子树查找
        return do_binary_search(lst, pattern, start, middle_index - 1)
    else:
        # 继续在右子树查找
        return do_binary_search(lst, pattern, middle_index + 1, end)


def binary_search(lst, pattern):
    return do_binary_search(lst, pattern, 0, len(lst) - 1)
    

if __name__ == '__main__':
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
    start = 0
    end = len(lst) - 1
    print(binary_search(lst, 0))
    print(binary_search(lst, 1))
    print(binary_search(lst, 3))
    print(binary_search(lst, 20))
    print(binary_search(lst, 6))
    print(binary_search(lst, -10))
    print(binary_search(lst, 100))
