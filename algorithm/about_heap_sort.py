# -*- coding: utf8 -*-
__author__ = 'wangqiang'


'''
堆排序：平均时间复杂度为(n * logn),  空间复杂度为O(1)
'''


def heap_sort(lst):

    def sift_down(current, end):
        """
        判断current节点及其子节点是否满足最大堆，如不满足就进行交换
        :param current: 当前节点下标
        :param end: 队尾节点下标
        """
        latest = current
        left = 2 * current + 1
        right = 2 * current + 2

        if left < end and lst[current] < lst[left]:
            latest = left
        if right < end and lst[latest] < lst[right]:
            latest = right
        # 如果latest == current，代表current节点没有子节点或者无须进行调整
        if latest != current:
            lst[latest], lst[current] = lst[current], lst[latest]
            # 递归判断交换后的节点及其子节点是否满足最大堆
            sift_down(latest, end)

    # 构建最大堆
    # 从最后一个叶子节点开始到根节点结束（实际上前面数次因为叶子节点没有子节点，会浪费掉；但是这样处理逻辑相对简洁）
    for current in range(len(lst), -1, -1):
        sift_down(current, len(lst))

    print(lst)  # [340, 200, 7, 20, 1, -12, 2, 6]

    # 进行排序（将根节点元素往队尾移动，然后再对除队尾外的元素重新构建堆）
    for current in range(len(lst) - 1, 0, -1):
        lst[current], lst[0] = lst[0], lst[current]
        sift_down(0, current)


if __name__ == "__main__":
    lst = [2, 1, 7, 6, 200, -12, 340, 20]
    heap_sort(lst)
    print(lst)  # [-12, 1, 2, 6, 7, 20, 200, 340]
