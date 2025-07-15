# Program to calculate the simple interest

# Variable Initialisation
prinAmount = float(input("Enter the principle Amount: "))
rateInterest = float(input("Enter the Rate of interest per year in %: "))
timeInterest = float(input("Enter the time in years: "))
numInterestCompound = int(input("Enter the number of interest compounded in a year: "))

# Simple Interest
simpleInterest = (prinAmount*rateInterest*timeInterest)/100

# Compound Interest
compoundInterest = prinAmount*((1+(rateInterest/(100*numInterestCompound)))**(timeInterest*numInterestCompound))

print(f"The Principle Amount is {prinAmount} and The interest amount to be paid by the borrower is {simpleInterest} after {timeInterest} years")
print(f"The Compound Amount is {prinAmount} and The interest amount to be paid by the borrower is {compoundInterest} after {timeInterest} years")