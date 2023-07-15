#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 155.py
Time: 2023/7/15
"""
import math


# https://leetcode.cn/problems/min-stack/
class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = [math.inf]  # 正无穷大

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._min_stack.append(min(val, self._min_stack[-1]))

    def pop(self) -> None:
        if self._stack:
            self._min_stack.pop()
            self._stack.pop(-1)

    def top(self) -> int:
        if self._stack:
            return self._stack[-1]

    def getMin(self) -> int:
        # 常数时间
        return self._min_stack[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    _li = [1,23,3,1,0,-1]
    print(min(_li))