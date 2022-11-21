#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        print(e)
        # 可以选择把当前的异常又抛出bar(),执行以下代码raise
        #raise

bar()

