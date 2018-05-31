numbers = []
def fun(a):
	# i = 0
	# while i < 6:
	for i in range(0, 6):
		print "At the top i is %d" % i 
		numbers.append(i)
		i = i + a;
		print "Numbers now: ",numbers
		print "At the bottom i is %d" % i

fun(2)
print "The numbers: "

for num in numbers:
	print num ,