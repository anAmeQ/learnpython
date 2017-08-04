# -*- coding:utf-8 -*-
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
# return函数的功能，如果不使用return函数还可以作为变量被识别吗？
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq) #为什么可以识别十进制整数？因为return函数。

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# 有点意思啊。。

print "That becomes: ", what, "Can you do it by hand?"
