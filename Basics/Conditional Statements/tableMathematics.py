# program to write for the tables nested loop example

# numTable = int(input("Enter the number for which table needs to be generated"))
# for i in range(1,21,1):
#     print(numTable*i, end="  ")

numTable = int(input("Enter the number upto which table needs to be generated: "))
numLength = int(input("Enter the number upto which table length needs to be generated: "))
for i in range(1,numTable+1):
    print(i)
    for j in range(1,numLength+1):
        print(f"{i} x {j} = {i*j}")
    print("-x-x-x-x-x-x-x-")