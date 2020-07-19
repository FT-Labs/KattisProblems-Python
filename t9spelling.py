"""
Author : Arda
Date : 7/18/2020
"""


phone = {"1" : 1 , "abc":2 , "def":3 , "ghi":4,"jkl":5,"mno":6,"pqrs":7,"tuv":8,"wxyz":9}


case = 1
tmp = ""
for _ in range(int(input())):
    s = ""
    for ch in input():
        if ch == " ":
            if s!="" and s[-1]=="0" : s+= " "
            s += "0"
            tmp = ""
        else:
            for key in phone:
                if ch in key:
                    times = key.find(ch)
                    if tmp==key : s+= " "
                    s += (times+1)*str(phone[key])
                    tmp = key

    print(f"Case #{case}: {s}")
    case += 1