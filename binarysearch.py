'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def binary_search(arr,target):
    left=0
    right=len(arr)-1 
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1 
        else:
            right=mid-1
    return-1
arr=[6,7,8,55]
target=55
print(binary_search(arr,target))