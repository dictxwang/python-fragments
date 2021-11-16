#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
测试异步方法，需要安装 pytest-asyncio
'''

import asyncio
import pytest
import sys
sys.path.append("..")
import tools


@pytest.mark.asyncio
async def test_async_pop_number():
    assert await tools.async_pop_number() == 10


@pytest.mark.asyncio
async def test_async_add():
    assert await tools.async_add(2, 3) == 5


# if __name__ == '__main__':
#     asyncio.run(test_async_pop_number())
