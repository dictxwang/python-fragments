# -*- coding: utf8 -*-
__author__ = 'wangqiang'


"""
哈夫曼编码
"""


class Node:

    def __init__(self, name, value):
        self._name = name
        self._value = value
        self._left = None
        self._right = None

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right


class HuffmanTree:

    def __init__(self, char_weights):
        self._root = Node(None, None)
        self.__build_tree(char_weights)

    def get_root(self):
        return self._root

    def __build_tree(self, char_weights):
        if len(char_weights) <= 1:
            return
        # 按照权重排序
        char_weights = sorted(char_weights, key=lambda x: x[1])

        # 取前两个权重最小的节点
        if len(char_weights[0]) == 3:
            left = char_weights[0][2]
        else:
            left = Node(char_weights[0][0], char_weights[0][1])
        if len(char_weights[1]) == 3:
            right = char_weights[1][2]
        else:
            right = Node(char_weights[1][0], char_weights[1][1])

        if len(char_weights) == 2:
            # 只剩两个节点，直接追加到root节点完事
            self._root.set_left(left)
            self._root.set_right(right)
        else:
            # 移除已经合并的节点
            del char_weights[0]
            del char_weights[0]
            # 生成新的节点
            new_node = Node(None, left.get_value() + right.get_value())
            new_node.set_left(left)
            new_node.set_right(right)
            # 将新节点保存到tuple中
            new_weight = (None, left.get_value() + right.get_value(), new_node)
            char_weights.append(new_weight)
            self.__build_tree(char_weights)

    def get_encodings(self):
        """
        获取编码表
        :return:
        """
        def encode(prefix, node):
            result = []
            if node is None:
                return result
            # 左子树是0右子树是1，根节点默认是0
            if node.get_name():
                result.append((node.get_name(), prefix))
            if node.get_left():
                result.extend(encode(prefix + "0", node.get_left()))
            if node.get_right():
                result.extend(encode(prefix + "1", node.get_right()))
            return result

        result = encode("", self._root)
        return result


if __name__ == '__main__':
    char_weights = [("A", 12), ("B", 1), ("D", 4), ("C", 5), ("E", 100), ("F", 40)]
    huffman = HuffmanTree(char_weights)
    print(huffman.get_encodings())
