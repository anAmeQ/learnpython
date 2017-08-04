#!/usr/bin/python
# -*- coding:utf-8 -*-
ten_things = "Apples Orange Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix it."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff) #是否实现的是从列表转换为字符串的操作？将序列中的元素以指定的字符连接生成一个新的字符串
print 'hhh'.join(stuff[3:5]) 

#复习word[]操作
#为什么在这里要学习python对于函数的解析方式。
