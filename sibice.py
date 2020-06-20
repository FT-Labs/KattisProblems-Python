nums = [int(i) for i in input().split(" ")]
hypot = (nums[1]**2+nums[2]**2)**0.5

for i in range(nums[0]):
    match = int(input())
    if match<=hypot:
        print("DA")
    else:
        print("NE")