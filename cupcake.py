'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def cupcakes(n,arr):
    sum=0
    for i in range(n):
        if arr[i]>=5:
           sum+=arr[i]
    print(sum)
n=5
arr=[1,2,5,8,3,7]
cupcakes(n,arr)