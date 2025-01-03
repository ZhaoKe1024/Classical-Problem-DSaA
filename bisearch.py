#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/1/3 10:00
# @Author: ZhaoKe
# @File : bisearch.py
# @Software: PyCharm
from typing import List


def bis_position(arr: List, p):
    if len(arr) == 0:
        arr.append(p)
        print(arr)
        return
    elif len(arr) == 1:
        if p < arr[0]:
            arr.insert(0, p)
            print(arr)
            return
        else:
            arr.append(p)
            print(arr)
            return
    lp, rp = 0, len(arr) - 1
    tp = None
    while True:
        mp = (lp + rp) // 2
        # print(lp, mp, rp)
        if lp >= mp:
            if p <= arr[lp]:
                tp = lp
                break
            else:
                if p < arr[rp]:
                    tp = rp
                else:
                    tp = rp + 1
                break
        if arr[mp] == p:
            tp = mp + 1
            break
        elif p > arr[mp]:
            lp = mp
        else:
            rp = mp
    arr.insert(tp, p)
    print(arr)

if __name__ == '__main__':
    bis_position([], 1)
    bis_position([2], 1)
    bis_position([4, 5], 1)
    bis_position([3, 5], 6)
    bis_position([1, 4, 6, 7, 9, 10], 8)
    bis_position([1, 4, 6, 7, 9, 10], 3)
    bis_position([1, 4, 6, 7, 9, 10], 5)
