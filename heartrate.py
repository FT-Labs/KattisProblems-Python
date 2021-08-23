#!/usr/bin/env/python3
"""
Author : Arda
Company : PhysTech
Date : '23.06.2020'
"""


rep = int(input())


for i in range(rep):
    b , m = [float(x) for x in input().split()]

    med = b/m*60
    std = med/b

    print("{0:.4f} {1:.4f} {2:.4f}".format(med-std,med,med+std))
