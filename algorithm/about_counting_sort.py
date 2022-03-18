# -*- coding: utf8 -*-
__author__ = 'wangqiang'

"""
计数排序： 对n个0到k直接的数排序，时间复杂度和空间复杂度均为 O(n+k)，由于比较类排序
    如果初始参数未指定最大值，时间复杂度会增加，最差为O(2n+k)
    如果存在浮点数，算法不适用
"""


def counting_sort(lst):
    if not lst or len(lst) == 1:
        return lst

    # 找到最大值和最小值（注意可能存在负数）
    min_num, max_num = lst[0], lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    # 这里做一下优化，支持负数排序，同时减少计数序列的内存使用
    counting_length = max_num - min_num + 1
    # 计算最小值和0的距离，用于修正数组下标和保存的值
    min_range_zero = 0 - min_num
    counting_lst = [0] * counting_length
    for num in lst:
        real_index = num + min_range_zero
        counting_lst[real_index] += 1

    result = []
    for i in range(len(counting_lst)):
        while counting_lst[i] > 0:
            # 修正得到当前下标对应的真实数值
            result.append(i - min_range_zero)
            counting_lst[i] -= 1
    return result


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, 4, 5, 6, 7, 8]
    lst = counting_sort(lst)
    print(lst)
