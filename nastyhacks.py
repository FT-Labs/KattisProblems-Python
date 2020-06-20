rep = int(input())

for i in range(rep):
    nums = [int(x) for x in input().split(" ")]
    advCost = nums[1] - nums[2]
    if advCost==nums[0]:
        print("does not matter")
    elif advCost>nums[0]:
        print("advertise")
    elif advCost<nums[0]:
        print("do not advertise")