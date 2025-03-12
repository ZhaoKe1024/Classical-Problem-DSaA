#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/3/6 8:47
# @Author: ZhaoKe
# @File : qst_array.py
# @Software: PyCharm
from collections import defaultdict
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

    def count_bit(self, num):
        res = 0
        while num > 0:
            if num & 1:
                res += 1
            num >>= 1
        return res

    def dec2bit(self, num):
        res = ""
        while num > 0:
            if num & 1:
                res += "1"
            else:
                res += "0"
            num >>= 1
        return res

    def beautifulSubsets_1(self, nums: List[int], k: int) -> int:
        N = len(nums)
        groups = []
        for i in range(N):
            for j in range(N):
                if abs(nums[i] - nums[j]) == k:
                    groups.append((1 << i) | (1 << j))
        cnt = N
        for mask in range(1, 1 << N):
            if self.count_bit(mask) < 2:
                continue
            for x in groups:
                if mask & x == x:
                    break
            else:
                print(self.dec2bit(mask))
                cnt += 1
        return cnt

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = defaultdict(dict)
        for num in nums:
            mod = num % k
            groups[mod][num] = groups[mod].get(num, 0) + 1
        ans = 1
        print(groups.values())
        for g in groups.values():
            print(g.keys())
            sorted_keys = sorted(g.keys())
            print(sorted_keys)
            m = len(sorted_keys)
            f = [[0] * 2 for _ in range(m)]
            f[0][0] = 1
            f[0][1] = (1 << g[sorted_keys[0]]) - 1
            for i in range(1, m):
                f[i][0] = f[i - 1][0] + f[i - 1][1]
                if sorted_keys[i] - sorted_keys[i - 1] == k:
                    f[i][1] = f[i - 1][0] * ((1 << g[sorted_keys[i]]) - 1)
                else:
                    f[i][1] = (f[i - 1][0] + f[i - 1][1]) * ((1 << g[sorted_keys[i]]) - 1)
            ans *= f[m - 1][0] + f[m - 1][1]
        return ans - 1

    def maximumBeauty_fail(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        kvs = []
        tmparr, cur = [items[0][1]], items[0][0]
        for i in range(1, len(items)):
            if items[i][0] != cur:
                tmparr.sort()
                kvs.append([cur] + tmparr)

                cur = items[i][0]
                tmparr = [items[i][1]]
            else:
                tmparr.append(items[i][1])
        tmparr.sort()
        kvs.append([cur] + tmparr)
        kvs.sort(key=lambda x: x[0])
        # for k in kvs:
        #     print(k)
        # print(items)
        res = []
        for q in queries:
            #     res.append(kvs[q][-1])
            # return res
            if q < kvs[0][0]:
                res.append(0)
                continue
            if q >= kvs[-1][0]:
                res.append(kvs[-1][-1])
                continue
            l, r = 0, len(kvs) - 1
            mid = (1 + r) // 2
            while l < r:
                # print(l, r, res, kvs)
                # if l == r:
                #     res.append(kvs[l][-1])
                #     break
                if l + 1 == r:
                    if kvs[l][0] < q < kvs[r][0] or kvs[l][0] == q:
                        res.append(kvs[l][-1])
                        break
                    elif kvs[r][0] == q:
                        res.append(kvs[r][-1])
                        break
                if q == kvs[mid][0]:
                    res.append(kvs[mid][-1])
                    break
                elif q > kvs[mid][0]:
                    l = mid
                else:
                    r = mid
                if l == r:
                    res.append(kvs[l][-1])
                    break
                mid = (l + r) // 2
        return res

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # 将物品按价格升序排序
        items.sort(key=lambda x: x[0])
        N = len(items)
        # 按定义修改美丽值
        for i in range(1, N):
            items[i][1] = max(items[i][1], items[i - 1][1])
        res = []
        for q in queries:
            l, r = 0, N
            while l < r:
                mid = (l + r) // 2
                if items[mid][0] > q:
                    r = mid
                else:
                    l = mid + 1
            if l == 0:
                res.append(0)
                continue
            else:
                res.append(items[l - 1][1])
        return res

    def sumOfBeauties(self, nums: List[int]) -> int:
        N = len(nums)
        pre, post = [0] * N, [100001] * N
        minv, maxv = 0, 100001
        for i in range(N):
            if nums[i] > minv:
                minv = nums[i]
            if nums[N - i - 1] < maxv:
                maxv = nums[N - i - 1]
            pre[i] = minv
            post[N - i - 1] = maxv
        # print(pre)
        # print(post)
        res = 0
        for i in range(1, N - 1):
            # print(nums[i])
            if pre[i - 1] < nums[i] < post[i + 1]:
                res += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.sumOfBeauties([1, 2, 3]))
    print(s.sumOfBeauties([2, 4, 6, 4]))
    print(s.sumOfBeauties([3, 2, 1]))
    # print(s.maximumBeauty(items=[[1, 2], [3, 2], [2, 4], [5, 6], [3, 5], [5, 2]], queries=[1, 2, 3, 4, 5, 6]))
    # for i in range(2, 9):
    #     print(s.count_bit(i))
    # print(s.beautifulSubsets([2, 4, 6], k=2))
    # print(s.beautifulSubsets([2, 4, 7, 8, 9], k=2))
    # print(subarraySum([1], 0))
    # print(subarraySum([1, 1, 1], 2))
    # print(subarraySum([1, 2, 3], 3))
    # print(beautifulSubarrays([4, 3, 1, 2, 4]))
    # print(s.getMaximumXor([0, 1, 1, 3], 2))
    # print(s.getMaximumXor([2, 3, 4, 7], 3))
    # print(s.getMaximumXor([0, 1, 2, 2, 5, 7], 3))
