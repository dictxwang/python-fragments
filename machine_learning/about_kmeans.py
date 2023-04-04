#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "wangqiang"

'''
k-means适用于对凸数据集的分类
'''

import numpy as np
from matplotlib import pyplot


class K_Means(object):

    def __init__(self, k=2, tolerance=0.0001, max_iter=300):
        '''
        k：分组数， tolerance：中心点误差，max_iter：最大迭代次数
        '''
        self._k = k
        self._tolerance = tolerance
        self._max_iter = max_iter
        self._centers = {}
        self._clf = {}

    def fit(self, data_set):

        # 先随机设置中心点（centroids质心）（这里可以选择用随机算法选取）
        for i in range(self._k):
            self._centers[i] = data_set[i]

        # 进行多轮计算，直到中心点误差在允许的范围内
        for i in range(self._max_iter):
            for j in range(self._k):
                self._clf[j] = []
            # print("质点：", self._centers)
            for feature in data_set:
                distances = []
                for center in self._centers:
                    # 计算欧拉距离（euclidean distance）
                    # sqrt((x1-x2)**2 + (y1-y2)**2 + ... + (n1-n2)**2)
                    # np.sqrt(np.sum((feature - self._centers[center]) ** 2))
                    # 这里用求二范数的方式，等价于计算欧拉距离
                    distances.append(np.linalg.norm(feature - self._centers[center]))
                classification = distances.index(min(distances))
                self._clf[classification].append(feature)

            # print("分组情况：", self._centers)
            prev_centers = dict(self._centers)
            for c in self._clf:
                self._centers[c] = np.average(self._clf[c], axis=0)

            # 判断中心点是否存在误差
            optimized = True
            for center in self._centers:
                org_centers = prev_centers[center]
                cur_centers = self._centers[center]
                if np.sum((cur_centers - org_centers) / org_centers * 100.0) > self._tolerance:
                    optimized = False
            if optimized:
                break

    def predict(self, p_data):
        '''
        判断数据在哪个分类
        '''
        distances = [np.linalg.norm(p_data - self._centers[center]) for center in self._centers]
        # 选择距离最近的中心点所在分类
        index = distances.index(min(distances))
        return index


if __name__ == '__main__':
    x = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11], [6, 10]])
    k_means = K_Means(k=2)
    k_means.fit(x)
    colors = ["r", "b", "g", "y"]
    # print(k_means._centers)

    # 绘制中心点
    for center in k_means._centers:
        pyplot.scatter(k_means._centers[center][0], k_means._centers[center][1], marker="*", s=100)

    # 绘制分组
    for cat in k_means._clf:
        for point in k_means._clf[cat]:
            pyplot.scatter(point[0], point[1], c=colors[cat])

    predict = [[2, 1], [6, 8], [10, 10]]
    for feature in predict:
        cat = k_means.predict(feature)
        pyplot.scatter(feature[0], feature[1], c=colors[cat], marker="x")

    pyplot.show()
