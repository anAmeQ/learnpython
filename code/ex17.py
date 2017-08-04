# -*- coding:utf-8 -*-
from sys import argv
from os.path import exists # exist函数用来验证是否存在

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file) # open(filename)默认使用的是'r'模块
indata = in_file.read()

print "The input file is %d bytes long" % len(indata) # len函数用于？为什么这里用%d？

print "Does the output file exist? %r" % exists(to_file) #如果这里用%s会有什么不一样？没什么不一样。。
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close() 
in_file.close()



# 3.open(to_file, 'w').write(open(from_file).read())
# 5.最后out_file.close()就是退出保存
# 余练习略



