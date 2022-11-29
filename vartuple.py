#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
# 可写函数说明
def printinfo( arg1, **kw ):
   # "打印任何传入的参数"
   print ("输出参数arg1:",arg1)
   print ("输出参数vartuple:",kw) #可变参数是个字典
   for var in kw:
      print (var,kw[var])
   return
 
# 调用printinfo 函数
printinfo( 10 )
print ("----------------")
printinfo( 70, city='Beijing', job='Engineer' )
print ("----------------")
extra = {'city': 'Beijing', 'job': 'Engineer'}
printinfo( 70, **extra )
print ("----------------")
printinfo( 30, **{'city': 'Beijing', 'job': 'Engineer'} )
