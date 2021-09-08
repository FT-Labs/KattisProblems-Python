#!/usr/bin/python


import sys


for line in sys.stdin:

    for ch in "BFPV":
        line = line.replace(ch, '1')

    for ch in "CGJKQSXZ":
        line = line.replace(ch, '2')

    for ch in "DT":
        line = line.replace(ch, '3')

    for ch in "MN":
        line = line.replace(ch, '5')

    line = line.replace('L', '4')
    line = line.replace('R', '6')

    ans = ""

    temp = line[0]

    if temp in "123456":
        ans += temp


    for ch in line[1:]:

        if ch in "123456":
            if ch != temp:
                ans += ch

        temp = ch


    print(ans)
