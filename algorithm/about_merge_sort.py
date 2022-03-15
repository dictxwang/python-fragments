# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
归并排序：最坏时间复杂度 n*lgn 采用分而治之的方式
'''


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    # 分别递归排序左右两个子序列
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    # 对已排序的子序列进行合并
    i = 0
    j = 0
    k = 0
    result = [0] * len(lst)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    # 将子序列多出的元素直接追加到结果序列中
    while i < len(left):
        result[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        result[k] = right[j]
        k += 1
        j += 1
    return result


if __name__ == '__main__':
    lst = [23, 1, 4, 5, -10, 56, 190, 230, 20, 30, 40, 50]
    lst = merge_sort(lst)
    print(lst)
