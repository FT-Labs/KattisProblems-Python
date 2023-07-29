#!/usr/bin/python


n = eval(input())


for _ in range(n):
    line = input()

    ans = ""

    for i in range(len(line)):
        ans += line[i]

        tmp = ans*int(2*(len(line)/(i+1)))

        if tmp[:len(line)] == line:
            print(i+1)
            break
