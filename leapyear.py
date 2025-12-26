'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
year=int(input())
if year%4==0 and year%100!=0:
    print("leap year")
elif year%400==0:
    print("leap year")
else:
    print("not a leapyear")