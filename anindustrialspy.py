#!/usr/bin/python


from itertools import combinations,permutations

def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False

        return True



t = eval(input())

for _ in range(t):
    s = input()

    cnt = 0
    se = set()
    for i in range(1, len(s)+1):
        for comb in permutations(s, i):
            num = int("".join(comb))

            if num not in se and isPrime(num):
                cnt += 1

            se.add(num)

    print(cnt)
