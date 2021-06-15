#!/usr/bin/python


l = input().split(';')

tot = 0

for i in l:
    if i.find('-') != -1:
        m,n = [int(x) for x in i.split('-')]
        tot += n-m+1
    else:
        tot += 1

print(tot)
