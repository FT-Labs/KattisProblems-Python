"""
Author : Arda
Date : 6/24/2020
"""

nums = [int(x) for x in input().split()]

for i in range(1,nums[-1]+1):

    if i%nums[0]==0 and i%nums[1]==0:
        print("FizzBuzz")
    elif i%nums[0] == 0:
        print("Fizz")
    elif i%nums[1] == 0:
        print("Buzz")
    else:
        print(i)