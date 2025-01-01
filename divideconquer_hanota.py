# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2025-01-02 1:18
from collections import deque


class mydeque(object):
    def __init__(self, name):
        self.name = name
        self.dq = deque()

    def pop(self):
        return self.dq.pop()

    def append(self, item):
        self.dq.append(item)


def conquer(A: mydeque, C: mydeque):
    print("{}-->{}".format(A.name, C.name))
    item = A.pop()
    C.append(item)


def divide(num, A, B, C):
    if num == 1:
        conquer(A=A, C=C)
        return
    divide(num=num - 1, A=A, B=C, C=B)
    conquer(A=A, C=C)
    divide(num=num - 1, A=B, B=A, C=C)


def hanota(num=3):
    A, B, C = mydeque("A"), mydeque("B"), mydeque("C")
    for i in range(num):
        A.append(num - i)
    divide(num=num, A=A, B=B, C=C)


if __name__ == '__main__':
    hanota(num=3)
