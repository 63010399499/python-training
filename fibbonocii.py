'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
    