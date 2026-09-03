#Arithematic operator
a = 10
b = 3 


print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)


#Simple calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#Students marks calculator 

name = input("enter student name: ")

m1 = int(input("Enter Python marks: "))
m2 = int(input("Enter Java marks: "))
m3 = int(input("Enter SQL marks: "))

total = m1+m2+m3
average = total/3

print("\n-----Student Report -----")
print("Name:", name)
print("Total Marks:",total)
print("Average Marks:", average)

#shopping bill calculator 

price1 = float(input("Enter product 1 price: "))
price2 = float(input("Enter product 2 price: "))
price3 = float(input("Enter product 3 price: "))

total_bill = price1 + price2 + price3

discount = total * 0.10 
final_amount = total - discount 

print("Discount:", discount)
print("Final Amount to be paid:", final_amount)

#assignment operator
x = 10

x +=5
print(x)

x -=2
print(x)

x *=3
print(x)

#bank balance 
balance = 10000

deposit = 5000
balance += deposit 

print("After deposit:", balance)

withdraw = 2000
balance -= withdraw 

print("After withdrawal:", balance)

#comparison operator 
a = 10 
b = 20 

print(a ==b)  # False
print(a != b)  # True
print(a < b)   # True
print(a > b)   # False
print(a <= b)  # True
print(a >= b)  # False

#age eligibility check
age = int(input("Enter your age: "))

print("Eligible:",age >=18)

#pass or fail checker 
marks = int(input("Enter marks:"))

print("passed:", marks >=40)


#login validation 
username = input("Enter username: ")
password = input("Enter password: ")
correct_username = "admin"
correct_password = "1234"

print(username == correct_username )
print(password == correct_password)




