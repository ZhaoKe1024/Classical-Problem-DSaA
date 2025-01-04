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
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    for item in dp:
        print(item)
    return dp[-1][-1]


def longest_common_substring(s1: str, s2: str) -> str:
    L1, L2 = len(s1), len(s2)
    if L1 == 0 or L2 == 0:
        return ""
    dpt = [[0 for _ in range(L2 + 2)] for _ in range(L1 + 1)]
    res = ""
    for i in range(1, L1 + 1):
        flag = True
        for j in range(1, L2 + 1):
            dpt[i][j] = max(dpt[i - 1][j], dpt[i][j - 1], dpt[i - 1][j - 1])
            if s1[i - 1] == s2[j - 1]:
                dpt[i][j] += 1
                if flag:
                    res += s1[i-1]
                    flag = False
    print("----------------------")
    for item in dpt:
        print(item)
    print("-----------------------")
    return res


if __name__ == '__main__':
    print(longest_common_substring(s1="UCAS", s2="UCASOUL"))
    print(longest_common_substring(s1="VASOFUL", s2="ASIROUL"))
    # print(edit_distance(s1="", s2="code"))  # 4
    # print(edit_distance(s1="leet", s2=""))  # 4
    # print(edit_distance(s1="asoul", s2="aoul"))  # 1
    # print(edit_distance(s1="asoul", s2="soul"))  # 1
    # print(edit_distance(s1="asoul", s2="asou"))  # 1
    # print(edit_distance(s1="asoul", s2="ucasoul"))  # 2
    # print(edit_distance(s1="asoul", s2="ucas"))  # 5
    # print(edit_distance(s1="asoul", s2="gsovl"))  # 2
