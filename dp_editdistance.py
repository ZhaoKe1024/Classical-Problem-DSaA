# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2025-01-02 0:15

def edit_distance(s1: str, s2: str) -> int:
    m, n = len(s1) + 1, len(s2) + 1
    if m == 1:
        if n == 1:
            return 0
        else:
            return n - 1
    elif n == 1:
        return m - 1
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0] = list(range(n))
    for i in range(m):
        dp[i][0] = i
    for i in range(1, m):
        for j in range(1, n):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j - 1], dp[i - 1][j]) + 1
    for item in dp:
        print(item)
    return dp[-1][-1]


if __name__ == '__main__':
    print(edit_distance(s1="", s2="code"))  # 4
    print(edit_distance(s1="leet", s2=""))  # 4
    print(edit_distance(s1="asoul", s2="aoul"))  # 1
    print(edit_distance(s1="asoul", s2="soul"))  # 1
    print(edit_distance(s1="asoul", s2="asou"))  # 1
    print(edit_distance(s1="asoul", s2="ucasoul"))  # 2
    print(edit_distance(s1="asoul", s2="ucas"))  # 5
    print(edit_distance(s1="asoul", s2="gsovl"))  # 2
