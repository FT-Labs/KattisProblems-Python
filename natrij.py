#!/usr/bin/python

import datetime


fmt = "%H:%M:%S"

start = datetime.datetime.strptime(input(), fmt)
end = datetime.datetime.strptime(input(), fmt)

cur = str(end-start)

if cur[0] == '-':
    if(cur[9] == ':'):
        print('0', end="")
    print(cur[8:])
else:
    if cur == "0:00:00":
        print("24:00:00")
    else:
        if cur[1] == ':':
            print('0', end="")

        print(cur)
