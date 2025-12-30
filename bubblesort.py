'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1): 
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=list(map(int,input().split(",")))
bubble_sort(arr)
print("sorted array:",arr)
   