#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/3/5 10:02
# @Author: ZhaoKe
# @File : backtracking.py
# @Software: PyCharm
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            tmp = []
            self._subsets_bt(nums, i, tmp, res)
        return res

    def _subsets_bt(self, nums, st, tmpres, res):
        if st == len(nums):
            return
        newtmp = list()
        for it in tmpres:
            newtmp.append(it)
        newtmp.append(nums[st])
        res.append(newtmp)
        if st == len(nums)-1:
            return
        for i in range(st+1, len(nums)):
            self._subsets_bt(nums, i, newtmp, res)

    def eq_arr(self, arr1, arr2):
        if len(arr1) != len(arr2):
            return False
        for i in range(len(arr1)):
            # print(arr1[i], arr2[i])
            if arr1[i] != arr2[i]:
                return False
        return True

    def _subsets2_bt(self, nums, st, tmpres, res):
        if st == len(nums):
            return
        newtmp = list()
        for it in tmpres:
            newtmp.append(it)
        newtmp.append(nums[st])

        res.append(newtmp)
        if st == len(nums)-1:
            return
        for i in range(st+1, len(nums)):
            self._subsets2_bt(nums, i, newtmp, res)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        indices = range(len(nums))
        res_indices = []
        for i in range(len(indices)):
            tmp = []
            self._subsets2_bt(indices, i, tmp, res_indices)
        # print(res_indices)
        nums.sort()
        res = [[]]
        for item in res_indices:
            tmp_res = []
            for ind in item:
                tmp_res.append(nums[ind])
            flag = True
            for k in range(len(res)-1, -1, -1):
                if self.eq_arr(res[k], tmp_res):
                    flag = False
                    continue
            if flag:
                res.append(tmp_res)
            # res.append(tmp_res)
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.subsets([1]))
    # print(s.subsets([1,2]))
    # print(s.subsets([1,2,3]))
    print(s.subsetsWithDup([4,4,4,1,4]))
    print(s.subsetsWithDup([1,2,2]))
    print(s.subsetsWithDup([0]))