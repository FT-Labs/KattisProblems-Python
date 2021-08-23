"""
Author : Arda
Date : 6/27/2020
"""


s = input()

word = ""
curch = ""
for ch in s:
    if curch!=ch:
        curch = ch
        word += curch
print(word)