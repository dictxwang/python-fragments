# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
pip install chardet
'''

import chardet


def use_chardet():
    with open("data/chardet_001.txt") as fp:
        for line in fp.readlines():
            # get encoding and confidence
            # {'encoding': 'utf-8', 'confidence': 0.7525, 'language': ''}
            print(chardet.detect(line.encode()))


def encode_decode():

    txt = "中国"
    # convert string to encoding bytes
    # b'\xe4\xb8\xad\xe5\x9b\xbd'
    encode_bytes = txt.encode("utf8")
    print(encode_bytes)
    # reverse to string
    print(encode_bytes.decode("utf8"))

    # convert to unicode bytes
    unicode_bytes = txt.encode("unicode_escape")
    # b'\\u4e2d\\u56fd'
    print(unicode_bytes)
    # unicode chars to string
    print("\\u4e2d\\u56fd".encode('utf8').decode('unicode_escape'))


def mysql_latin1():

    '''
    如果mysql表编码是latin1，需要注意不能直接从latin1转成utf8，而需要先转成gbk，再转成utf8
    '''
    # 加上当前列的数据是col_data
    col_data = None
    value = col_data.encode("latin1").decode("gbk")
    # 此时value才不会乱码
    print(value)


if __name__ == "__main__":
    use_chardet()
    encode_decode()
