"""
Author : Arda
Date : 6/25/2020
"""

order = [1,1,2,2,2,8]
nums = [int(x) for x in input().split()]

print(" ".join(str((nums[i]-order[i])*-1) if nums[i]>order[i] else str(order[i]-nums[i]) for i in range(len(order))))



