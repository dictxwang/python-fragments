#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "wangqiang"

'''
dbscan适用于对任意形状的稠密数据集进行聚类
    此算法类似病毒传播一样，从一个点触发，向一定范围内相邻点不断扩散，直到扩散的新节点数量小于阈值
'''

import numpy as np
import matplotlib.pyplot as pyplot
import time
import copy


def find_neighbor(j, x, eps):
    nodes = set()
    for i in range(x.shape[0]):
        distance = np.sqrt(np.sum(np.square(x[j] - x[i])))
        if distance < eps:
            nodes.add(i)
    return set(nodes)


