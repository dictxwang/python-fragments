# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
字符串查找算法（KMP算法：Knuth-Morris-Pratt）
'''


def gen_next(pattern):
    """
    计算next表
    通过PMT(Partial Match Table)『最长公共前后缀』推到
    :param pattern: 待查找串
    :return:
    """
    lst = list(pattern)
    # 将第一位设置为-1，方便判断当前位置是否是搜索词的起始位置
    # next表实际上是把PMT表整体向后移动一位，第一位用-1填充
    nxt = [-1] * len(lst)
    i = 0
    j = -1
    while True:
        if i >= len(lst) - 1:
            break
        if j == -1 or lst[i] == lst[j]:
            i += 1
            j += 1
            nxt[i] = j
        else:
            # 这里相当于是回到起始位置重新开始匹配
            # j = nxt[j]
            j = -1
    return nxt


def kmp_search(target, pattern):
    target = list(target)
    pattern = list(pattern)
    i = 0
    j = 0
    nxt = gen_next(pattern)
    result = []
    while True:
        if i >= len(target):
            break
        if j == -1 or target[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = nxt[j]

        if j == len(pattern):
            result.append(i - j)
            j = 0
    return result


if __name__ == '__main__':

    target = "AAABCEABDABCFABCABCEABCABZ"
    pattern = "ABCAB"
    # 先打印一下next表
    nxt = gen_next(pattern)
    print(nxt)

    print(kmp_search(target, pattern))
