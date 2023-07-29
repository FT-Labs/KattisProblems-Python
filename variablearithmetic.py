#!/usr/bin/python

x = input()

vals = dict()
while x != '0':
    if x.count('='):
        key, val = x.split(" = ")
        vals[key] = val
    else:

        tot = 0
        l = x.split(" + ")


        for key, val in vals.items():
            for i in range(len(l)):
                if l[i] in vals.keys():
                    l[i] = vals[l[i]]



        flag = False
        tmp = list()
        for i in l:
            try:
                tot += int(i)
                if int(i) == 0:
                    flag = True
            except:
                tmp.append(i)

        if tot != 0:
            if len(tmp) != 0:
                print("{} + ".format(tot), end="")
            else:
                print(tot, end="")
        elif flag:
            print('0', end="")

        print(" + ".join(tmp))

    x = input()
