#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 生产消费之间的绑定.py
Time: 2023/8/12
"""
import random
import time
from multiprocessing import Process


class Producer(Process):
    def __init__(self, name, queue):
        super().__init__(name=name)
        self.queue = queue

    def run(self) -> None:
        while True:
            value = random.randint(1, 10)
            item = {"id": self.name, "value": value}
            time.sleep(1)
            self.queue.put(item)
            print(item)


class Consumer(Process):
    def __init__(self, name, queue):
        super().__init__(name=name)
        self.queue = queue

    def run(self) -> None:
        while True:
            item = self.queue.get()
            time.sleep(1)
            print(f"consume: {self.name} consume: {item}")


def manager(queue):

    config = {
        "1": "1",
        "2": "2",
        "3": "1"
    }
    c1 = Consumer(name="1", queue=queue)
    c2 = Consumer(name="2", queue=queue)

    value = queue.get()






if __name__ == '__main__':
    from multiprocessing import Queue
    queue = Queue()
    p1 = Producer(name="1", queue=queue)
    p2 = Producer(name="2", queue=queue)
    p3 = Producer(name="3", queue=queue)


    p1.start()
    c1.start()

    p1.join()
    c1.join()




