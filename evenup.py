"""
Author : Arda
Date : 7/21/2020
"""

l = int(input())

nums = [x[-1] for x in input().split()]

i = 0

while i<len(nums):

    if (int(nums[i])+int(nums[i+1]))%2==0:
        nums.pop(i)
        nums.pop(i)
    else:
        i += 1

print(len(nums))

#Doesn't get execution time with python. Java or C++ instead, array operations are slow in python.