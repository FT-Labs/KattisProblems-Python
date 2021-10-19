#!/usr/bin/python

from itertools import permutations
import re

s = input()


perms = {}
for perm in permutations("RBL"):
    perms["".join(perm)] = 'C'

rep = dict((re.escape(k), v) for k, v in perms.items())
pattern = re.compile("|".join(rep.keys()))
s = pattern.sub(lambda m: rep[re.escape(m.group(0))], s)

#s = s.replace(perms)
s = s.replace('R', 'S')
s = s.replace('B', 'K')
s = s.replace('L', 'H')

print(s)
