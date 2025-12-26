'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
for i in range(n):
    for j in range(n):
      if j==0 or i==n-1 or i==j or i==0 or j==n-i-1 or j==n-1:
          print("*",end=" ")
      else:
          print(" ",end=" ")
    print()      