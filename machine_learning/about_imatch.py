#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import hashlib
import jieba
import jieba.analyse

'''
I-Match算法常用于搜索领域的网页去重
算法的基本思路是抽取内容中的主要特征，计算Hash值，通过判断Hash值是否相同来识别网页是否重复
'''


class IMatch(object):

    def __init__(self, k):
        self._k = k  # 设置获取token的数量

    def get_tokens(self, content):
        segments = jieba.cut(content)
        topn = self._k + 2  # 获取两倍数量的token，再去掉排名靠前的几个
        keywords = jieba.analyse.extract_tags("|".join(segments), topK=topn, withWeight=True, allowPOS=())
        # print(keywords)
        k = self._k
        if len(keywords) <= self._k:
            k = len(keywords)

        result = []
        # 选取中间较均衡的特征
        for i in range(1, min(k + 1, len(keywords))):
            result.append(keywords[i][0])
        sorted(result)
        return result

    def get_hash(self, tokens):
        val = "".join(tokens)
        return hashlib.sha1(val.encode()).hexdigest()

    def is_similarity(self, s1, s2):
        tokens1 = self.get_tokens(s1)
        tokens2 = self.get_tokens(s2)
        hash1 = self.get_hash(tokens1)
        hash2 = self.get_hash(tokens2)
        return 1 if hash1 == hash2 else 0


if __name__ == '__main__':

    s1 = "体育频道：中国足球队在米卢的率领下首次获得世界杯决赛阶段的比赛资格，新浪体育播报 。"
    s2 = "体育频道：米卢率领中国足球队员首次杀入世界杯决赛阶段，搜狐体育播报。"

    imatch = IMatch(4)
    print(imatch.get_tokens(s1))  # ['中国足球队', '播报', '决赛', '世界杯']
    print(imatch.get_tokens(s2))  # ['中国足球队', '播报', '决赛', '世界杯']
    print(imatch.is_similarity(s1, s2))  # 1
