#!/usr/bin/env python

from random import randint

n = int(input())

names = set()

vowels = "aeoiu"
consonants = "qwrtypsdfghjklzxcvbnm"

while len(names) != n:
    x = ""

    while len(x) != 20:
        if len(x)%3 == 0 or len(x)%4 == 0:
            x += vowels[randint(0, len(vowels) - 1)]
        else:
            x += consonants[randint(0, len(consonants) - 1)]

    names.add(x)


for i in names:
    print(i)
