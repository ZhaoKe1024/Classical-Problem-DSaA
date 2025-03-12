#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/3/8 17:34
# @Author: ZhaoKe
# @File : segmenttree.py
# @Software: PyCharm
class MyCalendar:
    def __init__(self):
        self.tree = set()
        self.lazy = set()

    def query(self, start: int, end: int, l: int, r: int, idx: int) -> bool:
        if r < start or end < l:
            return False
        if idx in self.lazy:
            return True
        if start <= l and r <= end:
            return idx in self.tree
        mid = (l + r) // 2
        return self.query(start, end, l, mid, 2 * idx) or self.query(start, end, mid + 1, r, 2 * idx + 1)

    def update(self, start: int, end: int, l: int, r: int, idx: int):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree.add(idx)
            self.lazy.add(idx)
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, 2 * idx)
            self.update(start, end, mid+1, r, 2*idx+1)
            self.tree.add(idx)
            if 2*idx in self.lazy and 2*idx+1 in self.lazy:
                self.lazy.add(idx)

    def book(self, start: int, end: int) -> bool:
        if self.query(start, end - 1, 0, 10 ** 9, 1):
            return False
        self.update(start, end - 1, 0, 10 ** 9, 1)


class MyCalendarTwo:
    def __init__(self):
        self.tree = {}

    def update(self, start: int, end: int, val:int, l: int, r: int, idx: int):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            p = self.tree.get(idx, [0, 0])
            p[0] += val
            p[1] += val
            self.tree[idx] = p
            return

        mid = (l + r) // 2
        self.update(start, end, val, l, mid, 2 * idx)
        self.update(start, end, val, mid+1, r, 2*idx+1)
        p = self.tree.get(idx, [0, 0])
        p[0] = p[1] + max(self.tree.get(2*idx, (0,))[0], self.tree.get(2*idx+1, (0,))[0])
        self.tree[idx] = p

    def book(self, start: int, end: int) -> bool:
        self.update(start=start, end=end - 1, val=1, l=0, r=10 ** 9, idx=1)
        if self.tree[1][0] > 2:
            self.update(start=start, end=end-1, val=-1, l=0, r=10**9, idx=1)
            return False
        return True

