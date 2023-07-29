#!/usr/bin/python


r, c, zr, zc =[int(x) for x in input().split()]

for i in range(r):
    txt = input()
    sent = ""
    ans = ""
    if zc > 1 :
        for j in txt :
            ans += zc*j
    else:
        ans = txt


    for j in range(zr):
        print(ans)
