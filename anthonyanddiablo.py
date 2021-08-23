"""
Author : Arda
Date : 7/10/2020
"""


from math import pi

a,n = [(float(x)) for x in input().split()]


r = n/(pi*2)
ar = pi * r**2

if ar >= a : print('Diablo is happy!')
else: print('Need more materials!')