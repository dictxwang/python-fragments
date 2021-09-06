# -*- coding: utf8 -*-
__author__ = 'wangqiang'

if __name__ == "__main__":

    # 四舍五入方式保留2位小数（3.14）
    print("{:.2f}".format(3.1415926))
    # 带符号保留2位小数（+3.14）
    print("{:+.2f}".format(3.1415926))
    # (-1.00)
    print("{:+.2f}".format(-1))
    # 四舍五入取整
    print("{:.0f}".format(2.7182))
    # 整数左边补零，宽度为2
    print("{:0>2d}".format(5))
    # 整数右边补x，宽度为4
    print("{:x<4d}".format(4))
    # 以逗号分隔数字
    print("{:,}".format(10000000))
    # 百分号表示，并且保留2位小数
    print("{:.2%}".format(0.25678))
    # 指数表示，并保留2位小数（1.35e+09）
    print("{:.2e}".format(1345600000))
    # 右对齐，宽度为5
    print("{:>5d}".format(23))
    # 左对齐
    print("{:<5d}".format(23))
    # 中间对齐
    print("{:^5d}".format(23))

    # 进制输出
    # 2进制（1011）
    print("{:b}".format(11))
    # 16进制
    print("{:x}".format(11))
    # 8进制
    print("{:o}".format(11))
    # 10进制
    print("{:d}".format(11))
    # 16进制带标志（0xb）
    print("{:#x}".format(11))
    # 16进制带标志（大写表示）（0XB）
    print("{:#X}".format(11))

    # 通过集合进行格式化
    info = [(1, "A"), (2, "B")]
    print("{0[1]},{0[0]}".format(info[1]))
