from math import sin,radians,ceil

nums = [int(x) for x in input().split(" ")]

print(ceil(nums[0]/sin(radians(nums[1]))))