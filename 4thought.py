#!/usr/bin/python


from itertools import combinations_with_replacement

if __name__ == "__main__":
    ops = ["+", "-", "*", "//"]

    ans = dict()



    for i in ops:
        for j in ops:
            for k in ops:
                cur = f"4 {i} 4 {j} 4 {k} 4"
                num = eval(cur)
                cur += f" = {num}"
                ans[num] = cur.replace("//", "/")



    t = int(input())

    for _ in range(t):
        num = int(input())

        if num in ans.keys():
            print(ans[num])
        else:
            print("no solution")
