#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 

def now():
    print("hello now")

f=now  #函数也是一个对象,通过变量也能调用该函数
f()

print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def now_decorator():
    print("hello now_decorator")

