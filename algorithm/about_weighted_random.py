#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'


'''
加权随机算法
'''

from functools import reduce
import random


class WeightedRandom(object):

    def __init__(self, instances):
        self._instances = instances
        self._total_weight = WeightedRandom._sum_weight(self._instances)

    @staticmethod
    def _sum_weight(instances):
        return reduce(lambda x, y: x+y, map(lambda inst: inst[1], instances))

    def random(self):
        if self._total_weight <= 0:
            return None  # 所有的项权重都为0

        rnd_weight = random.randint(0, int(self._total_weight * 0.9))
        random.shuffle(self._instances)  # 每次需要打乱顺序，避免随机出的元素向队头集中
        while True:
            for inst in self._instances:
                if inst[1] <= 0:
                    continue
                rnd_weight -= inst[1]
                if rnd_weight <= 0:
                    return inst[0]


def random_result_check(wr, times=10000):
    result = {}
    for _ in range(times):
        inst = wr.random()
        times = result.get(inst, 0) + 1
        result[inst] = times
    print(result)


if __name__ == '__main__':

    instances = [
        ("A", 1),
        ("B", 2),
        ("C", 6),
        ("D", 1)
    ]

    wr = WeightedRandom(instances)
    print(wr.random())

    random_result_check(wr, times=10000)
