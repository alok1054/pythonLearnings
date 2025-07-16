# # Program to call child class constructor by default
# class parent:
#     def __init__(self):
#         print("This is Parent Constructor")
#
# class child:
#     def __init__(self):
#         print("This is child constructor")
#
# c = child()

# Program to call parent class constructor within child class
class parent:
    def __init__(self):
        print("This is Parent Constructor")

class child(parent):
    def __init__(self):
        super().__init__()  # Calls the parent class constructor in child class
        print("This is child constructor")

c = child()