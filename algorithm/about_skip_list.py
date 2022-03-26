#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

"""
skipList跳表的python实现
"""

from typing import Optional
import random


class Node:
    # 这里Optional的含义是int或者None均可
    def __init__(self, data: Optional[int] = None):
        self._data = data
        self._forwards = []

    def get_data(self):
        return self._data

    def set_forwards(self, forwards):
        self._forwards = forwards

    def get_forwards(self):
        return self._forwards


class SkipList:
    _max_level = 6

    def __init__(self):
        self._level_count = 1
        self._head = Node()
        self._head._forwards = [None] * type(self)._max_level

    def find(self, value: int) -> Optional[None]:
        p = self._head
        # 从最外层的指针开始遍历
        for i in range(self._level_count - 1, -1, -1):
            while p.get_forwards()[i] and p.get_forwards()[i].get_data() < value:
                p = p.get_forwards()[i]

        # 判断第一层，实际上就是判断p的下一个节点
        return p.get_forwards()[0] if p.get_forwards()[0] and p.get_forwards()[0].get_data() == value else None

    def insert(self, value: int):
        level = self._random_level()
        new_node = Node(value)
        new_node.set_forwards([None] * level)
        update = [None] * level
        p = self._head
        for i in range(level - 1, -1, -1):
            while p.get_forwards()[i] and p.get_forwards()[i].get_data() < value:
                p = p.get_forwards()[i]
            update[i] = p

        # 交换每一层指针的指向
        for i in range(level):
            new_node.get_forwards()[i] = update[i].get_forwards()[i]
            update[i].get_forwards()[i] = new_node
        if level > self._level_count:
            self._level_count = level

    def delete(self, value: int):
        update = [None] * self._level_count
        p = self._head
        for i in range(self._level_count - 1, -1, -1):
            while p.get_forwards()[i] and p.get_forwards()[i].get_data() < value:
                p = p.get_forwards()[i]
            update[i] = p
        # 确定找到value后，交换每一层指针的指向
        if p.get_forwards()[0] and p.get_forwards()[0].get_data() == value:
            for i in range(self._level_count - 1, -1, -1):
                if update[i].get_forwards()[i] and update[i].get_forwards()[i].get_data() == value:
                    update[i].get_forwards()[i] = update[i].get_forwards()[i].get_forwards()[i]

    def _random_level(self, p: float = 0.5) -> int:
        """
        获取节点指针层级，理论来讲，一级索引中元素个数应该占原始数据的 50%，二级索引中元素个数占 25%，三级索引12.5% ，一直到最顶层。
        因为这里每一层的晋升概率是 50%。对于每一个新插入的节点，都需要调用 randomLevel 生成一个合理的层数。
        该 randomLevel 方法会随机生成 1~MAX_LEVEL 之间的数，且 ：
            50%的概率返回 1
            25%的概率返回 2
            12.5%的概率返回 3 ...
        :param p:
        :return:
        """
        level = 1
        while random.random() < p and level < type(self)._max_level:
            level += 1
        return level

    def pprint(self):
        for i in range(self._level_count):
            datas = []
            node = self._head
            while node.get_forwards()[i]:
                datas.append(str(node.get_forwards()[i].get_data()))
                node = node.get_forwards()[i]
            print("pointer path" + str(i) + ": *head -> " + " -> ".join(datas))


if __name__ == '__main__':
    sk = SkipList()
    for v in range(-30, 200, 3):
        sk.insert(v)
    sk.pprint()
    node = sk.find(189)
    print("find num {}".format(node.get_data()) if node else "not found 189")

    sk.delete(189)
    node = sk.find(189)
    print("find num {}".format(node.get_data()) if node else "not found 189")
