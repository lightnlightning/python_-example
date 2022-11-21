#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#创建了一个类，基类为RuntimeError
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
try:
    n = Networkerror("Bad hostname")
    raise n
except Networkerror as e:
    print(e.args) 
