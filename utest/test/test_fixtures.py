#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'


import pytest


def setup_module():
    print("\nsetup module...")


def teardown_module():
    print("\nteardown module...")


class TestPytest(object):

    @classmethod
    def setup_class(cls):
        print("\nsetup class...")

    @classmethod
    def teardown_class(cls):
        print("\nteardown class...")

    def setup_method(self, method):
        print("\nsetup method...")

    def teardown_method(self, method):
        print("\nteardown method...")

    def test_add(self):
        print("\nexec test_add")
        assert 1 + 2 == 3

    @pytest.fixture(scope="function")
    def get_message(self):
        print("\nget message start")
        yield "hello"
        print("\nget message finish")

    def test_message(self, get_message):
        assert "hello" == get_message


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
