#!/usr/bin/python3
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

#为了触发异常,禁用testfile文件的写权限
#在终端执行以下命令
#chmod -w testfile
#还原写入权限
#chmod +w testfile

