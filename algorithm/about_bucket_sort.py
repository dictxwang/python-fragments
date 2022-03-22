# -*- coding: utf8 -*-
__author__ = 'wangqiang'


"""
桶排序：桶排序可以看做是计数排序的升级版，不过分桶以后会采取分而治之的方式各自排序
    假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）
"""

import about_insertion_sort


def bucket_sort(lst, bucket_size=5):
    """
    桶排序
    :param lst: 待排序序列
    :param bucket_size: 桶大小
    :return:
    """
    if not lst or len(lst) == 1:
        return
    min_num, max_num = lst[0], lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    bucket_size = bucket_size if bucket_size > 0 else 5
    bucket_count = (max_num - min_num) // bucket_size + 1

    # 将数据按照指定的分布算法放到对应的桶
    buckets = [None] * bucket_count
    for num in lst:
        mod = (num - min_num) // bucket_size
        if not buckets[mod]:
            buckets[mod] = [num]
        else:
            buckets[mod].append(num)

    lst_index = 0
    for i in range(bucket_count):
        # 这里采用插入排序对每个桶分布排序
        about_insertion_sort.insertion_sort(buckets[i])
        for j in range(len(buckets[i])):
            lst[lst_index] = buckets[i][j]
            lst_index += 1


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, 4, 5, 6, 7, 8]
    bucket_sort(lst, bucket_size=5)
    print(lst)
