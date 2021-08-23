"""
Author : Arda
Date : 7/9/2020
"""
from itertools import combinations,permutations
import sys


_, total = [int(x) for x in input().split()]
z = str(total)
arr = []


for i in input().split():
    q = []
    if len(i)>len(str(total)):
        continue

    for j in permutations(i):
        tmp = "".join(j)
        if int(tmp)<total:
            q.append(tmp)
            if "6" in tmp : q.append(tmp.replace("6","9"))
        else:
            continue
        if "9" in tmp : q.append(tmp.replace("9","6"))
    arr.append(q)

#Unfortunately this long loop cant make it in time.
#Need to find a more compact way, without combinations.
for q in combinations(arr,2):
    for i in q[0]:

        if len(i)==len(z) and int(i[0])>int(z[0]):
            break
        for j in q[1]:
            if len(j) == len(z) and int(j[0]) > int(z[0]):
                break
            if int(i)+int(j) == total:
                print("YES")
                sys.exit()

print("NO")


