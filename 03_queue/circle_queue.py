#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: circle_queue.py
Time: 2023/6/30
"""


class CircleQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity + 1  # 队列为满时，尾指针额外的位置
        self.__queue = []
        self._head = 0
        self._tail = 0

    def enqueue(self, data):
        if self.is_full():
            return False
        self.__queue.append(data)
        self._tail = (self._tail + 1) % self.capacity
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.__queue[self._head]
        self._head = (self._head + 1) % self.capacity
        return data

    def is_full(self):
        return (self._tail+1) % self.capacity == self._head

    def is_empty(self):
        return self._head == self._tail

    def get_queue(self):
        return self.__queue

    def __str__(self):
        output = " | ".join(map(str, self.__queue[self._head: self._tail]))
        return output


if __name__ == '__main__':
    queue = CircleQueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue)
    print(queue.get_queue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)
