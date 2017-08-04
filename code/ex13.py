# -*- coding:utf-8 -*-
from sys import argv

script, first, second, third = argv 

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third



# 1.need more than 3 values to unpack. 给的参数不够还需要增加
# 2.script, first, second = argv      script, first, second, third, fourth = argv
# 3.中间加一行 x = raw_input()