'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def leftover(a,b):
    left=""
    remove=set(b)
    for ch in a:
        if ch not in remove:
            left+=ch
    if left:
        print(left)
    else:
        print("empty")
a="abcdef"
b="bde"
leftover(a,b)