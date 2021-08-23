"""
Author : Arda
Date : 7/2/2020
"""

for _ in range(int(input())):

    s = input()
    mLen = int(len(s)**0.5)

    m = [[x for x in s[j*mLen:mLen+j*mLen]] for j in range(mLen)]

    ans = ""


    for j in range(mLen-1,-1,-1):
        for i in range(mLen):
            ans += m[i][j]

    print(ans)


