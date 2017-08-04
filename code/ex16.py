# -*- coding:utf-8 -*-
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename,'w')

print "Truncating the file.  Goodbye!"

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ") 
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."
 
target.write(line1 + "\n" + line2 + "\n" + line3) # 改写后的与原版有什么不同

print "And finally, we close it."
target.close()



# 1、2略，3.target.write(line1 + "\n" + line2 + "\n" + line3)
# 4.open为了安全
# 5.在'w'模式下文件内容已被清空，没必要再truncate