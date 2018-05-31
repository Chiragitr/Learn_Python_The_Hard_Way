the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# this first kind of for-loop goes through a list
#i=5
for number in the_count:
	#print i
	print "This is count %d" % number
	#i += 1
for fruit in fruits:
	print "A fruit of type: %s " % fruit

#also we can go through mixed lists too 
#notice we have to use %r since we don't know what's in it

for i in change:
	print "I got %r" % i

#we can also build lists, first start with an empty one
elements = []

for i in range(0, 6):
	#y = int(raw_input("enter the number %d:" % i))
	print "Adding %d to the list." % i
	elements.append(i)
#now we can print them out too
for x in elements:
	print "ELement was: %d" % x