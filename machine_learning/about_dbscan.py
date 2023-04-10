#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "wangqiang"

'''
DBSCAN Density-Based Spatial Clustering of Applications with Noise
(基于密度的噪声应用空间聚类)

dbscan适用于对任意形状的稠密数据集进行聚类
    从一些核心点出发，向一定范围内相邻点不断扩散，直到扩散的新节点数量小于阈值

pip install scikit-learn
'''

import random
import numpy as np
import matplotlib.pyplot as pyplot
import time
import copy
from sklearn import datasets


class Dbscan(object):

    def __init__(self, eps, min_samples):
        self._eps = eps  # 能聚合成一组的最大半径
        self._min_samples = min_samples  # 能构成一组的最小样本数

    def _find_neighbor(self, j, x):
        nodes = set()
        for i in range(x.shape[0]):
            distance = np.sqrt(np.sum(np.square(x[j] - x[i])))
            if distance < self._eps:
                nodes.add(i)
        return set(nodes)

    def fit(self, data_set):
        k = -1
        neighbor_list = []  # 保存每个数据的邻域
        core_list = []  # 核心点集合
        unvisited = set([x for x in range(len(data_set))])  # 初始时将所有节点标记为未访问
        cluster = [-1 for _ in range(len(data_set))]  # 聚类集合

        for i in range(len(data_set)):
            neighbor_list.append(self._find_neighbor(i, data_set))
            if len(neighbor_list[-1]) >= self._min_samples:
                core_list.append(i)  # 邻域数量大于阈值，加入到核心点集合
        core_list = set(core_list)

        while len(core_list) > 0:
            unvisited_old = copy.deepcopy(unvisited)
            core = random.choice(list(core_list))  # 随机选取一个核心点
            k = k + 1
            print("k:", k)
            queue = list()
            queue.append(core)
            unvisited.remove(core)
            while len(queue) > 0:
                q = queue.pop(0)
                if len(neighbor_list[q]) >= self._min_samples:
                    neighbor_unvisited = neighbor_list[q] & unvisited  # 找到邻域中未访问的节点
                    neighbor_unvisited_list = list(neighbor_unvisited)
                    for i in range(len(neighbor_unvisited)):
                        queue.append(neighbor_unvisited_list[i])  # 将未访问的领域节点加入队列，继续访问领域节点
                        unvisited = unvisited - neighbor_unvisited

            # 记录已经访问的节点，及其所属的分类
            ck = unvisited_old - unvisited
            ck_list = list(ck)
            for i in range(len(ck)):
                cluster[ck_list[i]] = k
            core_list = core_list - ck

        return cluster


if __name__ == '__main__':

    # 生成环形，factor是内外圈的尺度因子，noise是噪点比例
    ds1, _ = datasets.make_circles(n_samples=1000, factor=.6, noise=.02)
    ds2, _ = datasets.make_blobs(n_samples=400, n_features=2, centers=[[1.2, 1.2]], cluster_std=[[.1]], random_state=9)
    ds_all = np.concatenate((ds1, ds2))
    eps = 0.08
    min_samples = 10
    begin = time.time()
    dbscan = Dbscan(eps, min_samples)
    cluster = dbscan.fit(ds_all)
    end = time.time()

    pyplot.figure()
    pyplot.scatter(ds_all[:, 0], ds_all[:, 1], c=cluster)
    pyplot.show()
