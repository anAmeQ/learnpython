# creat a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'


#creat a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities                                                                                                                                                                                     
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
#添加item到字典中

#print out some cities
print '-' * 10
print "NY state has:", cities['NY']
print "OR State has:", cities['OR']
#访问字典的item

#print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']


#do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
#嵌套访问

#print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
#字典的items函数，注意得到了两个值，并在for循环开始时赋予两个变量state、abbrev
#注意item后面的括号啊！！！！！！！

#print evert city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev,city)
	
#now do both at the same time	
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviation %s and has the city %s" % (
	state, abbrev, cities[abbrev])
#注意最后一行，由于abbrev在for循环中已经定义，所以我们可以通过字典cities得到对应的值
	
print '-' * 10
#safely get a abbreviation by state that might not be there
state = states.get('Texas', None)
#用字典的get函数创建新item。
#注意None的用法哦

if not state:
	print "Sorry, no Texas."
#not state为什么得到的值是True呢？
	
#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city


