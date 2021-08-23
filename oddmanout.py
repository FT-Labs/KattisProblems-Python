"""
Author : Arda
Date : 7/2/2020
"""
from collections import Counter

case = 1
for _ in range(int(input())):

    input()

    odd = Counter(input().split())

    print("Case #{}: {}".format(case,odd.most_common()[-1][0]))
    case += 1