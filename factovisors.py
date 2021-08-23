"""
Author : Arda
Date : 7/11/2020
"""
from collections import Counter



#Calculating factors of given integer

def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return Counter(factors)

while True:

    try:
        fact,div = [int(x) for x in input().split()]

        if div==0:
            print("{} does not divide {}!".format(div, fact))
            continue
        elif div==1:
            print("{} divides {}!".format(div, fact))
            continue

        first = primeFactors(div)
        istrue = False

        #Looking in factorial if there is enough or more prime factorials in given factorial
        for i in first.most_common():
            cnt = 0
            for q in range(i[0]-1,fact+1):
                #Calculating numbers
                while q%i[0]==0:
                    cnt += 1
                    q /= i[0]

                if cnt>=i[1]:
                    break
            if cnt<i[1]:
                print("{} does not divide {}!".format(div, fact))
                istrue = True
                break

        if not istrue:
            print("{} divides {}!".format(div,fact))

    except:
        break