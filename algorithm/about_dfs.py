# -*- coding: utf8 -*-
__author__ = 'wangqiang'


"""
图的遍历：深度优先遍历
"""


def dfs(graph, start):
    result = []
    # 通过栈保存待遍历的节点
    stack = [start]
    # set保存已经遍历过的节点
    viewed = set()
    viewed.add(start)
    while len(stack) > 0:
        vertex = stack.pop()  # 弹出最后一个元素
        nodes = graph[vertex]
        for w in nodes:
            if w not in viewed:
                stack.append(w)
                viewed.add(w)
        result.append(vertex)
    return result


if __name__ == '__main__':
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"]
    }

    result = dfs(graph, "A")
    print(result)  # ['A', 'C', 'E', 'D', 'F', 'B']
