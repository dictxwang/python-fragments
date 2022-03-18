# -*- coding: utf8 -*-
__author__ = 'wangqiang'


"""
基于哈夫曼编码实现压缩/解压缩
"""

import about_huffman
import pickle


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


def compress(huffman_tree, source_file):
    """
    执行压缩
    :param huffman_tree: 哈夫曼树
    :param source_file: 原文件
    :return:
    """
    compress_file = source_file + ".zip"
    ofp = open(compress_file, mode="wb")
    # 序列化huffman树，以便保存到文件中
    huffman_bytes = pickle.dumps(huffman_tree)
    huffman_length = len(huffman_bytes)

    # 第一个字节写入huffman树的长度（默认用2个字节来保存这个长度，最大值short足够了）
    ofp.write(int.to_bytes(huffman_length, length=2, byteorder="big"))
    ofp.write(huffman_bytes)
    ofp.flush()

    encoding_map = {}
    for e in huffman_tree.get_encodings():
        encoding_map[e[0]] = e[1]

    # 保存中间转换结果（字节到huffman编码的映射）
    codes = ""
    fp = open(source_file, mode="rb")
    buf = fp.read(1)
    while buf:
        encoding = encoding_map[int.from_bytes(buf, byteorder="big")]
        codes += encoding
        # 如果长度满足一个字节，转换成bytes并写入压缩文件
        while len(codes) >= 8:
            ofp.write(int.to_bytes(int(codes[:8], 2), length=1, byteorder="big"))
            ofp.flush()
            codes = codes[8:]
        # 继续读取文件
        buf = fp.read(1)

    append_bits = 0
    if len(codes) > 0:
        # 转换剩余的字符（需要先进行位数补齐）
        append_bits = 8 - len(codes)
        codes += "0" * append_bits
        ofp.write(int.to_bytes(int(codes[:], 2), length=1, byteorder="big"))
    # 写入补齐的位数
    ofp.write(int.to_bytes(append_bits, length=1, byteorder="big"))
    ofp.flush()

    fp.close()
    ofp.close()


def uncompress(compress_file):
    """
    解压缩
    压缩文件字节序列 {2bytes：huffman树字节长度 + nbytes：压缩后字节 + 1byte：末尾补齐的位数}
    :param compress_file:
    :return:
    """
    def huffman_decode(huffman_tree, codes):
        """
        解码
        :param huffman_tree:
        :param codes:
        :return: (剩余的code，解码后的结果list)
        """
        text = []
        remain = ""
        node = huffman_tree.get_root()
        for i in range(len(codes)):
            if codes[i] == "0":
                node = node.get_left()
            else:
                node = node.get_right()
            if node.get_name():
                # 匹配成功，回到根节点重新开始
                remain = codes[i + 1:]
                text.append(node.get_name())
                node = huffman_tree.get_root()
        return remain, text

    fp = open(compress_file, mode="rb")
    # 首先读取前两个字节
    buf = fp.read(2)
    huffman_length = int.from_bytes(buf, byteorder="big")
    # 读取huffman树的字节
    huffman_bytes = fp.read(huffman_length)
    huffman_tree = pickle.loads(huffman_bytes)
    ofp = open(compress_file + ".d", mode="wb")

    read_size = 4096
    buf = fp.read(read_size)
    offset = 2 + huffman_length
    append_bits = 0
    codes = ""
    while buf:
        offset = offset + len(buf)
        # 判断是否读取到末尾
        read_end = False
        if len(buf) < read_size:
            # 已经读到末尾
            buf_last = buf[len(buf) - 1:]
            buf = buf[:len(buf) - 1]
            append_bits = int.from_bytes(buf_last, byteorder="big")
            read_end = True
        else:
            # 再多读两位试试
            buf_more = fp.read(2)
            if not buf_more:
                # 已经在之前读取到末尾字节
                buf_last = buf[read_size - 1:]
                buf = buf[:read_size - 1]
                append_bits = int.from_bytes(buf_last, byteorder="big")
                read_end = True
            elif len(buf_more) == 1:
                # 正好读到末尾字节，解析出填充长度
                append_bits = int.from_bytes(buf_more, byteorder="big")
                read_end = True
            else:
                # 未读到末尾，指针回退到多读两位前
                fp.seek(offset, 0)

        for i in range(len(buf)):
            # c = int.from_bytes(buf[i], byteorder="big")
            # 转成2进制并补齐8位
            c = bin(buf[i])[2:].rjust(8, "0")
            if read_end and i == len(buf) - 1:
                # 移除追加到末尾的补位字符
                c = c[:8 - append_bits]
            codes += c

        # huffman解码
        codes, result = huffman_decode(huffman_tree, codes)
        if result:
            for r in result:
                ofp.write(int.to_bytes(r, 1, byteorder="big"))
            ofp.flush()
        if not read_end:
            buf = fp.read(read_size)
        else:
            buf = None
    ofp.close()
    fp.close()


if __name__ == '__main__':

    # 压缩
    source_file = "data/for_huffman_compression.txt"
    huffman = make_huffman_from_source(source_file)
    compress(huffman, source_file)

    # 解压缩
    compress_file = "data/for_huffman_compression.txt.zip"
    uncompress(compress_file)
