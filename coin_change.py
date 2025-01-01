#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2024/12/25 9:49
# @Author: ZhaoKe
# @File : coin_change.py
# @Software: PyCharm
"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
"""
from typing import List


class Solution:
    # reference: [Official answer of leetcode](https://leetcode.cn/problems/coin-change/solutions/132979/322-ling-qian-dui-huan-by-leetcode-solution/)
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dynamic programming(from bottom to top)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

    def coinChange_ms(self, coins: List[int], amount: int) -> int:
        mem = [float('inf')] * (amount + 1)
        mem[0] = 0

        def dp(rem) -> int:
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if 0 <= res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1:
            return 0
        return dp(amount)


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([1, 2, 3], 6))
