from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "if you don't want that,hit CTRL -C(^C)."
print "If you do want, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
targett = open(filename)
print "Truncating the file. Goodbye!"
target.truncate()

#abc = open(filename)
print targett.read()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")

line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I 'm going to write these to the file."

target.write(line1+"\n"+line2+"\n"+line3+"\n")
# target.write("\n")
# #print targett.read()

# target.write(line2)
# target.write("\n")
# #print targett.read()

# target.write(line3)
# target.write("\n")
#print targett.read()

print "And finally, we close it."
target.close()

targett = open(filename)
print targett.read()
targett.close()