"""
Author : Arda
Date : 7/2/2020
"""

n = input()

while True:
    digitSum = 0
    for i in n:
        digitSum += int(i)

    if int(n)%digitSum==0:
        print(n)
        break

    n = str(int(n)+1)
