#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 26.py
Time: 2023/8/20
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        p1, p2 = 0, 1
        while p2 < n:
            if nums[p2] != nums[p1]:
                nums[p1+1] = nums[p2]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        print(nums, p1)
        return p1+1


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3, 4]
    s = Solution()
    print(s.removeDuplicates(nums))


