# -*- coding: utf8 -*-
__author__ = 'wangqiang'


"""
红黑树的实现
红黑树的特性：
    1、每个节点或者红色，或者黑色
    2、根节点是黑色
    3、每个叶子节点（nil）是黑色（这里叶子节点，是指为空（NIL或NULL）的叶子节点！）
    4、如果一个节点是红色，则它的子节点必须是黑色
    5、从一个节点到该节点的子孙节点的所有路径上包含相同数目的黑色节点

注：当前仅实现了二叉查找树
"""


class Node:

    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._left = None
        self._right = None
        self._parent = None
        self._black = True

    def get_key(self):
        return self._key

    def get_value(self):
        return self._value

    def set_value(self, val):
        self._value = val

    def set_left(self, left):
        self._left = left

    def get_left(self):
        return self._left

    def set_right(self, right):
        self._right = right

    def get_right(self):
        return self._right

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent

    def set_color_black(self):
        self._black = True

    def set_color_red(self):
        self._black = False

    def is_black(self):
        return self._black


class RedBlackTree:

    def __init__(self):
        self._root = None
        self._size = 0

    def _find(self, root, key):
        """
        查找key所在的节点
        :param root: 起始查找节点
        :param key:
        """
        if root is None or key is None:
            return None
        root_key = root.get_key()
        if root_key == key:
            # 查找到就是当前节点
            return root
        elif key < root_key:
            if root.get_left():
                # 在左子树查找
                return self._find(root.get_left(), key)
        else:
            if root.get_right():
                # 在右子树查找
                return self._find(root.get_right(), key)
        # 递归以后仍未找到
        return None

    def _find_parent_and_node(self, root, key):
        """
        查找节点，返回当前节点以及其父节点
        :param root:
        :param key:
        :return: (parent,node)
        """
        if root is None or key is None:
            return None, None
        parent = None
        node = None
        while root is not None:
            root_key = root.get_key()
            if root_key == key:
                # 找到匹配跳出循环
                parent = root.get_parent()
                node = root
                break
            parent = root
            if key < root_key and root.get_left() is not None:
                # 继续查找左子树
                root = root.get_left()
                continue
            if key > root_key and root.get_right() is not None:
                # 继续查找右子树
                root = root.get_right()
                continue
            root = None
        return parent, node

    def _find_last_left_node(self, root):
        """
        找到最末尾的左子节点
        :param root:
        :return:
        """
        if root is None:
            return None
        while root.get_left() is not None:
            root = root.get_left()
        return root

    def set(self, key, val):
        if key is None or val is None:
            return
        node = Node(key, val)
        new_node = False
        if self._root is None:
            # 如果树为空，添加到根节点
            self._root = node
            new_node = True
        else:
            # 查找插入点
            parent, exists_node = self._find_parent_and_node(self._root, key)
            if exists_node is not None:
                # 节点已存在，更新值即可
                exists_node.set_value(val)
            else:
                parent_key = parent.get_key()
                node.set_parent(parent)
                if key > parent_key:
                    # 设置为右子节点
                    parent.set_right(node)
                else:
                    # 设置为左子节点
                    parent.set_left(node)

                new_node = True

        if new_node:
            self._size += 1

    def get(self, key):
        node = self._find(self._root, key)
        return node.get_value() if node else None

    def remove(self, key):
        if key is None or self._size == 0:
            return
        node = self._find(self._root, key)
        if node is None:
            # 未找到节点
            return

        node_left = node.get_left()
        node_right = node.get_right()
        node_parent = node.get_parent()
        # 1、没有左右子节点
        if node_left is None and node_right is None:
            # 1.1、没有父节点
            if node_parent is None:
                self._root = None
            # 1.2、有父节点
            else:
                if node_parent.get_left() == node:
                    node_parent.set_left(None)
                elif node_parent.get_right() == node:
                    node_parent.set_right(None)

        # 2、只有右子节点
        if node_left is None and node_right is not None:
            # 2.1、没有父节点
            if node_parent is None:
                # 右子节点升级为root节点
                self._root = node_right
                node_right.set_parent(None)
            # 2.2、有父节点
            else:
                node_right.set_parent(node_parent)
                if node_parent.get_left() == node:
                    node_parent.set_left(node_right)
                elif node_parent.get_right() == node:
                    node_parent.set_right(node_right)

        # 3、只有左子节点
        if node_right is None and node_left is not None:
            # 3.1、没有父节点
            if node_parent is None:
                # 左子节点升级为root节点
                self._root = node_left
                node_left.set_parent(None)
            # 3.2、有父节点
            else:
                node_left.set_parent(node_parent)
                if node_parent.get_left() == node:
                    node_parent.set_left(node_left)
                elif node_parent.get_right() == node:
                    node_parent.set_right(node_left)

        # 4、同时有左右子节点（将左子节点或右子节点升级为父节点）
        # 这里选择升级左子节点
        # 判断左子节点是否有右孙子节点，如果有将其移到右子节点的左孙子节点末尾
        if node_right is not None and node_left is not None:
            node_left_child_right = node_left.get_right()
            if node_left_child_right is not None:
                # 找到右子树的左叶子节点
                last_left = self._find_last_left_node(node_right)
                node_left_child_right.set_parent(last_left)
                last_left.set_left(node_left_child_right)

            # 原右子树设置为新parent的右子树
            node_left.set_right(node_right)
            node_right.set_parent(node_left)

            # 左子树占用原parent的位置
            node_left.set_parent(node_parent)
            if node_parent is not None:
                # 判断原node是祖父节点的左节点还是右节点，进行对应替换
                if node_parent.get_left() == node:
                    node_parent.set_left(node_left)
                else:
                    node_parent.set_right(node_left)
            else:
                self._root = node_left

        self._size -= 1

    def size(self):
        return self._size

    def _iterate_key_middle(self, root, keys):
        """
        中序遍历key
        """
        if root is None:
            return
        self._iterate_key_middle(root.get_left(), keys)
        keys.append(root.get_key())
        self._iterate_key_middle(root.get_right(), keys)

    def get_keys_ordered(self):
        """
        返回有序的key序列（中序遍历树）
        :return:
        """
        keys = []
        self._iterate_key_middle(self._root, keys)
        return keys


if __name__ == '__main__':

    tree = RedBlackTree()
    tree.set("H", 1)
    tree.set("E", 2)
    tree.set("J", 3)
    tree.set("D", 3)
    tree.set("F", 4)
    tree.set("I", 5)
    tree.set("K", 6)
    tree.set("Z", 6)
    tree.set("C", 6)
    tree.set("A", 6)
    print(tree.get_keys_ordered())
    print(tree.get("2"))
    print(tree.size())

    tree.remove("A")
    print(tree.get_keys_ordered())
    tree.remove("Z")
    print(tree.get_keys_ordered())
    tree.remove("J")
    print(tree.get_keys_ordered())
    tree.remove("E")
    print(tree.get_keys_ordered())
    tree.remove("H")
    print(tree.get_keys_ordered())
