# -*- coding:utf-8 -*-
i = 0
numbers = []
# 注意在循环前要把该定义的定义出来

#注意while后面的冒号啊！不能丢！
while i < 6:
	print "At the top i is %d." % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num

# 如何改写？详见t7.py。
	
	
