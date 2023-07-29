#!/usr/bin/python

from itertools import permutations



a, b = map(int, input().split())

minWord = b//2+1

minWord = max(a, minWord)


s = "abcdefghijklmno"

tot = 0


for perm in permutations(s):
    print("".join(perm), end=" ")
    tot += 1

    if tot >= minWord:
        break
