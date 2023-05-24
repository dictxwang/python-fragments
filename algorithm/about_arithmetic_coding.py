#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
算术编码
    核心思想：依据字符出现概率，将整段文本编码成一个浮点数
    优势：对比哈夫曼编码，使用的字节数更少，更接近香农信息熵
'''

import random


def interval_probability(original, interval):
    '''
    重新计算区间概率（依据最初字符概率，在概率区间范围重新计算每个字符的占有的概率区间）
    :param original: 最初的字符概率
    :param interval: 概率区间
    :return:
    '''
    mt = []
    for c, i in original.items():
        mt.append((c, i[1] - i[0]))
    mt = sorted(mt, key=lambda x: x[1], reverse=True)
    post_probability = interval[0]
    result = {}
    for t in mt:
        right = t[1] * (interval[1] - interval[0])
        result[t[0]] = (post_probability, right + post_probability)  # 概率区间左闭右开
        post_probability += right
    return result


def arithmetic_coding(text):

    def char_occurrence_probability(text):
        '''
        依据原始文本，计算字符概率
        :param text:
        :return: {char:probability}
        '''
        m = {}
        for c in text:
            times = m.get(c, 0) + 1
            m[c] = times

        mt = []
        for c, t in m.items():
            mt.append((c, t))
        mt = sorted(mt, key=lambda x: x[1], reverse=True)

        total_times = len(text)
        post_probability = 0
        result = {}
        for t in mt:
            p = t[1] / total_times
            result[t[0]] = (post_probability, p + post_probability)  # 概率区间左闭右开
            post_probability += p
        return result


    char_original_probability = char_occurrence_probability(text)
    current_interval = None
    coding_result = None
    for index in range(len(text)):
        if current_interval is None:
            current_interval = char_original_probability[text[index]]
        else:
            probabilities = interval_probability(char_original_probability, current_interval)
            current_interval = probabilities[text[index]]
        if index == len(text) - 1:
            # 编码到最后一个字符，返回结果
            coding_result = random.uniform(current_interval[0], current_interval[1])
            break
    return coding_result, char_original_probability


def arithmetic_decoding(coding, char_probability, text_length):
    '''
    算术解码
    :param coding: 编码
    :param char_probability: 字符概率区间
    :param text_length: 原始文本长度
    :return:
    '''
    def find_char(coding, interval):
        for c, p in interval.items():
            if p[0] <= coding < p[1]:
                return c, p
        return None, None

    result = ""
    current_interval = char_probability
    while True:
        c, p = find_char(coding, current_interval)
        if c is None:
            break
        else:
            result += c
            current_interval = interval_probability(char_probability, current_interval[c])
        if len(result) == text_length:
            break
    return result


if __name__ == '__main__':
    # text = "AABABCABAB"
    text = "我爱你我的祖国"
    ac, cp = arithmetic_coding(text)
    print("arithmetic coding: ", ac)
    print("char probability: ", cp)

    dc = arithmetic_decoding(ac, cp, len(text))  # 因为精度问题，解码可能会出现问题，需要优化
    print("arithmetic decoding: ", dc)
