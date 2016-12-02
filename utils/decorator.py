#-*- coding:utf-8 -*-
from functools import wraps

def coroutine(func):
    """协程装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        g.next()
        return g
    return wrapper