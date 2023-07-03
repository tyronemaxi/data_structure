#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 179_largest-number.py
Time: 2023/7/3
"""
"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
# https://leetcode.cn/problems/largest-number/
"""
from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = "".join(sorted(map(str, nums), key=cmp_to_key(lambda x,y:((x+y) < (y+x)) - ((x+y) > (y+x)))))
        return nums if nums[0] != '0' else '0'


if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber(nums=[2, 190, 9, 20]))
