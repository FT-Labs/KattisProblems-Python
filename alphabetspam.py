"""
Author : Arda
Date : 6/25/2020
"""

line = input()
totalChar = len(line)

spaces = 0
upper = 0
lower = 0
symbol = 0

for ch in line:
    if ch.isupper():
        upper += 1
    elif ch == "_":
        spaces += 1
    elif ch.islower():
        lower += 1
    else:
        symbol += 1

print("{:.15f}".format(spaces/totalChar))
print("{:.15f}".format(lower/totalChar))
print("{:.15f}".format(upper/totalChar))
print("{:.15f}".format(symbol/totalChar))