#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
基于gensim的doc2vec应用
pip install gensim
'''

import multiprocessing
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import jieba


def first_sample():
    documents = []
    documents.append(TaggedDocument(["刘德华", "四大", "天王"], [1]))
    documents.append(TaggedDocument(["刘德华", "香港", "歌手"], [2]))
    documents.append(TaggedDocument(["张学友", "四大", "天王"], [3]))
    documents.append(TaggedDocument(["张学友", "中国", "歌神"], [4]))
    model = Doc2Vec(documents, min_count=1, window=3, vector_size=100, sample=1e-3,
                    negative=5, workers=multiprocessing.cpu_count())
    model.train(documents, total_examples=model.corpus_count, epochs=10)
    v = model.infer_vector(doc_words=["香港", "张学友", "歌手"], alpha=0.025)
    sims = model.dv.most_similar([v], topn=4)
    print(sims)

    print(model.wv.most_similar("香港"))  # 根据词向量查找相似词语

    # v1 = model.infer_vector(doc_words=["张学友", "香港", "天王"])
    # v2 = model.infer_vector(doc_words=["刘德华", "歌手"])
    #
    # print(model.dv.similarity(["张学友", "中国", "歌神"], ["刘德华", "歌手"]))


def second_sample():
    original = [
        "乌军攻入俄罗斯境内",
        "国民神车为什么卖不动了",
        "智能科技，改变生产生活",
        "薇娅夫妇半年收获两家上市公司",
        "湛江当街杀人案嫌犯称有自首望轻判",
        "全红婵的水花让物理学不存在了"
    ]
    segments_lst = []
    stop_words = load_stop_words()
    for index in range(len(original)):
        # 分词处理
        segments = make_segments(stop_words, original[index])
        segments_lst.append((segments, [index]))

    # 训练模型
    documents = []
    for segments, index in segments_lst:
        documents.append(TaggedDocument(segments, index))
    model = Doc2Vec(documents, min_count=1, window=5, vector_size=100, sample=1e-3,
                    negative=1, workers=multiprocessing.cpu_count())
    model.train(documents, total_examples=model.corpus_count, epochs=10)

    # 相似文本查找
    doc = "薇娅夫妇"
    doc_segments = make_segments(stop_words, doc)
    doc_vector = model.infer_vector(doc_words=doc_segments, alpha=0.1, min_alpha=0.0001)
    sims = model.dv.most_similar([doc_vector], topn=2)
    print(sims)


def load_stop_words():
    result = []
    with open("data/stopwords.txt", encoding="utf8") as fp:
        for line in fp.readlines():
            line = line.strip("\r\n").strip("\n")
            result.append(line)
    return result


def make_segments(stop_words, document):
    '''
    分词
    :param stop_words: 停用词
    :param document: 待分词文本
    :return:
    '''
    segments = jieba.cut(document)
    senti_words = [seg for seg in segments if seg not in stop_words]
    return senti_words


if __name__ == '__main__':
    # first_sample()
    second_sample()
