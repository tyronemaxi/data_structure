#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 346.py
Time: 2023/7/14
"""
# 从数据流中移动平均值, 滑动窗口解法
"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
from collections import deque


class MovingAverage:
    def __init__(self, size):
        self.total = 0
        self.size = size
        self.queue = deque()

    def next(self, data):
        if len(self.queue) == self.size:
            self.total -= self.queue.popleft()

        self.queue.append(data)
        self.total += data

        return self.total / min(len(self.queue), self.size)  # 队列不满


if __name__ == '__main__':
    m = MovingAverage(3)
    print(m.next(1))
    print(m.next(2))
    print(m.next(3))
    print(m.next(5))
