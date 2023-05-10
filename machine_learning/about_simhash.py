#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import jieba
import jieba.analyse
import numpy as np

'''
SimHash常用于搜索引擎中的网页去重
SimHash是局部敏感哈希的一种，其基本思想是通过降维再计算汉明距离的方式计算内容的相似度。
SimHash的流程包括：分词、hash、加权、合并、降维
'''


class SimHash(object):

    def sim_hash(self, content):
        segments = jieba.cut(content)
        # jieba.analyse.set_stop_words("stopword.txt")  # 设置停用词
        # step1: 分词，通过jieba，基于TF-IDF提取关键词
        # jieba的tfidf会有对关键词排序
        keywords = jieba.analyse.extract_tags("|".join(segments), topK=20, withWeight=True, allowPOS=())

        # step2: hash+加权
        key_list = []
        for feature, weight in keywords:
            weight = int(weight * 20)
            feature = self.string_hash(feature)
            temp = []
            for f in feature:
                if f == "1":
                    temp.append(weight)
                else:
                    temp.append(-weight)
            key_list.append(temp)

        if len(key_list) == 0:
            return "00"

        # step3: 合并，将所有关键词的hash权重合并
        total_list = np.sum(np.array(key_list), axis=0)
        simhash = ""
        for i in total_list:
            if i > 0:
                simhash += "1"
            else:
                simhash += "0"
        return simhash

    def string_hash(self, source):
        '''
        自定义的hash算法
        因为自带的hash算法不稳定，会造成汉明计算异常
        :param source:
        :return:
        '''
        if source == "":
            return "0"
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            x = bin(x).replace("0b", "").zfill(64)[-64:]
            return str(x)

    def hamming_distance(self, sh1, sh2):
        distance = 0
        for index, char in enumerate(sh1):
            if char == sh2[index]:
                continue
            else:
                distance += 1
        return distance


if __name__ == '__main__':
    simhash = SimHash()
    sh1 = simhash.sim_hash("唐李白 床前明月光，疑似地上霜。举头望明月，低头思故乡。")
    sh2 = simhash.sim_hash("李白·唐 举头望明月，低头思故乡。床前明月光，疑似地上霜。")

    # 计算汉明距离
    distance = simhash.hamming_distance(sh1, sh2)
    print(distance)  # 0
