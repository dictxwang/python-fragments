#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
测试 @pytest.mark.parametrize 的使用
'''

import pytest


@pytest.mark.parametrize("word",
                         ['12345678',
                          'abcdefghijk'])
def test_words_len(word):
    '''
    这里列表中的多个参数将分别当做单独的用例测试
    :param word:  装饰器中第一个参数需要和当前方法同名
    '''
    assert len(word) >= 8


@pytest.mark.parametrize("first, second",
                         [pytest.param(1, 2, id="add<1, 2>"),
                          pytest.param(2, 0, id="add<2, 0>")])
def test_multi_param(first, second):
    '''
    多个参数时，各参数通过参数名对应，而和顺序无关
    pytest.param 中的id被用来区分不同的单测
    '''
    assert first + second > 0


@pytest.mark.parametrize("second, first",
                         [(1, 2),
                          (3, 5)])
def test_multi_param_pos_change(first, second):
    '''
    测试多个参数顺序变化，验证参数通过名字对应
    '''
    assert first - second > 0


@pytest.mark.parametrize("expression, result",
                         [(pytest.param("1+2", 3, id="1+2=3")),
                          (pytest.param("5-3", 2, id="5-3=2"))])
def test_multi_param_exp(expression, result):
    '''
    测试表达式的应用
    '''
    assert eval(expression) == result
