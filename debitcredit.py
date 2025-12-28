'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def debit(self,amount):
        if self.balance>amount:
            self.balance+=amount
            print(f"{amount}is debited,bal is{self.getbal()}")
        else:
            print("isufficient funds")
    def credit(self,amount):
        self.balance+=amount
        print(f"{amount}is credited,bal is{self.getbal()}")
    def getbal(self):
        return self.balance
acc1=Account(1000,"acc123")
acc1.credit(500)
acc1.debit(100)