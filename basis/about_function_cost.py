# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import time


def direct_func(a, b):
    return a + b


def add(a, b):
    return a + b


def call_func(a, b):
    return add(a, b)


if __name__ == "__main__":

    st1 = int(time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID) * 1000000000)
    for i in range(10000):
        direct_func(1, 2)
    cost1 = int(time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID) * 1000000000) - st1

    st2 = int(time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID) * 1000000000)
    for i in range(10000):
        call_func(1, 2)
    cost2 = int(time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID) * 1000000000) - st2

    print(cost1, cost2, cost2 - cost1, (cost2 - cost1) / 100000)
