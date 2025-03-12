#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/3/5 11:46
# @Author: ZhaoKe
# @File : qst_number.py
# @Software: PyCharm
import math
from typing import List


class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        sq = int(math.sqrt(n))
        if sq * sq != n:
            return False
        for i in range(2, sq):
            if n % i == 0:
                return False
        return True

    def divisorSubstrings(self, num: int, k: int) -> int:
        N = 0
        tmp = num
        while tmp > 0:
            N += 1
            tmp //= 10
        # print(N)
        tmp = str(num)
        res = 0
        for i in range(N - k + 1):
            # print(tmp[i:i+k])
            tmpsub = int(tmp[i:i + k])
            if tmpsub == 0:
                continue
            if num % tmpsub == 0:
                res += 1
        return res

    def evenOddBit(self, n: int) -> List[int]:
        res = [0, 0]
        flag = True
        while n > 0:
            if n & 1:
                if flag:
                    res[0] += 1
                else:
                    res[1] += 1
            flag = not flag
            n >>= 1
        return res

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        mp = {}


if __name__ == '__main__':
    s = Solution()
    print(s.evenOddBit(50))
    print(s.evenOddBit(64))
    print(s.evenOddBit(2))
    # print(s.divisorSubstrings(240, 2))
    # print(s.divisorSubstrings(430043, 2))
    # print(s.isThree(1))
    # print(s.isThree(2))
    # print(s.isThree(3))
    # print(s.isThree(4))
    # print(s.isThree(6))
    # print(s.isThree(8))
    # print(s.isThree(49))
