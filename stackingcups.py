"""
Author : Arda
Date : 6/28/2020
"""

colors = []
for _ in range(int(input())):
    s = input().split()

    try:
        rad = int(s[1])
        colors.append([rad,s[0]])
    except ValueError:
        rad = int(s[0])/2
        colors.append([rad,s[1]])

for i in sorted(colors):
    print(i[1])