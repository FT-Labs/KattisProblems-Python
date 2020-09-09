#!/usr/bin/env python3
"""
Author : Arda
Company : PhysTech
Date : 2020-09-09
"""

def main():

    eiger = dict()

    try:
        while True:
            line = input().split()

            if line[0] == "define":
                eiger[line[2]] = int(line[1])
            elif line[0] == "eval":

                if line[1] not in eiger.keys() or line[-1] not in eiger.keys():
                    print("undefined")
                elif line[2] == "=":
                    if eiger[line[1]] == eiger[line[-1]]:
                        print("true")
                    else:
                        print("false")
                elif line[2] == ">":
                    if eiger[line[1]] > eiger[line[-1]]:
                        print("true")
                    else:
                        print("false")
                elif line[2] == "<":
                    if eiger[line[1]] < eiger[line[-1]]:
                        print("true")
                    else:
                        print("false")


    except Exception as e:
        pass

if __name__ == '__main__':
    main()