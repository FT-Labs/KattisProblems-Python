"""
Author : Arda
Date : 6/26/2020
"""

nums = sorted([int(x) for x in input().split()])

s = input()

ordered = []
for i in s:
    if i=="A":
        ordered.append(str(nums[0]))
    elif i=="B":
        ordered.append(str(nums[1]))
    elif i=="C":
        ordered.append(str(nums[2]))

print(" ".join(ordered))