# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import datetime


class c1:
    def __str__(self):
        return "c1.Str"


class c2:
    def __repr__(self):
        return "c2.Repr"


class c3:
    cp01 = {}

    def __init__(self, name="wangqiang"):
        self._name_ = name

    def __new__(cls, *args, **kwargs):
        # 本质上讲，__new__才是构造方法
        pass

    @classmethod
    def cm01(cls, k, v):
        cls.cp01[k] = v

    @classmethod
    def cm02(cls, k):
        # 通过cls访问类属性
        return cls.cp01[k]

    @staticmethod
    def sm01(title):
        return title.title()

    @staticmethod
    def sm02(k):
        # 通过类名访问类属性
        return c3.cp01[k]

    def getName(self):
        return self._name_


if __name__ == "__main__":
    today = datetime.datetime.now()
    # str调用类的__str__方法，用于面向用户输出信息
    print(str(today))
    # repr调用类的__repr__方法，用于面向开发调试输出信息
    print(repr(today))

    c1_inst = c1()
    # 输出自定义的__str__内容
    print(str(c1_inst))
    # 仍然输出内置的__repr__内容
    print(repr(c1_inst))

    c2_inst = c2()
    # 此时输出自定义的__repr__内容
    print(str(c2_inst))
    print(repr(c2_inst))

    #静态方法与类方法
    print(c3.sm01("dict wang"))
    c3.cm01("wangqiang", "123456")
    print(c3.cm02("wangqiang"))
    print(c3.sm02("wangqiang"))

    s = (
        "123"
        "3456"
    )
    print (type(s))
