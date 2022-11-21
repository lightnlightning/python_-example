#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#类的方法与普通的函数只有一个特别的区别
#必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
class Test1:
    def prt(self):
        print(self)
#self 代表的是类的实例，代表当前对象的地址，
#self.__class__ 则指向类
        print(self.__class__)

t1 = Test1()
t1.prt()

#self 不是 python 关键字，我们把他换成 runoob 也是可以
class Test2:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
 
t2 = Test2()
t2.prt()
