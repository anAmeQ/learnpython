element = []
element.extend([1, 2, 3, 4, 5])
for i in element:
	print "Element was %d." % i
	
element.append(6)
print element

#比较下append([1, 2, 3])与extend([1, 2, 3])的区别