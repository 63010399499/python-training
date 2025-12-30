'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def shownumber(self):
        print(f"{self.real}i+{self.imag}j")
    def add(self,num2):
        newreal=self.real+num2.real
        newimag=self.imag+num2.imag
        return complex(newreal,newimag)
num1=complex(1,6)
num1.shownumber()
num3=complex(2,5)
num3.shownumber()
num4=num1.add(num3)
num4.shownumber()