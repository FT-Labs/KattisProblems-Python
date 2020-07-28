"""
Author : Arda
Date : 7/22/2020
"""



x = int(input())

fib = [0,1]

for i in range(2,x+1):
    fib.append(fib[i-2]+fib[i-1])


print("{} {}".format(fib[-2],fib[-1]))