#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 装饰器.py
Time: 2023/8/12
"""
import functools
import time


def timeit(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # 执行方法
        print(result)
        end = time.time()
        print(f"duration time: {(end - start):.3f}")
        return result

    return inner


class Timeit(object):
    def __init__(self, params):
        self.params = params

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)  # 执行方法
            end = time.time()
            print(f"duration time: {(end - start):.3f}")
            return result

        return inner


@Timeit("test")
def method(a):
    time.sleep(a)
    print("running")
    return 1


if __name__ == '__main__':
    method(1)
