# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
关于bytes的一些操作
'''

if __name__ == '__main__':

    # 将int型转换为bytes
    value = 20
    # 用一个字节存储，这是字节序设置big和little，实际效果都一样
    b1 = int.to_bytes(value, 1, "little")
    # 将字节转换成int型
    value_from_b1 = int.from_bytes(b1, "little")
    print("value from b1: {}".format(value_from_b1))

    # 超过一个字节存储时，需要注意字节序保持一致
    b2 = int.to_bytes(value, 2, "little")
    value_from_b2 = int.from_bytes(b2, "big")
    # 因为字节序不一致，这里将输出 5120
    print("value from b2: {}".format(value_from_b2))

    # 字符串转bytes，需要注意encoding的设置
    value_s = "我和我的祖国"
    b1_s = value_s.encode(encoding="utf8", errors="ignore")
    # 将字节转换成字符串
    value_from_b1_s = b1_s.decode(encoding="utf8", errors='ignore')
    print("value from b1 s: {}.".format(value_from_b1_s))
    # 转换成其他编码类型
    value_from_b1_s2 = b1_s.decode(encoding="gbk", errors="ignore")
    # 这里控制台输出会显示乱码，但写入对应编码(gbk)的文件是正常的
    print("value from b1 s2: {}".format(value_from_b1_s2))
