# function example
# def scold(i):
#     print(f" Is valuation over?? {i} come to COE!!")
#
# scold("Manish")


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    if a!=0 and b==0:
        print("Can not be divided by zero")
    elif a==0 and b==0:
        print("not defined")
    else:
        return a/b
while True:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    print("Select operation :\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

    choice = int(input("Select the mathematical operation(1,2,3 or 4: "))

    match choice:
        case 1:
            print("Result : ", add(n1,n2))
        case 2:
            print("Result : ", subtract(n1,n2))
        case 3:
            print("Result : ", multiply(n1,n2))
        case 4:
            print("Result : ", division(n1,n2))
        case 5:
            break
        case _:
            print("Invalid choice")