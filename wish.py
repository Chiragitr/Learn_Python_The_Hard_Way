from sys import argv

script= argv
print "Enter your present age: "
age = int(raw_input())
print "------------------------CAR-INFO-----------------------------"
car_name = raw_input("Enter Car Name:?")
car_cost = int(raw_input("Enter Car Cost:?"))
c_age = int(raw_input("Max Age To Buy:?"))
print "I want: %r\nIts Cost: %r\nAt a age of: %r\nDuration remaining: %r\n" %(car_name, car_cost, c_age, c_age - age)
print "------------------------HOUSE--------------------------------" 
# h_place = "Indore"
# h_cost = "10000000"
# h_age = 30
h_place = raw_input("Enter Place:?")
h_cost = int(raw_input("Enter House Cost:?"))
h_age = int(raw_input("Max Age To Buy:?"))

print "--------------------COTTON-INDUSTRY---------------------------" 
place = raw_input("Enter Place:?")
I_cost = int(raw_input("Enter Industry Cost:?"))
I_age = int(raw_input("Max Age To Buy:?"))

print "------------------------EUROPE TOUR--------------------------------" 
W_cost = int(raw_input("Enter Cost:?"))
W_age = int(raw_input("Max Age To FULFILL:?"))

total_cost = car_cost + h_cost + I_cost + W_age 
T_achieve = int(raw_input("MAX AGE TO ACHIEVE ALL WISHES:?"))
age_diff = T_achieve - age
months = age_diff * 12
print "To fullfill your wishes upto max age you have to earn %r per year from now" %(total_cost / age_diff)
print "To fullfill your wishes upto max age you have to earn %r per month from now" %(total_cost / months)

avg_age = (c_age + h_age + I_age + W_age)/4
age_diff_avg = avg_age - age

print "To fullfill your wishes on average you have to earn %r per year from now "%(total_cost / age_diff_avg)
