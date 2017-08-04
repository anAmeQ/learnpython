# -*- coding:utf-8 -*-
people = 20
cats = 30
dogs = 15

if people < cats:
   print "Too many cats!The world is doomed!"
#条件语句的下一行不一定用tab缩进
#条件结尾一定要加：
   
if people > cats:
   print "Not many cats! The world is saved!"
   
if people < dogs:
   print "The world is drooled on!"
   
if people > dogs:
   print "The world is dry!"
   
dogs += 5

if people >= dogs:
   print "People are greater than or equal to dogs."
   
if people <= dogs:
   print "People are less than or equal to dogs."
   
if people == dogs:
   print "People are dogs."
