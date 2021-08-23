#!/usr/bin/env python3
"""
Author : Arda
Company : PhysTech
Date : 2020-09-10
"""

def isPossible(n):
    n = str(n)
    dct = {"1" : "1234567890",
            "2" : "2356890",
            "3" : "369",
            "4" : "4567890",
            "5" : "56890",
            "6" : "69",
            "7" : "7890",
            "8" : "890",
            "9" : "9",
            "0" : "0"}
    a = True

    q = 0
    while q < len(n) - 1:
        a = a and n[q+1] in dct[n[q]]
        q += 1
    return a


for _ in range(int(input())):
    num = int(input())
    
    i = 0
    while not isPossible(num+i) and not isPossible(num-i):
        i += 1
    if isPossible(num+i):
        print(num+i)
    else:
        print(num-i)


