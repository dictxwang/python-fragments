# -*- coding: utf8 -*-
__author__ = 'wangqiang'


"""
基于哈夫曼编码实现压缩/解压缩
"""

import about_huffman


def make_huffman_from_source(file_path):
    """
    通过原文件构建huffman树
    :param file_path:
    :return:
    """
    bytes_times = {}

    fb = open(file_path, mode="rb")
    b = fb.read(1)
    while b:
        val = int.from_bytes(b, byteorder="big")
        if val in bytes_times:
            bytes_times[val] += 1
        else:
            bytes_times[val] = 1
        b = fb.read(1)
    fb.close()

    bytes_weights = []
    for b, t in bytes_times.items():
        bytes_weights.append((b, t))
    huffman_tree = about_huffman.HuffmanTree(bytes_weights)
    return huffman_tree


if __name__ == '__main__':

    source_file = "E:/data_transfer/index.html"
    huffman = make_huffman_from_source(source_file)
    print(huffman.get_encodings())
    # todo
