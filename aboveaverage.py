"""
Author : Arda
Date : 7/13/2020
"""

for _ in range(int(input())):

    scores = [int(x) for x in input().split()]
    nums = scores.pop(0)

    ans = sum([1/nums*100 for x in scores if x>sum(scores)/nums])

    print("{:.3f}%".format(ans))