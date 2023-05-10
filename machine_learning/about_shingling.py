#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'


'''
Shingling算法也被称作k-shingle算法，常用于搜索引擎中网页去重
算法的核心是计算两个字符串的jaccard相似度，计算公式可简单描述为：
sim(A, B) = A∩B/A∪B
'''


class Shingling(object):

    def __init__(self, k):
        self._k = k

    def cut_shingle(self, s):
        '''
        计算传入文本内容的shingle
        :param content:
        :return:
        '''
        if s == "" or self._k < 1:
            return []
        if self._k >= len(s):
            return [s]
        result = set()
        for i in range(0, len(s) - self._k):
            sh = s[i: i+self._k]
            result.add(sh)
        return list(result)

    def get_union(self, sh1, sh2):
        '''
        求并集
        '''
        result = set()
        for sh in sh1:
            result.add(sh)
        for sh in sh2:
            result.add(sh)
        return list(result)

    def find_intersection(self, sh1, sh2):
        '''
        求交集
        :return:
        '''
        result = set()
        for sh in sh1:
            if sh in sh2:
                result.add(sh)
        return list(result)

    def jaccard_similarity(self, s1, s2):
        '''
        计算jaccard相似度
        '''
        sh1 = self.cut_shingle(s1)
        sh2 = self.cut_shingle(s2)
        union = self.get_union(sh1, sh2)
        intersection = self.find_intersection(sh1, sh2)
        return len(intersection) / len(union)


if __name__ == '__main__':
    s1 = "我爱北京天安门，天安门上太阳升"
    s2 = "我喜爱北京的天安门，天安门上时常太阳升"

    shingling = Shingling(3)
    similarity = shingling.jaccard_similarity(s1, s2)  # 数值越大，相似度越高
    print(similarity)
