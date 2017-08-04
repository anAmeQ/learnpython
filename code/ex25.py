# -*- coding:utf-8 -*-
def break_words(stuff):
	"""This function will break up words for us"""
	words = stuff.split(' ')
	return words
# 三引号里的内容为该函数的解释文档

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
#如果直接用sorted(words)呢？
	
def print_first_word(words):
	"""Print the first word after popping it off."""
	word = words.pop(0)
	return word
	
def print_last_word(words):
	"""Print the last word after popping it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sorted(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words =sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

# sorted, split, pop(), pop(0), pop(-1)都是什么意思？