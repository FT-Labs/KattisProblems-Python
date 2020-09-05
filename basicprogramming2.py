"""
Author : Arda
Date : 9/5/2020
"""

from itertools import combinations
from collections import Counter
import sys

def main():


    n,t = [int(x) for x in input().split()]

    s = input()

    if t==1:
        q = sorted([int(x) for x in s.split()])

        small = q[0]
        big = q[-1]

        iS = 0
        iB = n-1
        while iS!=iB:
            if small+big<7777:
                iS += 1
                small = q[iS]
            elif small+big>7777:
                iB -= 1
                big = q[iB]
            else:
                print("Yes")
                sys.exit()

        print("No")

    elif t==2:
        q = Counter(s.split())
        if q.most_common(1)[0][1]>1:
            print("Contains duplicate")
        else:
            print("Unique")

    elif t==3:
        q = Counter(s.split())
        if q.most_common(1)[0][1]>n/2:
            print(q.most_common(1)[0][0])
        else:
            print("-1")

    elif t==4:

        q = sorted([int(x) for x in s.split()])
        if n%2!=0:
            print(q[n//2])
        else:
            print("{} {}".format(q[n//2-1],q[n//2]))
    else:
        q = sorted([int(x) for x in s.split() if len(x)==3])
        print(" ".join([str(x) for x in q]))






if __name__ == '__main__':
    main()


