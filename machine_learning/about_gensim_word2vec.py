#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "wangqiang"

import multiprocessing

'''
基于gensim的word2vec应用
pip install gensim

word2vec的一些知识
1、两种模型和两种训练方法
    模型： 跳字模型（skip-gram）   连续词袋模型（CBOW, Continuous Bag Of Words）
    方法： 负采样（negative sampling）  层序softmax（hierarchical softmax）
2、两种模型的比较
    CBOW模型： 利用上下文或周围的单词来预测中心词，即给定上下文预测中心词
    Skip-Gram模型： 利用中心词来预测上下文，即给定中心词预测上下文
3、余弦相似度：
    向量u和向量v的内积 / (向量u的2-范数 * 向量v的2-范数)
4、词向量生成的方式
    基于统计方法： 共现矩阵、SVD奇异值分解
    基于语言模型： 语言模型生成词向量是通过训练神经网络语言模型NNLM，而词向量是语言模型的副产品
5、word2vec在实现上的特性
    使用了CBOW与Skip-Gram来训练模型并得到词向量，但是没有使用传统的DNN模型（而是采用了优化的方式：如使用霍夫曼树来代替隐藏层和传输层的神经元，建设模型训练的计算量）
'''

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import jieba
import jieba.analyse


def first_sample():
    '''
    语料为列表
    '''
    sentences = [["白猫", "黑猫", "老鼠"], ["哈巴狗", "小黑狗", "耗子"]]
    model = Word2Vec(sentences, min_count=1)
    # 保存模型
    # model.save('data/gensim_word2vec_model_first.model')
    # 返回最相似的词
    print(model.wv.similar_by_word("白猫", topn=2))

    # 继续训练模型
    model.train([["西红柿", "土豆", "苹果"]], total_examples=1, epochs=1)
    # 找到不同类的词
    print(model.wv.doesnt_match(["西红柿", "土豆", "耗子"]))  # 耗子


def second_sample():
    '''
    语料为单个文件
    文件内容格式： 一行一条句子，单词用空格分隔
    '''
    sentences = LineSentence("data/word2vec_second_sample_source.txt", max_sentence_length=1000)
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)
    print(model.wv.similar_by_word("就是", topn=3))


def create_segment_file():
    '''
    创建分词文件
    '''
    seg_file_path = "data/word2vec_third_segments.txt"
    with open("data/word2vec_third_sample_source.txt", encoding="utf8") as fp:
        document = ""
        for line in fp.readlines():
            if line.strip("\r").strip("\r\n") == "":
                continue
            else:
                document += line
        segments = jieba.cut(document)
        result = ' '.join(segments)
        with open(seg_file_path, mode="w", encoding="utf8") as ofp:
            ofp.write(result)
    return seg_file_path


def third_sample():
    '''
    演示基于原始文本建立模型，再到模型使用的完整流程
    '''
    # step1: 基于原始文本，生成分词文件
    seg_fp = create_segment_file()

    # step2: 基于单文件构建模型
    sentences = LineSentence(seg_fp, max_sentence_length=1000)
    model = Word2Vec(sentences, vector_size=200, window=5, min_count=1, workers=multiprocessing.cpu_count())

    # step3: 查找相似的词
    similar_words = model.wv.similar_by_word("人民", topn=10)
    for x in similar_words: print(x)


if __name__ == '__main__':
    # first_sample()
    # second_sample()
    third_sample()
