#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import math
import jieba

'''
BM25是搜索引擎概率检索模型的一种实现算法。
'''

class BM25(object):

    def __init__(self, documents):
        '''
        初始化
        :param documents: 文档集合，每个文档实际是分词后的词序列
        '''
        self.count = len(documents)
        self.avgdl = sum([len(doc)+0.0 for doc in documents]) / self.count
        self.documents = documents
        self.f = []  # 列表的每一个元素是一个dict，dict存储着一个文档中每个词的出现次数
        self.df = {}  # 存储每个词及出现了该词的文档数量
        self.idf = {}  # 存储每个词的idf值
        self.k1 = 1.5
        self.b = 0.75
        self.init()

    def init(self):
        for doc in self.documents:
            temp = {}
            for word in doc:
                temp[word] = temp.get(word, 0) + 1
            self.f.append(temp)
            for k in temp.keys():
                self.df[k] = self.df.get(k, 0) + 1
        for k, v in self.df.items():
            self.idf[k] = math.log(self.count - v + 0.5) - math.log(v + 0.5)

    def sim(self, query, index):
        '''
        计算query和指定文档的bm25值
        :param query: 分词后的词列表
        :param index: 文档的序号
        :return:
        '''
        score = 0
        for word in query:
            if word not in self.f[index]:
                continue
            doc_len = len(self.documents[index])
            score += (self.idf[word] * self.f[index][word] * (self.k1 + 1)
                      / (self.f[index][word] + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)))
        return score

    def simall(self, query):
        '''
        计算query和所有文档的相关性
        :param query:
        :return:
        '''
        scores = []
        for index in range(self.count):
            score = self.sim(query, index)
            scores.append(score)
        return scores


class SearchEngine(object):

    def __init__(self, stop_words, documents):
        '''
        初始化
        :param stop_words: 停用词列表
        :param documents: 这里是原始文档文本
        '''
        self.stop_words = stop_words
        self.documents = documents
        self.bm25 = None
        self.init()

    def init(self):
        doc_words = []
        for doc in self.documents:
            doc_words.append(self.cut_word(doc))
        self.bm25 = BM25(doc_words)

    def cut_word(self, document):
        words = jieba.cut(document)
        result = []
        for w in words:
            if w not in self.stop_words:
                result.append(w)
        return result

    def search_top_k(self, query, k=3):
        top = list(enumerate(self.bm25.simall(self.cut_word(query))))
        top_sorted = sorted(top, key=lambda x: x[1], reverse=True)
        top_k = top_sorted[:k]
        result = []
        for index, score in top_k:
            result.append((index, self.documents[index], score))  # (doc_id, doc_content, score)
        return result


def load_stop_words():
    fp = open("data/stopwords.txt", mode="r", encoding="utf8")
    words = []
    for line in fp.readlines():
        line = line.strip("\r\n").strip("\n")
        words.append(line)
    fp.close()
    return words


if __name__ == '__main__':

    documents = [
        "自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。",
        "它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。",
        "自然语言处理是一门融语言学、计算机科学、数学于一体的科学。",
        "因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，",
        "所以它与语言学的研究有着密切的联系，但又有重要的区别。",
        "自然语言处理并不是一般地研究自然语言，"
    ]

    stop_words = load_stop_words()

    se = SearchEngine(stop_words, documents)
    r = se.search_top_k("计算机语言处理", 3)
    print(r)
