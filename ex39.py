#create a mapping of atate to abbrevation

states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
	}

# create a basic sets of some cities and states	in them
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
	}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
#print out some cities
print "-" * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']	

#print some states
print "-" * 10
print "Michigan's abbrevation is:", states['Michigan'] 
print "Florida's abbrevation is:", states['Florida']

#di it by using the state then cities dict
print "-" *10
print "Michigan has: ",cities [states['Michigan']]
print "Florida has: ",cities [states['Florida']]

#print every state abbrevation
print "-" * 10
for state, abbrev in states.items():
	print "%s is abbrevated %s" % (state, abbrev)

#print every city in state
print "-" * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

print "-" * 10
for state ,abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print "-" * 10
state = states.get('New York', None)
print state	
if not state:
	print "Sorry, no Texas."

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is : %s" % city	
