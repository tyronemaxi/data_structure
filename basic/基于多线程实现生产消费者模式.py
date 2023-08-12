#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 基于多线程实现生产消费者模式.py
Time: 2023/8/12
"""
import time
import random
import threading

from queue import Queue


def producer(queue):
    """
    生产者
    :param consumer:
    :return:
    """
    while True:
        value = random.randint(1, 10)
        print(f"produce a value: {value}")
        queue.put(value)
        time.sleep(1)


def consumer(queue: Queue):
    time.sleep(1)
    while True:
        if queue:
            value = queue.get()
            print(f"consume a value: {value}")


if __name__ == '__main__':
    queue = Queue()
    t1 = threading.Thread(target=producer, args=(queue,))
    t2 = threading.Thread(target=consumer, args=(queue,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
