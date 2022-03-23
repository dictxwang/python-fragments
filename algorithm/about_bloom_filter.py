# -*- coding: utf8 -*-
__author__ = 'wangqiang'

"""
布隆过滤器：在大量数据中判断数据是否存在，具有非常高的时间效率和空间利用率
    但是不能精确判断存在，只能精确判断不存在；不能查询和删除元素
    已知误判率p，数据规模n，求二进制数组长度m和hash函数个数k
    m = -(n*lnp/(ln2)^2)
    k = (m/n)*ln2
"""

import ctypes
import math


class BloomFilter:
    """
    这里是一个只支持整数的BloomFilter
    """

    def __init__(self, n: int, p: float):
        """
        构造函数
        :param n: 数据规模
        :param p: 允许误判率
        """
        self._bit_size = int(-n * math.log(p) / math.pow(math.log(2), 2))
        self._hash_count = int((self._bit_size / n) * math.log(2))
        # 用int代替bit，后续会进行位运算
        self._bit_array = [0] * (int((self._bit_size + 32 - 1) / 32))

    def put(self, value: int) -> None:
        # hash值的设置参考google的布隆过滤器
        # 整数的hash就是其自身
        hash1 = value.__hash__()
        hash2 = self._unsigned_right_shift(hash1, 16)
        for i in range(self._hash_count):
            combine_hash = hash1 + i * hash2
            if combine_hash < 0:
                combine_hash = ~combine_hash
            combine_hash %= self._bit_size
            # 确定位于第几个int
            index = int(combine_hash / 32)
            # 确定位于int的第几个bit
            position = combine_hash - index * 32  # 等价于 combine_hash % 32
            # 将第index个整数的position位设置为1
            self._bit_array[index] = self._bit_array[index] | (1 << position)

    def contains(self, value):
        hash1 = value.__hash__()
        hash2 = self._unsigned_right_shift(hash1, 16)
        for i in range(self._hash_count):
            combine_hash = hash1 + i * hash2
            if combine_hash < 0:
                combine_hash = ~combine_hash
            combine_hash %= self._bit_size
            # 确定位于第几个int
            index = int(combine_hash / 32)
            # 确定位于int的第几个bit
            position = combine_hash % 32
            # 判断对应位置是否是1
            result = self._bit_array[index] & (1 << position)
            if result == 0:
                return False
        return True

    def _int_overflow(self, value):
        """
        整数溢出的处理
        :param value:
        :return:
        """
        # 4byte int最大值和最小值
        max_int = 2147483647
        min_int = -max_int - 1
        if not min_int <= value <= max_int:
            value = (value + (min_int + 1)) % (2 * (max_int + 1)) - max_int - 1
        return value

    def _unsigned_right_shift(self, value, bit_count):
        """
        无符号右移
        :param value: 待移位的数值
        :param bit_count: 移位位数
        :return:
        """
        if value < 0:
            value = ctypes.c_uint32(value).value
        return self._int_overflow((value >> bit_count))


if __name__ == '__main__':
    bloom = BloomFilter(5000000, 0.01)
    total_size = 100000
    not_contains_count = 0
    for i in range(0, total_size, 2):
        bloom.put(i)
    for i in range(total_size):
        if not bloom.contains(i):
            not_contains_count += 1

    # 真实不存在数量
    real_not_contains = total_size / 2
    # 误判数量
    fail_count = abs(not_contains_count - real_not_contains)
    # 误判率
    fail_rate = float(fail_count / total_size)
    # 32769 50000.0 17231.0 0.17231
    print(not_contains_count, real_not_contains, fail_count, fail_rate)

