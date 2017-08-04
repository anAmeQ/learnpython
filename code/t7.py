# -*- coding:utf-8 -*-

def newlist(x, y):
	i = 0
	number = []
	while i < x:
		number.append(i)
		i += y
	print number

newlist(6, 2)



newlist = []
for i in range(0, 6):
	newlist.append(i)
#注意for后面的冒号啊！时刻不能丢！
#while后面的冒号也要注意啊，，，总之注意冒号啊，，，，
	
print newlist