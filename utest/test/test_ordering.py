#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
测试执行顺序，需要安装 pytest-ordering
'''

import time
import pytest


@pytest.mark.run(order=2)
def test_order_01():
    time.sleep(1)
    now = time.time()
    print(f"exec test_order_01 at {now}")


@pytest.mark.run(order=1)
def test_order_02():
    time.sleep(1)
    now = time.time()
    print(f"exec test_order_02 at {now}")
