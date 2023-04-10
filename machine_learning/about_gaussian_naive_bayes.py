#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
高斯朴素贝叶斯分类器（Gaussian Naive Bayes Classifier）
适用于特征数据是连续值的数据集（注意：如果特征数据是离散值通常符合多项式分布，如果特征数据是布尔型离散值通常符合伯努利分布）
pip install pandas
pip install numpy
'''

import pandas as pd
import numpy as np


def load_and_parse_train_test_data():
    '''
    加载数据，并分离训练数据集（特征值、标签）和测试数据集
    '''
    data = pd.read_csv(r"data/pima-indians-diabetes.data.csv", header=None, names=[
        "怀孕次数", "口服葡萄糖耐量实验中血浆葡萄糖浓度", "舒张压（mm Hg）", "三头肌组织褶厚度（mm）", "2小时血清胰岛素（μU/ml）",
        "体重指数（km/(身高（m）) ^ 2）", "糖尿病系统功能", "年龄（岁）", "是否患有糖尿病"
    ])

    # 将属性值为0的值转换成NaN，并于后续的移除处理
    data.iloc[:, 0:8] = data.iloc[:, 0:8].applymap(lambda x : np.NaN if x == 0 else x)
    data = data.dropna(how="any", axis=0)

    # 随机选取80%的样本作为训练样本
    data_train = data.sample(frac=0.8, random_state=4, axis=0)
    # 将剩下的数据作为测试样本
    data_test_idx = [i for i in data.index.values if i not in data_train.index.values]
    data_test = data.loc[data_test_idx, :]

    # 分别提前训练数据和测试数据的 特征和标签
    train_features = data_train.iloc[:, :-1]
    train_labels = data_train.iloc[:, -1]

    test_features = data_test.iloc[:, :-1]
    test_labels = data_test.iloc[:, -1]

    return (train_features, train_labels), (test_features, test_labels)


class Gaussian_Naive_Bayes:

    def __init__(self):
        # 样本总数
        self._num_of_samples = None
        # 分类总数
        self._num_of_labels = None
        self._label_names = []
        # 先验概率
        self._priori_probability = []
        # 各类别下，各维度特征的平均值
        self._feature_mean_average = []
        # 各类别下，各维度特征的方差
        self._feature_variance = []

    def separate_by_label(self, features, labels):
        self._num_of_samples = len(labels)
        labels = labels.reshape(labels.shape[0], 1)
        # 将特征和分类水平叠加
        data = np.hstack((features, labels))

        # 提取个类别数据，字典的键为类别名，值为对应的分类数据
        data_by_labels = {}
        for i in range(len(data[:, -1])):
            if i in data[:, -1]:
                data_by_labels[i] = data[data[:, -1] == i]

        self._label_names = list(data_by_labels.keys())
        self._num_of_labels = len(data_by_labels.keys())
        return data_by_labels

    def cal_priori_probability(self, y_by_label):
        '''
        计算先验概率（使用拉普拉斯平滑）
        '''
        # 计算公式：（当前类别下的样本数+1）/（总样本数+类别总数）
        return (len(y_by_label) + 1) / (self._num_of_samples + self._num_of_labels)

    @staticmethod
    def cal_feature_mean_average(x_by_labels):
        '''
        计算各类别特征各维度的平均值
        '''
        feature_mean = []
        for i in range(x_by_labels.shape[1]):
            feature_mean.append(np.mean(x_by_labels[:, i]))
        return feature_mean

    @staticmethod
    def cal_feature_variance(x_by_labels):
        '''
        计算各类别特征各维度的方差
        '''
        feature_variance = []
        for i in range(x_by_labels.shape[1]):
            feature_variance.append(np.var(x_by_labels[:, i]))
        return feature_variance

    @staticmethod
    def cal_gaussian_probability(feature_new, mean, var):
        '''
        计算训练集特征在各类别下的条件概率
        '''
        # 输入新样本的特征，训练集特征的平均值和方差，输出新样本的特征在相应训练集中的分布概率
        # 计算公式: (np.exp(-(feature_new - mean)**2 / (2 * var))) * (1 / np.sqrt(2 * np.pi * var))
        gaussian_probability = []
        for a, b, c in zip(feature_new, mean, var):
            formula1 = np.exp(-(a - b) ** 2 / (2 * c))
            formula2 = 1 / np.sqrt(2 * np.pi * c)
            gaussian_probability.append(formula1 * formula2)

        return gaussian_probability

    def fit(self, features, labels):
        '''
        训练数据：输入训练集特征和目标，输出目标的先验概率、特征的平均值和方差
        '''
        features, labels = np.asarray(features, np.float32), np.asarray(labels, np.float32)

        data_by_labels = self.separate_by_label(features, labels)
        # 计算各类别数据的目标先验概率，特征平均值和方差
        for data in data_by_labels.values():
            x_by_labels = data[:, :-1]
            y_by_labels = data[:, -1]
            self._priori_probability.append(self.cal_priori_probability(y_by_labels))
            self._feature_mean_average.append(Gaussian_Naive_Bayes.cal_feature_mean_average(x_by_labels))
            self._feature_variance.append(Gaussian_Naive_Bayes.cal_feature_variance(x_by_labels))

        return self._priori_probability, self._feature_mean_average, self._feature_variance

    def predict(self, feature_new):
        '''
        数据分类预测
        '''
        feature_new = np.asarray(feature_new, np.float32)
        # 初始化极大后验概率
        posteriori_prob = []

        for prob, mean, var in zip(self._priori_probability, self._feature_mean_average, self._feature_variance):
            gaussian = Gaussian_Naive_Bayes.cal_gaussian_probability(feature_new, mean, var)
            posteriori_prob.append(np.log(prob) + sum(np.log(gaussian)))

        idx = np.argmax(posteriori_prob)
        return self._label_names[idx]


if __name__ == '__main__':

    train_dataset, test_dataset = load_and_parse_train_test_data()
    gnb = Gaussian_Naive_Bayes()
    gnb.fit(train_dataset[0], train_dataset[1])

    acc = 0
    TP = 0
    FP = 0
    FN = 0
    for i in range(len(test_dataset[0])):
        predict = gnb.predict(test_dataset[0].iloc[i, :])
        target = np.array(test_dataset[1])[i]

        if predict == 1 and target == 1:
            TP += 1
        if predict == 0 and target == 1:
            FP += 1
        if predict == target:
            acc += 1
        if predict == 1 and target == 0:
            FN += 1
    print("准确率：", acc/len(test_dataset[0]))
    print("查准率：", TP / (TP + FP))
    print("查全率：", TP / (TP + FN))
    print("F1:", 2 * TP / (2 * TP + FP + FN))
