#!/usr/bin/env/python3
"""
Author : Arda
Company : PhysTech
Date : '23.06.2020'
"""

month , num = input().split()

if (month == "OCT" and num == "31") or (month == "DEC" and num == "25"):
    print("yup")
else:
    print("nope")