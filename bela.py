"""
Author : Arda
Date : 6/25/2020
"""

hands , dom = input().split()
hands = int(hands)*4

cardVals = {"A" : 11 , "K" : 4 , "Q" : 3 , "J" : 2 , "T" : 10 , "9" : 0 , "8" : 0 , "7" : 0}

total = 0

for _ in range(hands):
    card = input()
    if card[0] == "J" and card[1] == dom:
        total += 20
    elif card[0] == "9" and card[1] == dom:
        total += 14
    else:
        total += cardVals[card[0]]

print(total)


