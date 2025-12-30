'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class overloadDemo:
    def multiply(self,a,b):
       print(a*b)
    def multiply(self,a,b,c):
        print(a*b*c)
m=overloadDemo()
m.multiply(5,10)