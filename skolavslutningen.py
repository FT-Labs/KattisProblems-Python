#!/usr/bin/env python


r, c, class_count = map(int, input().split())


arr = []

for i in range(r):
    arr.append(input())

ans = []

for i in range(c):
    s = ""
    for j in range(r):
        s += arr[j][i]

    if i == 0:
        ans.append(s)
    else:
        found = False
        for ch in s:
            for k in range(len(ans)):
                if ch in ans[k]:
                    ans[k] += s
                    found = True
                    break
            if found:
                break
        if not found:
            ans.append(s)

print(ans)
print(len(ans))
