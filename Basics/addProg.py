'''program to do basic mathematical operations using input functions and
 type casting '''

# a_str = input("enter a number: ")
# a = int(a_str)
a = int(input("enter a number: "))
# b_str = input("enter another number: ")
# b = int(b_str)
b = int(input("enter another number: "))

sumoutput = a+b
productoutput = a*b
devisionoutput = a/b
remainderoutput = a%b

print(f"Sum of the two numbers is : {sumoutput} " )
print(f"Product of the two numbers is : {productoutput} ")
print(f"Division of first number by second is : {devisionoutput} " )
print(f"Remainder of first number by  second is : {remainderoutput} " )