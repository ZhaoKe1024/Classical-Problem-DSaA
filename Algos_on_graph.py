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
        [-1, -1, 15, 0, 3, -1, 9],
        [-1, -1, -1, 3, 0, 17, 16],
        [28, -1, -1, -1, 17, 0, 25],
        [36, 1, 4, 9, 16, 25, 0]
    ]


def get_graph5():
    # test kruskal
    return [
        (0, 1, 20), (0, 3, 21), (1, 2, 7),
        (1, 4, 5), (1, 3, 13), (3, 4, 10),
        (3, 5, 14), (2, 4, 1), (4, 5, 22),
        (4, 6, 15), (5, 6, 4), (4, 7, 6),
        (6, 7, 11), (6, 8, 3), (7, 8, 2),
        (6, 9, 19), (8, 9, 18), (10, 9, 17),
        (8, 10, 12), (7, 10, 8), (7, 11, 9),
        (10, 11, 16)
    ]


def get_graph6():
    # test floyd
    return [
        [0, 12, -1, -1, -1, 16, 14],
        [12, 0, 10, -1, -1, 7, -1],
        [-1, 10, 0, 3, 5, 6, -1],
        [-1, -1, 3, 0, 4, -1, -1],
        [-1, -1, 5, 4, 0, 2, 8],
        [16, 7, 6, -1, 2, 0, 9],
        [14, -1, -1, -1, 8, 9, 0]
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


def mst_my(graph: List[List[int]]):
    # minimum spanning tree for UDG
    # O(n^3)
    vnum = len(graph)
    # dist = [-1] * vnum
    marker = [False] * vnum
    vcur = 0
    # dist[vcur] = 0
    marker[vcur] = True
    res = [vcur]
    st = [-1]
    # print(dist)
    while len(res) < vnum:
        minval = -1
        minst = -1
        minidx = -1
        for v in res:
            for i in range(len(graph[v])):
                if graph[v][i] == -1:
                    continue
                if (not marker[i]) and (minval == -1 or (graph[v][i] < minval)):
                    minval = graph[v][i]
                    minst = v
                    minidx = i
        print("minidx minval:", minidx, minval)
        marker[minidx] = True
        st.append(minst)
        res.append(minidx)
    for i in range(len(st)):
        print("{}->{}".format(st[i], res[i]))


def mst_prim(graph: List[List[int]]):
    # minimum spanning tree Prim Algorithm for UDG
    # O(n^2)
    vnum = len(graph)
    vcur = 0
    st = [-1] * vnum
    dist = [-1] * vnum
    for i in range(vnum):
        if graph[0][i] <= 0:
            continue
        else:
            dist[i] = graph[0][i]
            st[i] = 0
    marker = [False] * vnum
    marker[vcur] = True
    res_st = [-1]
    res = [vcur]
    # print(dist)
    while len(res) < vnum:
        minval = -1
        minst = -1
        minidx = -1
        for i in range(vnum):
            if dist[i] == -1:
                continue
            if (not marker[i]) and (minval == -1 or (dist[i] < minval)):
                minval = dist[i]
                minst = st[i]
                minidx = i
        # print("minst minidx minval:", minst, minidx, minval)
        marker[minidx] = True
        res_st.append(minst)
        res.append(minidx)
        for i in range(vnum):
            if graph[minidx][i] <= 0:
                continue
            if (dist[i] == -1) or (dist[i] > graph[minidx][i]):
                dist[i] = graph[minidx][i]
                st[i] = minidx
        # print(dist)
    for i in range(len(st)):
        print("{}->{}".format(res_st[i], res[i]))


class UnionFindSet(object):
    """并查集"""

    def __init__(self):
        """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
        初始化的时候，将节点的父节点设为自身，size设为1"""
        self.father_dict = {}
        self.size_dict = {}

    def find(self, node):
        """使用递归的方式来查找父节点
        在查找父节点的时候，顺便把当前节点移动到父节点上面
        这个操作算是一个优化
        """
        if node not in self.father_dict:
            return None
        father = self.father_dict[node]
        if node != father:
            if father != self.father_dict[father]:  # 在降低树高优化时，确保父节点大小字典正确
                self.size_dict[father] -= 1
            father = self.find(father)
        self.father_dict[node] = father
        return father

    def isin(self, v):
        return v in self.father_dict

    def add(self, v):
        self.father_dict[v] = v
        self.size_dict[v] = 1

    def is_same_set(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        a_head = self.find(node_a)
        b_head = self.find(node_b)
        if a_head != b_head:
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if a_set_size >= b_set_size:
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size


def mst_kruskal(edges: List[tuple]):
    # minimum spanning tree Prim Algorithm for UDG
    # O(n^2)
    # vnum = len(graph)
    # edges = []
    # for i in range(vnum):
    #     for j in range(vnum):
    #         if graph[i][j] != -1:
    #             edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2])
    print(edges)
    res_st = []
    res_en = []
    res_va = []
    s = UnionFindSet()
    # print(dist)
    for edge in edges:
        if s.isin(edge[0]):
            if s.isin(edge[1]):
                if s.is_same_set(edge[0], edge[1]):
                    continue
                else:
                    res_st.append(edge[0])
                    res_en.append(edge[1])
                    res_va.append(edge[2])
                    s.union(edge[0], edge[1])
            else:
                res_st.append(edge[0])
                res_en.append(edge[1])
                res_va.append(edge[2])
                s.add(edge[1])
                s.union(edge[0], edge[1])
        else:
            s.add(edge[0])
            if not s.isin(edge[1]):
                s.add(edge[1])
            s.union(edge[0], edge[1])
            res_st.append(edge[0])
            res_en.append(edge[1])
            res_va.append(edge[2])
    for i in range(len(res_st)):
        print("{}->{}:{}".format(res_st[i], res_en[i], res_va[i]))


def sp_floyd():
    # multi-source shortest path
    pass


if __name__ == '__main__':
    # graph1 = get_graph4()
    # for item in graph1:
    #     print('\t'.join([str(v) for v in item]))
    graph5 = get_graph5()
    for item in graph5:
        print("{}->{}:{}".format(item[0], item[1], item[2]))
    mst_kruskal(graph5)
    # ssp_dijkstra_udg(get_graph3(), 0)
