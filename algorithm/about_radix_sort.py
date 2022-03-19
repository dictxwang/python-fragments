# -*- coding: utf8 -*-
__author__ = 'wangqiang'


"""
基数排序
如果要支持负数，需要注意扩充桶数量
不支持浮点数排序
"""


def radix_sort(lst):

    if not lst or len(lst) == 1:
        return lst
    # 找到最大数和最小数，确定基数比较轮次，以及桶数量
    min_num, max_num = lst[0], lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    radix_level = 0
    min_num_abs = abs(min_num)
    max_num_abs = abs(max_num)
    max_abs = max(min_num_abs, max_num_abs)
    while max_abs > 0:
        max_abs //= 10
        radix_level += 1

    # 是否包含负数
    has_negative = min_num_abs != min_num
    # 如果有负数，桶数量需要增加到19
    bucket_size = 19 if has_negative else 10
    bucket = [None] * bucket_size

    # 进行多轮基数计算
    for level in range(0, radix_level - 1):
        radix = pow(10, level)
        radix_next = pow(10, level + 1)
        for num in lst:
            # 前缀置零再计算当前基数值
            if num >= 0:
                remain = num % radix_next // radix
            else:
                # 负数转换成整数求基数，在取负数
                remain = 0 - abs(num) % radix_next // radix
            if has_negative:
                # 如果有负数，需要偏移下标
                bucket_index = remain + 9
            else:
                bucket_index = remain
            if bucket[bucket_index] is None:
                bucket[bucket_index] = []
            bucket[bucket_index].append(num)

        # 结束一轮之前，将bucket中的数取出重新填充待排序序列
        index = 0
        for i in range(bucket_size):
            while bucket[i] is not None and len(bucket[i]) > 0:
                # 按照先进先出取出
                lst[index] = bucket[i].pop(0)
                index += 1
    return lst


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 0, 0, 1, 2, 23, -2, -5, -456, 6, 8797, 53, 456, -12393]
    lst = radix_sort(lst)
    print(lst)
