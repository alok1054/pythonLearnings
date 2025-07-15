# # Class without attributes
# class Hello:
#     def printHello(self):
#         print("Yen Samachara!!")
#
# obj1  = Hello()
# obj1.printHello()
# # Hello.printHello(' ')

# Class program with attributes
class student: #creates class
    def __init__(self,name,usn): #constructor called, object is created
        self.name = name #attributes
        self.usn = usn #attributes

    def printDetails(self):
        print(f"Name is {self.name} and USN is {self.usn}" )
        # print(f"USN is {self.usn}")

s1=student("Alok", "1BM21CV001")
s2=student("Manjunath", "1BM21CV002")

print(s1.name, s1.usn)
print(s2.usn)

s1.printDetails()
s2.printDetails()