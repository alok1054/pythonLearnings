# Arbitrary Arguments
def name(*n):
    # print("Your name is: "+n[1])
    print("Names in the list:")
    for i in n:
        print(i)
name("Alok", "Pocoyo")

#Keywords arguments
def name(name1, name2, name3):
    print("First name is " + name1)

name(name2="Alok", name1="Manju", name3 = "BMS")


# Arbitrary Keyword Arguments
def name(**n):
    print("Faculty name is "+n["name3"])

name(name1="Alok", name2="Manju", name3="Manish")