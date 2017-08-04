# -*- coding:utf-8 -*-
name = '猴猴'
age = 35 # not a lie
height = 74 # not inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name # 使用%s与%r在显示中文字符时有显著不同
print "He's %r inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth 

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
	
	

# 1.已改
# 2-4略，3中提出的格式化字符在后面有涉及到
