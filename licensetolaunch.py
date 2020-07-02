"""
Author : Arda
Date : 7/2/2020
"""

input()
d = dict()

#Don't use int's for this problem, it would be too inefficient.

junks = input().split()
minL = len(junks[0])
minD = junks[0]
dayL = 0
for i in range(len(junks)):

    if len(junks[i])<=minL:
        minL = len(junks[i])
        if int(junks[i])<int(minD):
            minD = junks[i]
            dayL = i

print(dayL)

#At first i tried to solve it with dictionary, but forgot about junk can repeat for some different days. It
#breaks the pattern.

# junks = sorted(junks,key=len)
#
# minDay = junks[0]
# for i in junks:
#     if len(i)>len(junks[0]):
#         break
#     elif int(i)<int(minDay):
#         minDay = i
#
# print(d[minDay])







