#Program to check whether number is Prime #shorthand in print
n=int(input("Enter the number: "))
isPrime = True
if n<2:
    isPrime = False
else:
    for i in range(2,n):
        if n%i==0:
            isPrime = False
            break
print(f"{n} is Prime" if isPrime else f"{n} is not Prime" )