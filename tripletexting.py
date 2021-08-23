"""
Author : Arda
Date : 6/25/2020
"""

t = input()

wordLen = int(len(t)/3)

if t[:wordLen] == t[wordLen:-wordLen]:
    print(t[:wordLen])
elif t[:wordLen] == t[-wordLen:]:
    print(t[:wordLen])
elif t[wordLen:-wordLen] == t[-wordLen:]:
    print(t[-wordLen:])
