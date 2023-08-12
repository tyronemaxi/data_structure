#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 基于多进程实现生产者消费者模式.py
Time: 2023/8/12
"""
import multiprocessing
import random
import time
from multiprocessing import Queue



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
    queue = Queue(10)
    p1 = multiprocessing.Process(target=producer, args=(queue,))
    p2 = multiprocessing.Process(target=producer, args=(queue,))
    c1 = multiprocessing.Process(target=consumer, args=(queue,))

    p1.start()
    c1.start()

    p1.join()
    c1.join()



