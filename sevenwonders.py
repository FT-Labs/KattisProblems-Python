"""
Author : Arda
Date : 6/27/2020
"""

from collections import Counter

s = Counter(input())

total = 0

for i in s.most_common():
    total += i[1]**2
if len(s.most_common())>=3:
    total += min([x[1] for x in s.most_common()])*7

print(total)

