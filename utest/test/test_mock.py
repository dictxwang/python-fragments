#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import pytest
from unittest import mock
import sys

sys.path.append("..")
import tools


def test_multi_001():
    tools.multi = mock.Mock(return_value=9)
    assert tools.multi(3, 3) == 9


def test_multi_002():
    # side_effect的值将覆盖return_value的值
    tools.multi = mock.Mock(return_value=9, side_effect=[1, 4, 16])
    assert tools.multi(1, 1) == 1
    assert tools.multi(2, 2) == 4
    assert tools.multi(2, 8) == 16
