#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "wangqiang"

'''
dbscan适用于对任意形状的稠密数据集进行聚类
    此算法类似病毒传播一样，从一个点触发，向一定范围内相邻点不断扩散，直到扩散的新节点数量小于阈值
'''

import random
import numpy as np
import matplotlib.pyplot as pyplot
import time
import copy
from sklearn import datasets


class Dbscan(object):

    def __init__(self, eps, min_samples):
        self._eps = eps  # 成为邻居的最大半径
        self._min_samples = min_samples  # 构成一组的最小样本数

    def _find_neighbor(self, j, x):
        nodes = set()
        for i in range(x.shape[0]):
            distance = np.sqrt(np.sum(np.square(x[j] - x[i])))
            if distance < self._eps:
                nodes.add(i)
        return set(nodes)

    def fit(self, data_set):
        k = -1
        neighbor_list = []  # 保持每个数据的邻域
        omega_list = []  # 核心对象集合
        gama = set([x for x in range(len(data_set))])  # 初始时将所有节点标记为未访问
        cluster = [-1 for _ in range(len(data_set))]  # 聚类

        for i in range(len(data_set)):
            neighbor_list.append(self._find_neighbor(i, data_set))
            if len(neighbor_list[-1]) >= self._min_samples:
                omega_list.append(i)  # 邻域数量大于阈值，加入到核心对象集合
        omega_list = set(omega_list)

        while len(omega_list) > 0:
            gama_old = copy.deepcopy(gama)
            j = random.choice(list(omega_list))  # 随机选取一个核心对象
            k = k + 1
            queue = list()
            queue.append(j)
            gama.remove(j)
            while len(queue) > 0:
                q = queue[0]
                queue.remove(q)
                if len(neighbor_list[q]) >= self._min_samples:
                    delta = neighbor_list[q] & gama
                    delta_list = list(delta)
                    for i in range(len(delta)):
                        queue.append(delta_list[i])
                        gama = gama - delta

            ck = gama_old - gama
            ck_list = list(ck)
            for i in range(len(ck)):
                cluster[ck_list[i]] = k
            omega_list = omega_list - ck

        return cluster


if __name__ == '__main__':

    X1, y1 = datasets.make_circles(n_samples=2000, factor=.6, noise=.02)
    X2, y2 = datasets.make_blobs(n_samples=400, n_features=2, centers=[[1.2, 1.2]], cluster_std=[[.1]], random_state=9)
    X = np.concatenate((X1, X2))
    eps = 0.08
    min_samples = 10
    begin = time.time()
    dbscan = Dbscan(eps, min_samples)
    cluster = dbscan.fit(X)
    end = time.time()
    pyplot.figure()
    pyplot.scatter(X[:, 0], X[:, 1], c=cluster)
    pyplot.show()
