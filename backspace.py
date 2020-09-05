"""
Author : Arda
Date : 8/24/2020
"""

s = input()

stack = []

for i in s:
    if i != "<":
        stack.append(i)
    else:
        stack.pop()

print("".join(stack))






