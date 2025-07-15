# Program to write to display pattern square of star

# for i in range(5):
#     for j in range(5):
#         print("*",end =" ")
#     print()

# Program to write to display pattern square of star
# num = int(input("Enter the rows upto which you want pattern to get printed: "))
# for i in range(1,num+1,2):
#     for j in range(1,i+1):
#         print("*",end =" ")
#     print()
#
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("*",end =" ")
#     print()

# Program for Star Triangle
# nRows = 5
# for i in range(nRows):
#     for spaces in range(nRows-i-1):
#         print(" ", end='')
#     for stars in range(2*i+1):
#         print("*", end='')
#     print()

# Program for Heart
nRows =6
nCol =7
for i in range(nRows):
    for j in range(nCol):
        if i==0 and j%3!=0:
            print(" * ", end ='')
        elif i==1 and j%3==0:
            print(" * ", end ='')
        elif i-j==2:
            print(" * ", end ='')
        elif i+j==8:
            print(" * ", end ='')
        else:
            print("   ", end='')
    print()