'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
      lower=i
      for j in range(i+1,n): 
          if arr[j]<arr[lower]:
              lower=j 
      arr[i],arr[lower]=arr[lower],arr[i]          
arr=[8,4,48,26,3]
selection_sort(arr)
print("sorted array:",arr)