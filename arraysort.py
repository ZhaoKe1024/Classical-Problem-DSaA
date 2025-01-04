#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/1/3 15:28
# @Author: ZhaoKe
# @File : arraysort.py
# @Software: PyCharm
from typing import List


def quicksort(array: List, start=None, end=None) -> None:
    if start is None:
        start, end = 0, len(array)-1
    if start >= end:
        # print(array)
        return
    else:
        base = array[start]
        lp, rp = start, end
        while lp < rp:
            while lp < rp and array[rp] >= base:
                rp -= 1
            array[lp] = array[rp]
            while lp < rp and array[lp] <= base:
                lp += 1
            array[rp] = array[lp]
        array[lp] = base
        quicksort(array, start, lp-1)
        quicksort(array, lp+1, end)


def mergesort(array: List) -> List:
    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return array
    midpos = len(array) // 2
    subarr1 = mergesort(array[:midpos])
    subarr2 = mergesort(array[midpos:])

    resarr = []
    i, j = 0, 0
    while i < len(subarr1) and j < len(subarr2):
        if subarr1[i] < subarr2[j]:
            resarr.append(subarr1[i])
            i += 1
        else:
            resarr.append(subarr2[j])
            j += 1
    if i < len(subarr1):
        resarr.extend(subarr1[i:])
    if j < len(subarr2):
        resarr.extend(subarr2[j:])
    return resarr


if __name__ == '__main__':
    testarr_list = [
        [1, 2, 4, 3, 6, 5, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 0, 1, 2, 3],
        [1, 5, 2, 6, 3, 4, 7, 9, 8, 10]
    ]
    for testarr in testarr_list:
        # print(mergesort(testarr))
        quicksort(testarr)
        print(testarr)
