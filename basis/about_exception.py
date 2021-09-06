# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import traceback

if __name__ == "__main__":

    x, y = 1, 0
    try:
        z = x / y
    except Exception as exp:
        # 打印堆栈信息
        traceback.print_exc()
