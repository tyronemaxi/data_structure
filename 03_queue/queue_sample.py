#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: queue_sample.py
Time: 2023/6/30
"""


class Queue:
    """
    基于数组实现顺序队列
    """
    def __init__(self, capacity: int):
        self.__queue = []
        self._capacity = capacity
        self._head = 0
        self._tail =0

    def enqueue(self, data):
        if self._tail == self._capacity:
            if self._head == 0:  # 队列已满
                return False
            else:
                # 数据搬移
                for i in range(0, self._tail - self._head):
                    self.__queue[i] = self.__queue[i+self._head]

                self._tail = self._tail - self._head
                self._head = 0

        self.__queue.insert(self._tail, data)
        self._tail += 1
        return True

    def dequeue(self):
        if self._tail != self._head:
            data = self.__queue[self._head]
            self._head += 1
            return data
        return None

    def head(self):
        return self.__queue[self._head]

    def tail(self):
        return self.__queue[self._tail]

    def __len__(self):
        return len(self.__queue)

    def __str__(self):
        output = " | ".join(map(str, self.__queue[self._head: self._tail]))
        return output


if __name__ == '__main__':
    queue = Queue(10)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    queue.dequeue()
    queue.dequeue()
    print(queue)
