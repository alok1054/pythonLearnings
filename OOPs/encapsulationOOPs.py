class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self._balance = balance #Protected
        self.__pin = pin #Private

    def showBalance(self):
        print(f"Account holder : {self.name}")
        print(f"Balance is : {self._balance}")
        print(f"Pin : {self.__pin}")

acc = BankAccount("Alok", 9999999999, 6666)

print(acc.name)
print(acc._balance)
# print(acc.__pin)
acc.showBalance()
