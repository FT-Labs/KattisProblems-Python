#!/usr/bin/env/python3
"""
Author : Arda
Company : PhysTech
Date : '23.06.2020'
"""

word = input()

#Easy solution thanks to python syntax

if "ss" in word:
    print("hiss")
else:
    print("no hiss")


#Uncomment for second solution (For other programming lans)

# ch = word[0]
#
# ishiss = False
#
# for i in word[1:]:
#     if ch == "s" and i == "s":
#         print("hiss")
#         ishiss = True
#         break
#     ch = i
# if not ishiss:
#     print("no hiss")