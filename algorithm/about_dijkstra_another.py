#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

"""
dijkstra最短路径算法的另一种实现
"""


def dijkstra(graph, start):
    """
    查找start到任意节点的最短路径
    :param graph:
    :param start: 起始节点
    :return:
    """
    # 记录路径结果："起点终点": ("路径", 路径权重)
    result = {start*2: (start, 0)}
    # 记录已经访问过的节点（途中如果没有遇到新的节点，则遍历结束）
    visited = set()
    current = start
    while True:
        nodes = []
        # 查找当前节点的联通节点
        for node in graph[current].keys():
            if node not in visited:
                nodes.append(node)
        # 当前节点没有联通节点，或所有联通节点已经访问过，结束遍历
        if not nodes:
            break

        if start == current:
            # 如果当前节点是起始节点，直接写入路径
            for node in nodes:
                result[start + node] = (start + "->" + node, graph[start][node])
        else:
            # 查找出起始节点到当前节点的路径信息(路径, 权重)
            current_path_weight = result[start+current]

            # 遍历当前节点所有未访问过的联通节点，并记录下起点到联通节点的路径和权重
            for node in nodes:
                weight = graph[current][node]
                # 计算起始节点到联通节点的距离
                distance = current_path_weight[1] + weight
                key = start + node
                if key not in result:
                    # 结果中还没有起始节点到联通节点的路径，直接记录即可
                    result[key] = (current_path_weight[0] + "->" + node, distance)
                else:
                    # 如果结果中已经存在起始节点到联通节点的路径，需要比较权重后保留权重较小的路径
                    exists_distance = result[key][1]
                    if distance < exists_distance:
                        result[key] = (current_path_weight[0] + "->" + node, distance)

        # 标记当前节点已经访问过
        visited.add(current)

        # 从已访问的路径中选择最短的一条，找到其对应的末尾节点继续下一轮遍历
        min_weight = -1
        min_key = None
        for key, t in result.items():
            if key[1:] in visited:
                continue
            if min_weight == -1 or t[1] <= min_weight:
                min_weight = t[1]
                min_key = key
        if min_key:
            # 更新当前节点，继续遍历
            current = min_key[1:]
        else:
            # 遍历完成，跳出while循环
            break
    return result


if __name__ == '__main__':
    # 用字典来表示图
    graph = {
        "A": {"F": 1, "B": 10, "D": 9},
        "B": {"C": 5, "A": 10, "E": 3},
        "C": {"B": 5, "D": 6},
        "D": {"C": 6, "E": 2, "A": 9, "F": 12},
        "E": {"B": 3, "D": 2, "F": 1},
        "F": {"A": 1, "E": 1, "D": 12}
    }
    paths = dijkstra(graph, "A")
    for k, v in paths.items():
        print(k, v)
'''
AA ('A', 0)
AF ('A->F', 1)
AB ('A->F->E->B', 5)
AD ('A->F->E->D', 4)
AE ('A->F->E', 2)
AC ('A->F->E->D->C', 10)
'''
