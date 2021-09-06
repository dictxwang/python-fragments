# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import cProfile
import functools


def foo():
    sum = 0
    for i in range(100):
        sum += i
    return sum


if __name__ == "__main__":
    # 另一种调试方式
    # python -m cProfile main.py
    cProfile.run("foo()")

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = functools.reduce(lambda x, y: x+y, filter(lambda x: x % 2 == 0, lst))
    print(count)

    count = sum(filter(lambda x: x % 2 == 1, lst))
    print(count)
