'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} is debited, balance is {self.getbal()}")
        else:
            print("insufficient funds")

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} is credited, balance is {self.getbal()}")

    def getbal(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, interest):
        self.interest = interest
        super().__init__(1000, "acc123")

    def interestrate(self):
        interest_amount = self.balance * (self.interest / 100)
        self.balance += interest_amount
        print(f"Balance after interest: {self.getbal()}")


acc1 = SavingsAccount(5)
acc1.credit(500)
acc1.interestrate()

