"""
Author : Arda
Date : 7/11/2020
"""

import heapq
import sys

try:
    case = 1

    while True:
        sys.stdin.read(2)
        arr = []
        for x in input().split():
            heapq.heappush(arr,int(x))

        print("Case {}: {} {} {}".format(case,heapq.nsmallest(1,arr)[0],heapq.nlargest(1,arr)[0],heapq.nlargest(1,arr)[0]-heapq.nsmallest(1,arr)[0]))

        case += 1
except:
    pass