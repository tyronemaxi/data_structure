#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 单例.py
Time: 2023/8/12
"""


class Singleton(object):
    _instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
            return cls._instance

        return cls._instance


if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    c = Singleton()
    print(id(a))
    print(id(b))
    print(id(c))
