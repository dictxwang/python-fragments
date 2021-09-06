# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import operator
import collections


if __name__ == "__main__":

    c01 = ["113", "022", "abc"]
    c01.sort()
    print(c01)

    # 倒序
    c01.sort(reverse=True)
    print(c01)

    # 按元素的第2个字符排序
    c01.sort(key=lambda x: x[1])
    print(c01)

    c02 = ["154", "xyz", "810"]
    c02 = sorted(c02)
    print(c02)
    # 按元素的第3个字符排序
    c02 = sorted(c02, key=lambda x: x[2])
    print(c02)

    c03 = [["zhao", 90], ["qian", 86], ["sun", 88]]
    # 按照子序列的第2个元素排序
    c03 = sorted(c03, key=operator.itemgetter(1))
    print(c03)

    c04 = [["zhou", 90, "A"], ["wu", 95, "A"], ["zheng", 86, "B"]]
    # 按照子序列的第3个元素和第2个元素排序
    c04 = sorted(c04, key=operator.itemgetter(2, 1))
    print(c04)
    
    c05 = [
        {"name": "zhou", "score": 90, "class": "A"},
        {"name": "wu", "score": 95, "class": "A"},
        {"name": "zheng", "score": 86, "class": "B"}
    ]
    # 按照指定的字段key排序
    c05 = sorted(c05, key=operator.itemgetter("class", "score"))
    print(c05)

    c06 = {
        "wang": 80,
        "liu": 90,
        "li": 100,
        "chen": 87,
        "zheng": 98
    }
    # 按照value排序，得到元组序列 [('wang', 80), ('chen', 87), ('liu', 90), ('zheng', 98), ('li', 100)]
    c06 = sorted(c06.items(), key=operator.itemgetter(1))
    print(c06)

    # Counter 进行计数统计
    c10 = [1, 2, 4, 2, 3, 'a', 'b', 'd', 'b', 3]
    print(collections.Counter(c10))
    print(collections.Counter(c10).get('a'))
