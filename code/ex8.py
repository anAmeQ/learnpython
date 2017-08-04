# -*- coding:utf-8 -*-
formatter = "%r %r %r %r" # 使用%s于%r的区别 

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four") # 使用双引号与单引号的区别？
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
	"That you could type up right.",
	"But it did't sing.",
	"So I said goodnight"
)



# 1略。
# 2中python认为前后两个双引号是字符串的边界，字符串中的单引号不会作为边界识别出来。