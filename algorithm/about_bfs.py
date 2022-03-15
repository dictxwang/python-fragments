# -*- coding: utf8 -*-
__author__ = 'wangqiang'


"""
图的遍历：广度优先遍历
"""


def bfs(graph, start):
    result = []
    # 通过队列保存待遍历的节点
    queue = [start]
    # set过滤已经遍历过的节点
    viewed = set()
    viewed.add(start)
    while len(queue) > 0:
        vertex = queue.pop(0)  # 弹出第一个元素
        nodes = graph[vertex]
        for w in nodes:
            if w not in viewed:
                queue.append(w)
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

    result = bfs(graph, "A")
    print(result)  # ['A', 'B', 'C', 'D', 'E', 'F']
