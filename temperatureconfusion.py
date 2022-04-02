#!/usr/bin/env python

from fractions import Fraction

top, bot = map(int, input().split("/"))

top -= 32 * bot
top *= 5
bot *= 9

fr = Fraction(top, bot)
print(str(fr.numerator)+'/'+str(fr.denominator))
