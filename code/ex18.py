# -*- coding:utf-8 -*-
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
#python是一种对缩进非常敏感的语言，最常见的情况是tab和空格的混用会导致错误，或者缩进不对，而这是用肉眼无法分别的。	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no argument
def print_none():
	print "I got nothing'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
