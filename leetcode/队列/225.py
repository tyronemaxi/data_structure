#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 225.py
Time: 2023/7/14
"""
# https://leetcode.cn/problems/implement-stack-using-queues/
from collections import deque


class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()


    def push(self, x: int) -> None:
        # 入栈
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        self.queue1, self.queue2 = self.queue2, self.queue1


    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()