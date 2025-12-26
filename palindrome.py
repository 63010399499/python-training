'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def check(x):
    l=0
    r=len(x)-1
    while l<r:
        if x[l]!=x[r]:
            return "not a palindrome"
        else:
            l+=1
            r-=1
    return"palindraome"
x="madam"
print(check(x))
     