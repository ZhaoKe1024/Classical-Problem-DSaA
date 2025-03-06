#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/3/5 11:46
# @Author: ZhaoKe
# @File : qst_number.py
# @Software: PyCharm
import math


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

if __name__ == '__main__':
    s = Solution()
    print(s.isThree(1))
    print(s.isThree(2))
    print(s.isThree(3))
    print(s.isThree(4))
    print(s.isThree(6))
    print(s.isThree(8))
    print(s.isThree(49))
