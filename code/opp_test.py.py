#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
		   "class %%%(%%%):":
		   "Make a class named %%% is a %%%.",
		   "class %%%(object):\n\tdef __init__(self, ***):":
		   "class has-a __init__ that takes self and *** parameters.",
		   "class %%%(object):\n\tdef ***(self, @@@)":
		   "class has-a function named *** that takes self and @@@ parameters.",
		   "*** = %%%()":
		   "Set *** to an instance of class %%%.",
		   "***.***(@@@)":
		   "From *** get the *** function and call it with parameters self, @@@.",
		   "***.*** = '***'":
		   "From *** get the *** attribute and set is to '***'."
}
		  
#do they want to drill phrases first
PHRASES_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASES_FIRST = True
	
#load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())
#这里是realines不是readline，注意区别
#strip在这里去掉了\n
	
def covert(snippet, phrases):
	class_names = [w.capitalize() for w in
				   random.sample(WORDS, snippet.count("%%%"))]
	#首字母大写

	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		
	for sentence in snippet, phrase:
		result = sentence[:] #这里并没有列表，只涉及字符串，列表切片有何意义？
		
		#fake class name
		for word in class_names:
			result = result.replace("%%%", word, 1)
			
		#fake other name
		for word in other_names:
			result = result.replace("***", word, 1)
			
		#fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
		
	return results
	
#keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = covert(snippet, phrase) #把一个列表中的两个元素分别赋予两个变量，神奇
			
			if PHRASES_FIRST:
				question, answer = answer, question
				
			print question
			
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
			
except EOFError:
	print "\nBye"
	