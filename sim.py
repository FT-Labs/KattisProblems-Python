"""
Author : Arda
Date : 8/24/2020
"""

#This is the true solution, however you can't get past execution time with Python. Try C++ instead.


for _ in range(int(input())):
    s = input()

    stack = []
    stackPointer = 0

    for i in s:
        if i == "<":
            try:
                if stackPointer != 0:
                    stack.pop(stackPointer-1)
                    stackPointer -= 1
                    continue
            except IndexError:
    
                continue
        elif i != "[" and i != "]":
            stack.insert(stackPointer , i)
            stackPointer += 1

        elif i == "[":
            stackPointer = 0

        elif i == "]":
            stackPointer = len(stack)




    print("".join(stack))