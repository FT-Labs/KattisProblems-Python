nums = input().split(" ")

x = int(nums[0][::-1])
y = int(nums[1][::-1])

if x>y:
    print(x)
else:
    print(y)



