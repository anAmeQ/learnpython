# -*- coding:utf-8 -*-
#写没一行代码你都必须明白其作用是什么，要学会控制，而不是乱用技能。
#其实就是要让计算机学会思考啊。
from sys import exit
#在这里引入exit函数

def gold_room():
	print "This room is full of gold.	How much do you take?"
	
	next = raw_input("> ") #容易出现bug，如何修改？
	while not next.isdigit():
		print "Please type in a number."
		next = raw_input("> ")
		
	if "0" in next or "1" in next:
		how_much = int(next)
#如果在指定序列中找到值则返回True，否则返回False。
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

#此段代码很有意思！！！！！好好学！！！！！！！！！！	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear looks at you then slapes your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True #开关
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()




