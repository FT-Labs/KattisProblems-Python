"""
Author : Arda
Date : 6/24/2020
"""
from collections import Counter

raw = input().split()
chars = []


for i in raw:
    chars.append(i[0])

print(Counter(chars).most_common(1)[0][1])