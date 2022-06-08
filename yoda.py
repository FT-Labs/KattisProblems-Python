#!/usr/bin/env python

s1 = input()
s2 = input()

ans1 = ""
ans2 = ""

a1 = len(ans1) - 1
a2 = len(ans2) - 1

for i in range(min(len(s1), len(s2)) - 1, -1, -1):
    if s1[a1] == s2[a2]:
        ans1 += s1[a1]
        ans2 += s2[a2]
    elif s1[a1] > s2[a2]:
        ans1 += s1[a1]
    else:
        ans2 += s2[a2]
    a1 -= 1
    a2 -= 1

if len(s1) > len(s2):
    for i in range(len(s1) - len(s2) - 1, -1, -1):
        ans1 += s1[i]
elif len(s2) > len(s1):
    for i in range(len(s2) - len(s1) - 1, -1, -1):
        ans2 += s2[i]

print("YODA" if ans1 == "" else int(ans1[::-1]))
print("YODA" if ans2 == "" else int(ans2[::-1]))
