"""
Author : Arda
Date : 7/10/2020
"""

s1,s2 = input().split()

if s1[-2:] == 'ex':
    print(s1+s2)
elif s1[-1] == 'e':
    print(s1+"x"+s2)
elif s1[-1] == 'a' or s1[-1] == 'i' or s1[-1] == 'o' or s1[-1] == 'u':
    print(s1[:-1]+"ex"+s2)
else:
    print(s1+"ex"+s2)