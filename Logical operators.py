# AND 

age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
else:
    print("Not eligible")

#OR

age = 16
student = True

if age >= 18 or student:
    print("Eligible for discount")
else:
    print("Not eligible")

#NOT

age = 15
if not age >= 18:
    print("Not eligible")
print(age >= 18 and citizen)
#logical operators 

age = 25 
citizen = True 

print(age >= 18 and citizen == True )

age = 16 
citizen = True 

print(age >=18 and citizen == True)

#or 

has_card = False
has_cash = True

print(has_card or has_cash)


#not 
is_logged_in = True 

print(not is_logged_in)

#atm eligibility checker

balance = 10000
withdraw = 5000

print(withdraw >0 and withdraw <= balance)

#Student scholarship eligibility checker 

marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance: "))

eligible = marks >= 85 and attendance >=75

print("Scholarship Eligible:", eligible)















