# List is mutable, ordered collection of data

# Properties: Ordered, Mutable, Allows Duplicates

# In other languages we have arrays ---> int array[]

a = [1, "hello", 10.5, True]

myList = [1,2,3,4,5]

anotherList = list(range(2,101,3))
print(anotherList[0])

priceFruits=["Mango", 100, "Orange", 50]
#1. Assessing the elements of the list
print(priceFruits[1:3])
print(priceFruits[-4:-1])
print(priceFruits[-4:])
#2. Modifying the lists
priceFruits[-2]="Peach"
print(priceFruits)
#3. Insert
priceFruits.insert(2,'Orange')
priceFruits.insert(3,240)
print(priceFruits)
#4. Append
priceFruits.append("Jaamun")
print(priceFruits)
#5. remove
priceFruits.remove("Jaamun")
print(priceFruits)
#6. Pop removes last elements
priceFruits.pop()
print(priceFruits)

#other functions
priceFruits.append(150)
print(priceFruits)
print(len(priceFruits))
priceFruits.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'
print(priceFruits)
priceFruits.sort(reverse=True)
print(priceFruits)

