#!\usr\bin\python
# -*- coding:utf-8 -*-
from sys import exit
def kick(time):

	if time < 5:
		print "You can't find his soul."
	else:
		print "We can get closer."

print "Show me your fate."
x = int(raw_input('> '))
kick(x)