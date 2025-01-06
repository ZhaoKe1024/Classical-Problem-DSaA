#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/1/4 21:47
# @Author: ZhaoKe
# @File : Algos_on_graph.py
# @Software: PyCharm
from typing import List
from collections import deque


class Graph(object):
    def __init__(self):
        self.vertices = []
        self.edges = [
            [0, 7, 9, -1, -1, 14],
            [-1, 0, -1, 15, -1, -1],
            [-1, 1, 0, 11, -1, -1],
            [-1, -1, -1, 0, 6, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 9, 0]
        ]


def get_graph1():
    # 有向图1
    return [
        [0, 7, 9, -1, -1, 14],
        [-1, 0, -1, 15, -1, -1],
        [-1, 1, 0, 11, -1, -1],
        [-1, -1, -1, 0, 6, -1],
        [-1, -1, -1, -1, 0, -1],
        [-1, -1, -1, -1, 9, 0]
    ]


def get_graph2():
    # 有向图2
    return [
        [0, 6, -1, 4, -1, -1],
        [-1, 0, 2, 1, 3, -1],
        [-1, -1, 0, -1, -1, 7],
        [-1, -1, -1, 0, 2, -1],
        [-1, -1, 3, -1, 0, 2],
        [-1, -1, -1, -1, -1, -1]
    ]


def get_graph3() -> List[List[int]]:
    # 无向图1
    return [
        [0, 10, -1, 4, -1, -1],
        [10, 0, 8, 2, 6, -1],
        [-1, 8, 0, 15, 1, 5],
        [4, 2, 15, 0, 6, -1],
        [-1, 6, 1, 6, 0, 12],
        [-1, -1, 5, -1, 12, 0]
    ]


def get_graph4():
    # 无向图2
    return [
        [0, 23, -1, -1, -1, 28, 36],
        [23, 0, 20, -1, -1, -1, 1],
        [-1, 20, 0, 15, -1, -1, 4],
        [-1, -1, 15,  0, 3, -1, 9],
        [-1, -1, -1,  3, 0, 17, 16],
        [28, -1, -1, -1, 17, 0, 25],
        [36,  1,  4,  9, 16, 25, 0]
    ]


def ssp_dijkstra_dag(graph: List[List[int]], vs: int):
    # single source shortest path for DAG
    vnum = len(graph)
    dq = deque()
    dq.append(vs)
    dist = [-1] * vnum
    for i in range(len(graph[vs])):
        if graph[vs][i] > -1:
            dist[i] = graph[vs][i]
            dq.append(i)
    while len(dq) > 0:
        vcur = dq.popleft()
        for j in range(vnum):
            if graph[vcur][j] > 0:
                if (dist[j] == -1) or (dist[vcur] + graph[vcur][j] < dist[j]):
                    dist[j] = dist[vcur] + graph[vcur][j]
                    dq.append(j)
    print(dist)


def ssp_dijkstra_udg(graph: List[List[int]], vs: int):
    # single source shortest path for UDG
    vnum = len(graph)
    dist = [-1] * vnum
    marker = [False] * vnum
    cnt = 0
    dist[vs] = 0
    print(cnt, vnum)
    print(dist)
    while cnt < vnum:
        minval = -1
        minidx = -1
        for i in range(vnum):
            if dist[i] == -1:
                continue
            if (not marker[i]) and (minval == -1 or (dist[i] < minval)):
                minval = dist[i]
                minidx = i
        print("minidx minval:", minidx, minval)
        marker[minidx] = True
        if minval == -1:
            break
        cnt += 1
        for idx in range(vnum):
            if graph[minidx][idx] == -1:
                continue
            if dist[idx] == -1 or (dist[idx] > dist[minidx] + graph[minidx][idx]):
                dist[idx] = dist[minidx] + graph[minidx][idx]
        print(dist)
    print(dist)


def mst_prim():
    pass


def sp_floyd():
    # multi-source shortest path
    pass


def shortest_path_on_graph(graph: List[List[int]]) -> List[int]:
    pass


if __name__ == '__main__':
    graph1 = get_graph3()
    for item in graph1:
        print('\t'.join([str(v) for v in item]))
    ssp_dijkstra_udg(get_graph3(), 0)
