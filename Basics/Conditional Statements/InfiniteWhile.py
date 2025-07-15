
# print("Please Select one of the following 1. Hello 2. Bye 3. Exit")
# i = int(input("Enter the choice in number: "))
# while i<3:
#     if i==1:
#         print("Hello")
#         print("Please Select one of the following 1. Hello 2. Bye 3. Exit")
#         i = int(input("Enter the choice in number: "))
#     else:
#         print("Bye")
#         print("Please Select one of the following 1. Hello 2. Bye 3. Exit")
#         i = int(input("Enter the choice in number: "))
#
# while i==3:
#     print ("Exit")
#     break

while True:
    print("1. Say Hello\n2. Say Bye\n3. Exit")
    choice =int(input("Enter the choice in number: "))
    if choice==1:
        print("Hello")
    elif choice==2:
        print("Bye")
    elif choice==3:
        print("Exit")
        break
    else:
        print("Invalid Choice!!")

