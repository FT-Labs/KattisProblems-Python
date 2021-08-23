"""
Author : Arda
Date : 7/2/2020
"""


total = 0

for _ in range(int(input())):
    s = input().lower()

    if "pink" in s or "rose" in s:
        total += 1

if total == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(total)