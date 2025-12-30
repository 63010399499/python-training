'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def facti(n):
    if n==0 or n==1:
        return n
    return n*facti(n-1)
print(facti(6))
    