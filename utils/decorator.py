#-*- coding:utf-8 -*-
from functools import wraps

def coroutine(func):
    """协程装饰器"""
    @wraps(func)
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        g.next()
        return g
    return start