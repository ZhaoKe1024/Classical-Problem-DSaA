# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2025-01-01 22:57
import math


def n_queens_judge(d, queen):
    for i in range(d):
        if (queen[d] == queen[i]) or (abs(queen[i] - queen[d]) == (d - i)):
            return False
    return True


def n_queens_dfs(d, n=8, queen=None, a=None, cnt=None):
    if d >= n:
        print("No.{}".format(cnt))
        cnt += 1
        for i in range(n):
            for j in range(n):
                print(a[j][i], end='')
            print()
        return cnt
    for i in range(n):
        queen[d] = i
        if (a[d][i] != 1) and n_queens_judge(d, queen):
            a[d][i] = 1
            cnt = n_queens_dfs(d=d + 1, n=n, queen=queen, a=a, cnt=cnt)
            a[d][i] = 0
    return cnt


def n_queens(n=8, cnt=1):
    queen = [-1 for _ in range(n)]
    a = [[0 for _ in range(n)] for _ in range(n)]
    n_queens_dfs(0, n=n, queen=queen, a=a, cnt=cnt)


if __name__ == '__main__':
    n_queens(n=5)
