#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
def ChangeInt( a ):
    print(a)
    a = 10
    print(a)
 
b = 2
ChangeInt(b)
print(b)  # 结果是 2

def ChangeInt( a ):
    print(a)
    a = "inside str"
    print(a)
 
b = "outside str"
ChangeInt(b)
print(b)  # 结果是 2
