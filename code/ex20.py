# -*- coding:utf-8 -*-
from sys import argv
script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)
# f.seek() 如何运行？

def print_a_line(line_count, f):
	print line_count, f.readline()
# f.readline()如何运行？读完一行是否会空行？为什么会空行？print末尾加逗号还会空行吗？

current_file = open(input_file)

print "First, let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape"

rewind(current_file)

print "Let's print three lines:"

current_line = 1 
print_a_line(current_line, current_file)

current_line += 1 # +=这是什么意思？
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
# 注意变量运算，得出的结果跟你想的一样吗？



# 附加练习已在代码中的注释中体现