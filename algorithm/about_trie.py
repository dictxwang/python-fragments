# -*- coding: utf8 -*-
__author__ = 'wangqiang'

"""
Trie字典树
"""


class Node:

    def __init__(self, key):
        self._key = key
        # 所有的next节点（key: node）
        self._children = {}
        self._is_word = False

    def get_key(self):
        return self._key

    def append_child(self, key, node):
        self._children[key] = node

    def remove_child(self, key):
        if key in self._children:
            del self._children[key]

    def get_children(self):
        return self._children

    def get_child(self, key):
        if key in self._children:
            return self._children[key]
        else:
            return None

    def set_is_word(self, is_word=True):
        self._is_word = is_word

    def get_is_word(self):
        return self._is_word


class Trie:

    def __init__(self):
        # 根节点
        self._root = Node(None)

    def insert(self, word) -> None:
        if word is None:
            return

        root = self._root
        for c in word:
            node = root.get_child(c)
            if node is None:
                node = Node(c)
                root.append_child(c, node)
            root = node
        node.set_is_word(is_word=True)

    def remove(self, word) -> None:
        """
        移除单词
        :param word:
        :return:
        """
        def remove_word(word, last_node):
            if last_node.get_is_word():
                # 如果是单词节点，不能移除
                return
            if len(last_node.get_children()) > 0:
                # 如果还有子节点，直接返回
                return
            if len(word) == 1:
                # 从根节点移除即可
                self._root.remove_child(word[0:1])
                return
            # 找到末尾字符的父节点
            parent = self._root
            for c in word[:len(word) - 1]:
                parent = parent.get_child(c)

        if not word:
            return
        # 找到最后一个字符的节点
        node = self._root
        for c in word:
            node = node.get_child(c)
            if not node:
                break

        # 未找到节点或者节点不是完整的单词
        if not node or not node.get_is_word():
            return
        # 将节点置为非单词
        node.set_is_word(is_word=False)


    def search(self, word) -> bool:
        """
        判断单词是否在trie中
        :param word:
        :return:
        """
        if not word:
            return False
        node = self._root
        for c in word:
            child = node.get_child(c)
            if not child:
                return False
            node = child
        return node.get_is_word()

    def starts_with(self, prefix) -> bool:
        """
        判断是否以指定字符串开头
        :param prefix:
        :return:
        """
        if not prefix:
            return False
        node = self._root
        for c in prefix:
            child = node.get_child(c)
            if not child:
                return False
            node = child
        return True

    def get_words_start_with(self, prefix):
        """
        查找以指定字符串开头的单词
        :param prefix:
        :return:
        """
        def find_words(prefix, pre_node):
            word_list = []
            if pre_node.get_is_word():
                word_list.append(prefix)
            for key, child in pre_node.get_children().items():
                word_list.extend(find_words(prefix + key, child))
            return word_list

        if not self.starts_with(prefix):
            # 没有prefix开头的词
            return []
        # 找到prefix最后一个字符的node
        node = self._root
        for c in prefix:
            node = node.get_child(c)
        return find_words(prefix, node)


if __name__ == '__main__':
    trie = Trie()
    trie.insert("hello")
    trie.insert("world")
    trie.insert("I")
    trie.insert("like")
    trie.insert("programing")

    print(trie.search("world"))
    print(trie.search("I"))
    print(trie.search("like"))
    print(trie.search("i"))
    print(trie.search("lik"))
    print(trie.starts_with("lik"))

    trie.insert("abc")
    trie.insert("abcd")
    trie.insert("abcde")
    trie.insert("abcdef")
    trie.insert("abcdefg")
    print(trie.get_words_start_with("like"))
    print(trie.get_words_start_with("lik"))
    print(trie.get_words_start_with("zyx"))
    print(trie.get_words_start_with("likep"))
    print(trie.get_words_start_with("abcd"))
