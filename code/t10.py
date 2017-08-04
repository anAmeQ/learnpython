#!/usr/bin/python
# -*- coding:utf-8 -*-
from sys import argv
import random
script, filename = argv
list = []
WORDS = open(filename)
WORDS.seek(0)

for word in WORDS.readlines():
	list.append(word.strip())

	
class_names = [w.capitalize() for w in
			   random.sample(list, 2)]

print class_names