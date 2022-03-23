# -*- coding: utf8 -*-
__author__ = 'wangqiang'


"""
布隆过滤器：采用 mmh3 + bitarray 实现（准确率更高）
pip install mmh3
pip install bitarray
"""
import mmh3
from bitarray import bitarray
import math


class BloomFilterAnother:

    def __init__(self, n: int, p: float):
        """
        构造函数
        :param n: 数据规模
        :param p: 允许误判率
        """
        self._bit_size = int(-n * math.log(p) / math.pow(math.log(2), 2))
        self._hash_count = int((self._bit_size / n) * math.log(2))
        bit_array = bitarray(self._bit_size)
        bit_array.setall(0)
        self._bit_array = bit_array

    def put(self, text):
        positions = self._calculate_bit_positions(text)
        for p in positions:
            self._bit_array[p] = 1

    def contains(self, text) -> bool:
        positions = self._calculate_bit_positions(text)
        for p in positions:
            if self._bit_array[p] == 0:
                return False
        return True

    def _calculate_bit_positions(self, text):
        """
        计算bit位置
        :param text:
        :return:
        """
        positions = []
        for i in range(self._hash_count):
            # 直接将i作为seed
            positions.append(mmh3.hash(text, i) % self._bit_size)
        return positions


if __name__ == '__main__':
    bloom = BloomFilterAnother(5000000, 0.01)
    total_size = 100000
    not_contains_count = 0
    for i in range(0, total_size, 2):
        bloom.put(str(i))
    for i in range(total_size):
        if not bloom.contains(str(i)):
            not_contains_count += 1

    # 真实不存在数量
    real_not_contains = total_size / 2
    # 误判数量
    fail_count = abs(not_contains_count - real_not_contains)
    # 误判率
    fail_rate = float(fail_count / total_size)
    # 50000 50000.0 0.0 0.0
    print(not_contains_count, real_not_contains, fail_count, fail_rate)
