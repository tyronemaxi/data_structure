#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 56_merge_intervals.py
Time: 2023/7/3
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 使用区间的左端点进行排序
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:  # 判断当前区间不在上一个区间中
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
