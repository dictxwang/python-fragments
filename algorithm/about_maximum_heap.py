# -*- coding: utf8 -*-
__author__ = 'wangqiang'


'''
最大堆的两种构建方式
最大堆：近似完全二叉树，父节点值始终大于子节点值
数组表示法：子节点下标//2，正好是父节点下标；第一个叶子节点下标是count//2
    当前节点下标*2+1是其左子节点下标，当前节点下标*2+2是其右子节点下标
'''


class MaxHeapA:
    """
    最大堆
    构建方式：
    1、将当前插入的元素直接放至数组的末尾
    2、从插入值开始往上找，如果父结点值比当前数值小，则交换，直到找到比他大的或者没有结点可找之后结束
    """
    def __init__(self):
        self._data = []
        self._count = 0

    def sift_up(self, index):
        while index > 0 and self._data[index // 2] < self._data[index]:
            self._data[index], self._data[index // 2] = self._data[index // 2], self._data[index]
            index //= 2

    def insert(self, value):
        self._data.append(value)
        self._count += 1
        self.sift_up(self._count - 1)

    def print(self):
        print(self._data)


class MaxHeapB:
    """
    最大堆
    构建方式：
    1、直接将整个数据填入数组中
    2、从第一个非叶结点开始，向上走，每次与自己的左、右结点比较，调整位置，直到调整到根结点为止
    注意：这里直接从最后一个节点开始，尽管最后几个节点是叶子节点不需要调整，但是这样处理实现上相对简单
    """
    def __init__(self, nums):
        self._data = []
        self._count = 0

        for n in nums:
            self._data.append(n)
            self._count += 1

        for i in range(self._count, -1, -1):
            self.sift_down(i)

    def sift_down(self, index):
        size = len(self._data)
        latest = index
        # 计算左右子节点下标
        left = index * 2 + 1
        right = index * 2 + 2

        # 如果左子节点存在，并且左子节点大于当前节点，将左子节点作为交换节点
        if left < size and self._data[left] > self._data[index]:
            latest = left
        # 如果右子节点存在，并且右子节点大于当前节点和左子节点，将右子节点作为交换节点
        if right < size and self._data[right] > self._data[latest]:
            latest = right
        if latest != index:
            self._data[latest], self._data[index] = self._data[index], self._data[latest]
            # 因为发送了节点交换，递归构建当前节点的子树使其保持最大堆结构
            self.sift_down(latest)

    def print(self):
        print(self._data)


if __name__ == '__main__':

    """
    A、B两种方式构造的数结构略有差异，但是都满足最大堆的结构
    """

    lst = [10, 20, 9, 4, 5, 30, 2, 2, -10, 50, 100, 340]
    heapA = MaxHeapA()
    for val in lst:
        heapA.insert(val)
    heapA.print()  # [340, 100, 50, 4, 10, 30, 2, 2, -10, 5, 9, 20]

    heapB = MaxHeapB(lst)
    heapB.print()  # [340, 100, 30, 4, 50, 10, 2, 2, -10, 20, 5, 9]
