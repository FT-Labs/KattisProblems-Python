"""
Author : Arda
Date : 7/2/2020
"""

s = ""

line = input()

i = 0

while i<len(line):
    if line[i] == "a" or line[i] == "o" or line[i] == "e" or line[i] == "u" or line[i] == "i":
        s += line[i]
        i += 3
    else:
        s += line[i]
        i += 1


print(s)