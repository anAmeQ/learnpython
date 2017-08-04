# -*- coding:utf-8 -*-
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intution
and requires an explanaion
\n\t\twhere there is none.
"""
# 为什么会有空格？
print "---------------"
print poem
print "---------------"

five = 10 - 2 + 3 - 6
print "This should be five:", five
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
# 为什么可以这样，原理是什么

print "With a starting point of :", start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way."
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) # 因为已经返回了函数里的变量，在给定函数参数的前提下，可以用%d表示出来
# %d 只能显示整数，比如0.2只能显示0.

