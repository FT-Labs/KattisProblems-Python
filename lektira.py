"""
Author : Arda
Date : 7/28/2020
"""


s = input()
tmp = s

for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s)):
        tot = s[:i][::-1]+s[i:j][::-1]+s[j:][::-1]
        if tot < tmp:
            tmp = tot

print(tmp)