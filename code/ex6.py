# -*- coding:utf-8 -*-
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x 
print "I also said: '%s'." % y

hilarious = False 
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

print w + e



# 1-3略
# 4中python允许变量间的运算。此处变量 = 特定字符串，从而此处看到字符串合并后得到一个更长字符串。