#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import pytest
import sys
sys.path.append("..")
import tools

__version = "v1.0"


@pytest.mark.skip(reason="i know fail")
def test_is_person_adult_skip():
    '''
    对于暂时不用的用例，或明确不能通过的用例，可以跳过
    '''
    assert tools.is_person_adult(5)


@pytest.mark.skipif(__version == "v1.0", reason="not need in this version")
def test_is_person_adult_skip_if():
    '''
    按条件跳过
    '''
    assert tools.is_person_adult(10)


@pytest.mark.xfail(reason="not a positive for age")
def test_is_person_adult_xfail():
    '''
    跳过异常，在统计计数时不计为失败，而是计为预期失败xfailed
    '''
    assert tools.is_person_adult(10)
