loop = int(input())

for i in range(loop):
    fact = int(input())
    ans = 1

    for x in range(1, fact+1):
        x = str(x)
        ans *= int(x[-1])

    ans = str(ans)
    print(ans[-1])
