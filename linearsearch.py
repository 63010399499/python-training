'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return-1 
arr=list(map(int,input().split(",")))
target=int(input())
print(linear_search(arr,target))