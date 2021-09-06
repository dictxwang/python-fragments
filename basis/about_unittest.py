# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import unittest


class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    print(unittest.main())
