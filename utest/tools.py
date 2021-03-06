#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import asyncio


def add(first, second):
    return first + second


def double_add(first, second):
    return first * 2 + second * 2


def is_person_adult(age=0):
    if age >= 18:
        return True
    elif age >= 0:
        return False
    else:
        raise Exception("not positive age")


def multi(first, second):
    '''
    空方法，等待被mock
    '''
    pass


async def async_pop_number():
    return 10


async def async_add(first, second):
    return first + second
