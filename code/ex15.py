# -*- coding:utf-8 -*-
from sys import argv # 从系统中调取argv模块（module或者library），argv即在命令行运行python时传递给python脚本的参数变量（可包含多个）

script, filename = argv #将argv参数变量解包，赋值于左边的变量

txt = open(filename) # open是一个打开文件的函数，返回的并不是文件内容而是file object

print "Here's your file %r." % filename 
print txt.read() # txt本身可以支持的命令，在这里通过.read执行读取文件的命令

print "Type the filename again:"
file_again = raw_input("> ") # 还记得上一节promt吗？

txt_again = open(file_again)

print txt_again.read()



# 1见上，5个人认为使用raw_input获取文件名称更具交互性，剩余练习略