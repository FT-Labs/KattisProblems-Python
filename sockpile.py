"""
Author : Arda
Date : 8/30/2020
"""

from itertools import combinations,permutations

p , w = [int(x) for x in input().split()]

socks = [1 for i in range(w)]


q = 2
x = 0

while x<p:
    socks += [q,q]
    q += 1
    x += 1

cnt = 0
tot = 0

totWhite = 0
totPair = 0
for perm in permutations(socks):

    for i in range(0,len(perm),2):
        try:
            if perm[i] == perm[i+1]:
                if perm[i] == 1:
                    totWhite += 1
                else:
                    totPair += 1
                cnt += 1
                break
        except:
            pass

    tot += 1

print(cnt/tot)
print()
print(cnt)
print(tot)

print(f"White : {totWhite} , Pair : {totPair}")

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n = 7
table = np.zeros((n+1 , n+1))
table[1][0] = 1
table[1][1] = 0.333333
table[1][2]  = 0.333333
table[1][3] = 0.6
table[1][4:] = 1
table[2][0] = 0.333333
table[2][1] = 0.333333
table[2][2] = 0.466666667
table[2][3] = 0.5428571428571428
table[2][4] = 0.7714285714285715
table[2][5] = 0.873015873015873
table[2][6] = 1
table[3][0] = 0.466666667
table[3][1] = 0.3523809523809524
table[3][2] = 0.42857142857142855
table[3][3] = 0.5047619047619047
table[3][4] = 0.6952380952380952
table[3][5] = 0.7922077922077922


df = pd.DataFrame(columns=['White Count','1 Pair' , '2 Pair' , '3 Pair'])
df['White Count'] = [0,1,2,3,4,5,6]
df['1 Pair'] = table[1][:7]
df['2 Pair'] = table[2][:7]
df['3 Pair'] = table[3][:7]


plt.plot([_ for _ in range(7)] , df['1 Pair'] , c='g')
plt.plot([_ for _ in range(7)] , df['2 Pair'] , c='r')
plt.plot([_ for _ in range(7)] , df['3 Pair'] , c='b')
plt.show()

for row in range(3, n + 1):
    table[row][:row] = table[row - 1][:row]

    for column in range(row, n + 1):
        table[row][column] = table[row - 1][column - row] + table[row - 1][column]











