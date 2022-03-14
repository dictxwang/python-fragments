# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
字符串查找的bf（brute force）暴力算法
'''


def bf_search(target, pattern):

    result = []
    if not target or not pattern:
        return result

    target_from = 0
    while True:
        if target_from + len(pattern) > len(target):
            break
        matched = True
        for pattern_index in range(0, len(pattern)):
            if pattern[pattern_index] != target[target_from + pattern_index]:
                # 遍历子串字符过程中，发生不匹配直接跳出
                matched = False
                break
        if matched and pattern_index == len(pattern) - 1:
            result.append(target_from)
        # 每次向前移动一位
        target_from += 1
    return result


if __name__ == '__main__':
    target = "AECCCCCCCDFGHECDFIXYECW"
    child = "EC"
    result = bf_search(target, child)
    print(result)
