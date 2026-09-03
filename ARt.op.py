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




basic_salary = float(input("Enter your basic salary: "))
# Calculate HRA (House Rent Allowance) as 20% of basic salary
hra = 0.2 * basic_salary
#calculate DA (Dearness Allowance) as 10% of basic salary
da = 0.1 * basic_salary
total_salary = basic_salary + hra + da
print(basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Total Salary:", total_salary)



basic_salary = 10000
hra = 0.20 * basic_salary
da = 0.10 * basic_salary
#0.20 * 10000 = 2000
#0.10 * 10000 = 1000
total_salary = basic_salary + hra + da
#10000 + 2000 + 1000 = 13000
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Total Salary:", total_salary)

