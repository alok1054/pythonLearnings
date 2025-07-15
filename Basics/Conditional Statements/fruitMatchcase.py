# Fruit matchcase

fruit = input("Enter the name of the fruit : ").lower()

match fruit:
    case "apple":
        print("An apple a day takes your salary away!!")
    case "mango":
        print("Delicious!!")
    case "orange":
        print("Vitamin C!!")
    case _:
        print("Fruit not found :(")