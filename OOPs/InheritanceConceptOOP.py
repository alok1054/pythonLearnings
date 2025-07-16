# Example of Single level inheritance (concept of OOPs)
# class Animal:
#     def eat(self):
#         print("Eating...")
#
# class Dog(Animal):
#     def bark(self):
#         print("Bho Bho...")
#
# a=Animal()
# d=Dog()
#
# a.eat()
#
# d.bark()
# d.eat()

# # Example of Multi level inheritance (concept of OOPs)
# class Animal:
#     def eat(self):
#         print("Eating...")
#
# class Dog(Animal):
#     def bark(self):
#         print("Bho Bho...")
#
# class Puppy(Dog):
#     def cry(self):
#         print("Crying...Uaaannn")
# a=Animal()
# d=Dog()
# p=Puppy()
# #Grandparent
# a.eat()
# #Parent
# d.bark()
# d.eat()
# #Child
# p.eat()
# p.bark()
# p.cry()

# # Example of Multiple level inheritance (concept of OOPs)
# class dad:
#     def couch(self):
#         print("sleeping in couch...")
#
# class mom:
#     def work(self):
#         print("working hard")
#
# class child(dad, mom):
#     def cry(self):
#         print("Crying...Uaaannn")
# d=dad()
# m=mom()
# c=child()
# #Grandparent
# d.couch()
# #Parent
# m.work()
#
# #Child
# c.couch()
# c.work()
# c.cry()

# Example of Hierarchical level inheritance (concept of OOPs)
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Bho Bho...")

class cat(Animal):
    def meow(self):
        print("Meow")

a=Animal()
d=Dog()
c=cat()
#parent

a.eat()
#child
d.eat()
d.bark()

#another Child
c.eat()
c.meow()
