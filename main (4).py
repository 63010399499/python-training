'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
x=int(input())
for i in range(1,x+1):
    if(i%3==0)and(i%5==0):
        print("fizzbuzz")
    elif i%3==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)