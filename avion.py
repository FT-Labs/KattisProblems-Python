"""
Author : Arda
Date : 6/25/2020
"""

x = ""
for i in range(5):

    s = input()

    if "FBI" in s:
        if x == "":
            x += str(i+1)
        else:
            x += " {}".format(i+1)

print("HE GOT AWAY!" if x=="" else x)