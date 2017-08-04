# -*- coding:utf-8 -*-
the_count = {1, 2, 3, 4}
fruits = {'apples', 'oranges', 'pears', 'apricots'} #字符串要用引号引出来
change = {1, 'pennies', 2, 'dimes', 3, 'quarters'}

#this first kind of for-loop goes through a list
for number in the_count:
	print "This is count for %d" % number
	
#same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r." % i
	
#we can also build lists, first start with an empty one
element = []
#要先添加数字必须先建立list。

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	element.append(i)
#range函数的用法？range(5)? range(0, 5)?
#append函数与extend函数的区别？详细见t5.py
	
#now we can print them out too
for i in element:
	print "Element was: %d" % i
	

	
