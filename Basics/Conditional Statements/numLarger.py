# Program to identify larger number between two

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1>num2:
    print(f"{num1} is larger than {num2}")
elif num1==num2:
    print(f"both numbers are equal")
else:
    print(f"{num2} is larger than {num1}")