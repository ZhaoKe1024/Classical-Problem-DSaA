#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/3/6 8:47
# @Author: ZhaoKe
# @File : qst_array.py
# @Software: PyCharm
from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    """560 Given an array of integers nums and an integer k,
    return the total number of subarrays whose sum equals to k.
    A subarray is a contiguous non-empty sequence of elements within an array."""
    pre, cnt = 0, 0
    mp = {0: 1}
    for i in range(len(nums)):
        pre += nums[i]
        if pre - k in mp:
            cnt += mp[pre - k]
        if pre in mp:
            mp[pre] += 1
        else:
            mp[pre] = 1
    return cnt
    # cnt = 0
    # for i in range(len(nums)):
    #     sum = 0
    #     for j in range(i, (len(nums))):
    #         sum += nums[j]
    #         if sum == k:
    #             cnt += 1
    # return cnt


def beautifulSubarrays(nums: List[int]) -> int:
    """2588. Count the Number of Beautiful Subarrays.
    We can use XOR to solve this problem"""
    pre, cnt = 0, 0
    mp = {0: 1}
    for i in range(len(nums)):
        pre ^= nums[i]
        if pre in mp:
            cnt += mp[pre]
            mp[pre] += 1
        else:
            mp[pre] = 1
    return cnt


class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        """1829. Maximum XOR for Each Query"""
        n = len(nums)
        mask = (1 << maximumBit) - 1
        xorsum = nums[0]
        for i in range(1, len(nums)):
            xorsum ^= nums[i]
        # k = xorsum^mask
        ans = list()
        for i in range(n - 1, -1, -1):
            ans.append(xorsum ^ mask)
            xorsum ^= nums[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(subarraySum([1], 0))
    # print(subarraySum([1, 1, 1], 2))
    # print(subarraySum([1, 2, 3], 3))
    # print(beautifulSubarrays([4, 3, 1, 2, 4]))
    print(s.getMaximumXor([0, 1, 1, 3], 2))
    print(s.getMaximumXor([2, 3, 4, 7], 3))
    print(s.getMaximumXor([0, 1, 2, 2, 5, 7], 3))
