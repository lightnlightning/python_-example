#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
# 可写函数说明
def printinfo( arg1, *vartuple ):
   # "打印任何传入的参数"
   print ("输出参数arg1:",arg1)
   print ("输出参数vartuple:",vartuple) #可变参数是个元组
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )
print ("--------------------")
nums = [1, 2, 3]
printinfo( *nums )
print ("--------------------")
printinfo( *[1, 2, 3] )