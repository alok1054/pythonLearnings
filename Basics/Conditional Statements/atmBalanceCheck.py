# Program to withdraw from ATM and show balance amount

accBalance = float(input("Enter the account balance in INR: "))
amtWithdrawal = int(input("Enter the withdrawal amount in INR: "))

if amtWithdrawal<=0 :
    print(f"Invalid entry : you have entered negative values {amtWithdrawal}")
elif amtWithdrawal>accBalance :
    print(f"Invalid entry : Insufficient balance")
else :
    accBalance = accBalance - amtWithdrawal
    print(f"Transaction Successful, Balance amount is INR {accBalance} , Please maintain minimum balance")

