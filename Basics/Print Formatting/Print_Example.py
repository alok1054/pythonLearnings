# birthYear = int(input('Enter your birthdate: '))
# age = 2025 - birthYear
# print("your age is: ", age)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
empID= int(input("Enter your EmpID: "))
# Without formatted strings (explicit typecasting) , comma will work for the last variable only
print("Your name is " + name + " and your age is " + str(age) + " and your empID is : ", empID)
# With formatted strings
print(f"Your name is {name} and your age is {age} and your empID is {empID}")