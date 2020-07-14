"""
Author : Arda
Date : 7/13/2020
"""

from string import ascii_lowercase

for _ in range(int(input())):

    tot = set()

    s = input().lower()

    for i in s:
        if i in ascii_lowercase:
            tot.add(i)


    if (len(ascii_lowercase)-len(tot)) == 0:
        print("pangram")
    else:
        tmp = ""
        for i in ascii_lowercase:
            if i not in tot:
                tmp += i

        print("missing {}".format(tmp))
