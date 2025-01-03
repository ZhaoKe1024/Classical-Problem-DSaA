#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/1/3 15:43
# @Author: ZhaoKe
# @File : KnapsackCollection.py
# @Software: PyCharm
from typing import List


def knapsack_greedy(capacity: int, weight_list: List, price_list: List) -> int:
    unit_price_list = []
    for i in range(len(weight_list)):
        unit_price_list.append(price_list[i] / weight_list[i])
    print("unit price:", unit_price_list)
    sorted_id = sorted(range(len(unit_price_list)), key=lambda k: unit_price_list[k], reverse=True)
    print("sorted id:", sorted_id)
    sum_price = 0
    sum_weight = 0
    obj_ind = 0
    while sum_weight < capacity:
        if capacity >= sum_weight + weight_list[sorted_id[obj_ind]]:
            sum_price += price_list[sorted_id[obj_ind]]
            sum_weight += weight_list[sorted_id[obj_ind]]
            print("add all of Object:{}".format(sorted_id[obj_ind]))
        else:
            sum_price += capacity // unit_price_list[sorted_id[obj_ind]] * unit_price_list[sorted_id[obj_ind]]
            sum_weight += capacity // unit_price_list[sorted_id[obj_ind]]
            print("add {} Object:{}.".format(capacity // unit_price_list[sorted_id[obj_ind]], sorted_id[obj_ind]))
        print("current sum price {}, capacity:{}/{}.".format(sum_price, sum_weight, capacity))
        obj_ind += 1
    return sum_price


def knapsack_dp(capacity: int, weight_list: List, price_list: List):
    # dynamic programming
    dptable = [[0 for _ in range(capacity)] for _ in range(len(weight_list))]
    for i in range(len(weight_list)):
        for j in range(capacity):
            if j+1 < weight_list[i]:
                continue
            else:
                dptable[i][j] = max(dptable[i - 1][j+1 - weight_list[i]] + price_list[i], dptable[i - 1][j])
    for item in dptable:
        print(item)


def knapsack_backtracking():
    pass


def knapsack_branchBound():
    pass


if __name__ == '__main__':
    knapsack_greedy(capacity=19, weight_list=[8, 1, 9, 3, 2, 4], price_list=[2, 6, 7, 4, 10, 3])
    knapsack_dp(capacity=19, weight_list=[8, 1, 9, 3, 2, 4], price_list=[2, 6, 7, 4, 10, 3])
    knapsack_dp(capacity=5, weight_list=[2, 1, 3, 2], price_list=[12, 10, 20, 15])
