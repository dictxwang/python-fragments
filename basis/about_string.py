# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
字符串操作相关的功能
'''

if __name__ == "__main__":

    # 单个字符串多行定义的方式
    # 不会换行
    s1 = """1234\
56789"""
    print(s1)
    # 会换行
    s2 = """12345
56789"""
    print(s2)

    # 不会换行
    s3 = "1234" \
         "56789"
    print(s3)

    # 不会换行(推荐方式)
    s4 = (
        "1234"
        "56789"
    )
    print(s4)

    # 字符串类型判断
    s21 = "123"
    print(isinstance(s21, str)) # True
    # 通过tuple形式传递多个类型
    print(isinstance(s21, (str, int)))

    # *with函数族
    s22 = "abcdefghijklmn"
    print(s22.endswith("n")) # True
    print(s22.endswith(("l", "n"))) # True
    print(s22.endswith("c", 0, 3)) # True

    s23 = "a123bc12de123fg"
    print(s23.count("123")) # 2
    print(s23.count("123", 0, 6)) # 1

    s24 = "123|456|789"
    # 输出一个三元组 ('123', '|', '456|789')
    print(s24.partition("|"))
    # 拆分失败，返回三元组 ('123|456|789', '', '')
    print(s24.partition("xxx"))
    # 输出一个序列 ['123', '456', '789']
    print(s24.split("|"))

    s25 = " what is this\t. "
    # 前后去空格后按空白字符拆分 ['what', 'is', 'this', '.']
    print(s25.split())
    # 严格按照空格拆分 ['', 'what', 'is', 'this\t.', '']
    print(s25.split(' '))

    s26 = "123"
    # 用0填充位数 00123
    print(s26.zfill(5))
    # 以给定的字符填充 zzz123zzzz
    print(s26.center(10, 'z'))
    # 123zz
    print(s26.ljust(5, 'z'))
    # yy123
    print(s26.rjust(5, 'y'))

    s27 = "123\t456"
    # 默认把制表符替换成8个空格
    print(s27.expandtabs())
    # 把制表符替换成2个空格
    print(s27.expandtabs(2))
