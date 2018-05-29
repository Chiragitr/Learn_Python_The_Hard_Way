from sys import argv	

script, first, second, third = argv		

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
x = raw_input("what is your age?")
print "your age is %r and input through command line are %r %r %r" %(x, first, second, third)
#comment added