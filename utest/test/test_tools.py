#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import pytest
import sys
sys.path.append("..")
import tools


def test_add():
    assert 3 == tools.add(1, 2)


def test_double_add():
    assert 6 == tools.double_add(1, 2)


def test_is_person_adult():
    assert not tools.is_person_adult(10)
    assert tools.is_person_adult(18)
    assert tools.is_person_adult(20)


def test_is_person_adult_exception():
    '''
    测试抛出异常的情况
    '''
    with pytest.raises(Exception) as exp:
        tools.is_person_adult(-1)
        assert exp.message == "not positive age"
