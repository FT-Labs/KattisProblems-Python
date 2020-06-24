"""
Author : Arda
Date : 6/24/2020
"""
import sys

try:
    while True:
        #To pass execution time, you should write this in c++. Same code below in c++ will get past through execution time.
        #For complicated problems or if you need to initiliaze long arrays and have <1 second cpu limit, you should try them on c++
        #Python is much much slower than c++
        n,strnums = input().split(": ")

        nums = [int(x) for x in strnums.split()]
        boolList = [False for x in range(len(nums))]

        antiarithmetic = True

        for _ in range(int(n)):
            if not antiarithmetic:
                break
            if boolList[nums[_]]:
                antiarithmetic = False
            else:
                boolList[nums[_]] = True
                for i in range(_):
                    ans = 2*nums[_]-nums[i]
                    if 0 <= ans < int(n) and not boolList[ans]:
                        antiarithmetic = False

        print("yes" if antiarithmetic else "no")


except ValueError:
    sys.exit()




