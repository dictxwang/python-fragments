# -*- coding: utf8 -*-
__author__ = 'wangqiang'


def change_lst(lst):
    '''
    测试对象的引用传递
    :param lst:
    :return:
    '''
    lst[0] = "AA"
    print("{0}".format(lst))
    # 此处的改变不会传递到函数外
    lst = ["BB", "123"]


def has_default_parameter(name="wangqiang"):
    print(name)


def decorator_001(func):
    '''
    函数装饰器
    :param func:
    :return:
    '''
    def wrap(args):
        print("pre process")
        result = func(args)
        print("post process")
        return result
    return wrap


@decorator_001
def user_decorator(name="wangqiang"):
    # .title()每个单词首字母大写
    name = name.title()
    return name


def tuple_param(*tup):
    '''
    单个* 接受任意数量参数，并将参数解析为元组
    :param tup:
    :return:
    '''
    return tup


def dict_param(**dict):
    '''
    两个* 接受任意数量参数，并将参数解析为字典
    :param dict:
    :return:
    '''
    return dict


if __name__ == "__main__":

    lst = [1, 2, 3]
    change_lst(lst)
    print("{0}".format(lst))

    # 获取默认参数
    print(has_default_parameter.__defaults__)

    # 函数装饰器
    name = user_decorator("dict wang")
    print(name)

    # 元组类型参数
    # (1, 2, 3) 参数将被解析为元组
    print(tuple_param(1, 2, 3))

    # 字典类型参数
    # {'a': 1, 'b': 2, 'c': 3}
    print(dict_param(a=1, b=2, c=3))