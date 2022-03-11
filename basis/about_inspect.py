# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
python反射，python自省相关的
'''

import inspect


def add(num1, num2):
    """
    method add
    :param num1:
    :param num2:
    :return: add result
    """
    return num1 + num2


def merge(first, *second, **third):
    """
    merge
    :param first: 参数一
    :param second: 参数二
    :param third: 参数三
    :return: 字符串拼接结果
    """
    result = first
    for s in second:
        result += s
    for k, v in third.items():
        result += k
    return result


class Foo(object):

    addr = "cd"

    def __init__(self, name):
        self.__name = name

    def getname(self):
        """
        获取name
        :return: name
        """
        return self.__name

    @classmethod
    def say(cls):
        print("hello, i am in {}".format(cls.addr))

    @staticmethod
    def say2():
        print("hello, everyone")


if __name__ == "__main__":

    # 获取方法参数信息
    print(inspect.getfullargspec(merge))  # FullArgSpec(args=['first'], varargs='second', varkw='third', defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={})
    # 返回对象的成员（属性、方法）
    print(inspect.getmembers(str))
    print(inspect.getmembers("hello"))
    # 返回对象（方法）的源码
    print(inspect.getsource(add))
    # 判断是否是用户定义的方法
    print(inspect.isfunction(add))  # True
    # 判断是否是实例的方法
    print(inspect.ismethod(add))  # False

    # inspect.isclass是getmembers方法的前置条件
    print(inspect.getmembers(Foo, inspect.isclass))

    # 返回当前调用脚本的执行帧
    print(inspect.currentframe())
    # {code_base}/python-fragments/basis/about_inspect.py
    print(inspect.currentframe().f_code.co_filename)

    foo = Foo(name="liudehua")
    members = inspect.getmembers(foo, predicate=lambda x: inspect.isfunction(x) or inspect.ismethod(x))
    for m in members:
        func_name = m[0]
        if func_name != "__init__":
            m[1]()
