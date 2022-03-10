#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import os
from subprocess import check_call
from subprocess import call

if __name__ == '__main__':

    cmd = "ls -ls /"
    # 方法一：通过os.system
    print(os.system(cmd))

    # 方法二：通过check_call
    print(check_call(cmd, shell=True))

    # 方法三：通过call
    print(call(["ls", "-ls", "/"], timeout=5))

    # 方法四：通过popen（需要解析response）
    resp = os.popen(cmd)
    result = []
    while True:
        cresult = resp.readline()
        if cresult:
            for r in cresult.split("\n"):
                if r:
                    result.append(r)
        else:
            break
    for l in result:
        print(l)

    # 辅助方法，切换执行命令的路径
    os.chdir("/")
