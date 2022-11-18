#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
# 打开一个文件
fo = open("foo.txt", "w")

# 把字符串写入文件
fo.write( "www.runoob.com!\nVery good site!\n")

# 关闭打开的文件
fo.close()
