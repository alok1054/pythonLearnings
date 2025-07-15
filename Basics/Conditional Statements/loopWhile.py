
# i=1
# while i<101:
#     print(f"{i}", end="|")
#     i+=1

#my code
# num = int(input("Enter the number: "))
# i=2
# isPrime = True
# while i<num:
#     if num % i == 0:
#         isPrime = False
#         print(f"{num} is Prime" if isPrime else f"{num} is not Prime")
#         break
#     i+=1
# print(f"{num} is Prime" if isPrime else f"{num} is not Prime")
# while num == 1 or num == 2:
#         print("Invalid number", end="|")
#         break

# instructor
n = int(input("Enter the number: "))
isPrime = True
if n<2:
    isPrime = False
else:
    i=2
    while i<n:
        if n%i==0:
            isPrime = False
            break
        i+=1
print(f"{n} is Prime" if isPrime else f"{n} is not Prime")