'''
Manage pets (Dogs and Cats), their actions, and some shared behavior.
1. Class
A class is a blueprint for creating objects (a template). It defines attributes and methods common to all objects of that type.
2. Object
An object is an instance of a class. You can create multiple objects from a single class.
3. Inheritance
Inheritance allows a class (child) to inherit properties and behavior from another class (parent).
4. Encapsulation
Encapsulation is the concept of restricting access to certain details of an object and only exposing necessary parts.
5. Polymorphism
Polymorphism allows different classes to be treated through the same interface, especially via method overriding or operator overloading.
python
Copy
Edit

'''
# Base class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some generic sound"

    def get_info(self):
        return f"{self.name}, Age: {self.age}"

# Derived class - Dog
class Dog(Pet):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class - Cat
class Cat(Pet):
    def speak(self):
        return f"{self.name} says Meow!"

# Pet Manager class to manage all pets
class PetManager:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        print(f"{pet.name} has been added!")

    def show_all_pets(self):
        for pet in self.pets:
            print(pet.get_info(), "|", pet.speak())


# --------- Demo ---------
if __name__ == "__main__":
    manager = PetManager()

    # Create some pets
    dog1 = Dog("Buddy", 3)
    cat1 = Cat("Whiskers", 2)

    # Add pets to manager
    manager.add_pet(dog1)
    manager.add_pet(cat1)

    # Show all pets
    print("\nAll Pets:")
    manager.show_all_pets()
