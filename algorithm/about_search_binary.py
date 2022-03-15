# -*- coding: utf8 -*-
__author__ = 'wangqiang'

"""
二分查找：二分查找的前提是待查找序列是有序的
"""


def binary_search(lst, pattern, offset=0):
    """
    二分查找
    :param lst: 待查找序列（切片）
    :param pattern: 查找元素
    :param offset: 切片下标偏移量（即从列表的offset元素开始查找匹配）
    :return:
    """
    if not lst or (len(lst) == 1 and lst[0] != pattern):
        return -1

    middle = (len(lst) - 1) // 2
    if pattern == lst[middle]:
        return offset + middle
    elif pattern > lst[middle]:
        # 待查找元素大于序列中间值，递归待右侧序列查找
        return binary_search(lst[middle + 1:], pattern, offset=offset+middle+1)
    else:
        return binary_search(lst[:middle], pattern, offset=offset)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
    print(binary_search(lst, 1))
    print(binary_search(lst, 3))
    print(binary_search(lst, 20))
    print(binary_search(lst, 6))
    print(binary_search(lst, -10))
    print(binary_search(lst, 100))
