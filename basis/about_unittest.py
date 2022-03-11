# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import unittest

"""
更多单元测试参见 utest目录
"""


class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    print(unittest.main())
