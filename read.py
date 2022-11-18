#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
# 打开一个文件
fo = open("foo.txt", "r+")

# fo.read(10) 如果没有传入，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾
str = fo.read(10)
print ("读取的字符串是 : ", str)

# 关闭打开的文件
fo.close()

