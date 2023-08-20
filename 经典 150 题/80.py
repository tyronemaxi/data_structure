#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 80.py
Time: 2023/8/20
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def retain(k):
            u = 0
            for i in range(len(nums)):
                if u < k or nums[u-k] != nums[i]:
                    nums[u] = nums[i]
                    u += 1

            print(nums, u)
            return u

        return retain(2)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3, 4]
    s = Solution()
    s.removeDuplicates(nums)


