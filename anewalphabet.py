"""
Author : Arda
Date : 6/29/2020
"""


newAlphabet = {"a" : "@", "b" : "8" , "c" : "(" , "d" : "|)" , "e" : "3",
               "f" : "#" , "g" : "6" , "h" : "[-]" , "i" : "|" , "j" : "_|",
               "k" : "|<" , "l" : "1" , "m" : "[]\\/[]", "n" : "[]\\[]",
               "o" : "0" , "p" : "|D", "q" : "(,)", "r" : "|Z", "s" : "$" ,
                "t" : "']['" , "u" : "|_|", "v" : "\\/" , "w" : "\\/\\/",
               "x" : "}{" , "y" : "`/" , "z" : "2"}


decrypt = ""

for i in input().lower():
    if i in newAlphabet.keys():
        decrypt += newAlphabet[i]
    else:
        decrypt += i

print(decrypt)