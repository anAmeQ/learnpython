#!/usr/bin/python
# -*- coding:utf-8 -*-

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

#用于在实例化时定义类的属性
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
	
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

	