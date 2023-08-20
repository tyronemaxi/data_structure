#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 27.py
Time: 2023/8/20
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        flag = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[flag] = nums[i]
                flag += 1

        print(nums, flag)
        return flag
"""
总结：实际上就是维护一个指针去判断不是目标值的区间，然后去进行原地替换
"""

if __name__ == '__main__':
    nums = [3, 2, 2, 3, 4, 3]
    s = Solution()
    s.removeElement(nums, 3)
