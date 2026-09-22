#check the number is even (or) odd

num = int(input("Enter a number: "))

if num % 2 ==0 :
    print(f"{num}is even")
else:
    print(f"{num}is odd")


num = int(input("enter a number:"))
if num % 2 ==0:
    print(f"{num}is even")
elif num % 2 == 0 :
    print(f"{num}is odd")
else:
    print("Invalid input")    
          
# Program to check Pass or Fail

marks = int(input("Enter your marks: "))

if marks >= 40:   # condition for pass
    print(" You Passed!")
else:             # condition for fail
    print(" You Failed!")

 # Program to check temperature warning

temperature = float(input("Enter the temperature in °C: "))

if temperature > 40:
    print(" High Temperature Warning!.")
else:
    print(" Temperature is normal.")

#number divisible 

number = int(input("enter a number:"))

if number % 5 == 0:
    print("Divisible by 5")

#postive or negative     

number = int(input("enter a number:"))

if number >=0:
    print("positive")
else:
    print("negative")

#Greater 

number = int(input("enter a number:"))

if number > 100:
    print("number is greater than 100")
else:
    print("number is not greater than 100")

#Marks 
marks = int(input("enter marks:"))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 60:
    print("grade c")
elif marks >= 40:
    print("grade D")
else:
    print("fail")

#Largest 

a = int(input("enter first number: "))
b = int(input("enter second number:"))

if a > b:
    print("largest:",a)
elif b > a:
    print("largest:",b)
else:
    print("both are equal")

#largest abc 

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if a >= b and a >=c :
    print("largest:",a)
elif b >=a and b >= c:
    print("Largest:",b)
else:
    print("largest:",c)

#Days

# Program to get day name from number using if-elif

num = int(input("Enter day number (1-7): "))

if num == 1:
    print("Day 1 == Monday")
elif num == 2:
    print("Day 2 == Tuesday")
elif num == 3:
    print("Day 3 == Wednesday")
elif num == 4:
    print("Day 4 == Thursday")
elif num == 5:
    print("Day 5 == Friday")
elif num == 6:
    print("Day 6 == Saturday")
elif num == 7:
    print("Day 7 == Sunday")
else:
    print(" Invalid input! Please enter between 1 and 7.")

 #operators

 # Simple calculator using if statements

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("cannot Divided by zero")
else:
    print("Invalid operator")

 # Nested if example for login system

username = input("Enter username: ")
password = input("Enter password: ")

# Check username first
if username == "admin":
    # Nested check for password
    if password == "12345":
        print("Login Successful! Welcome,", username)
    else:
        print("Password is wrong!")
else:
    print("Username not found!")
   
   
    






              





   
