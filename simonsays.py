"""
Author : Arda
Date : 6/26/2020
"""

rep = int(input())

for _ in range(rep):
    s = input()

    if "Simon says" == s[:10]:
        print(s[10:])
