"""
Author : Arda
Date : 7/27/2020
"""


def main():

    for _ in range(int(input())):
        total,absDiff = [int(x) for x in input().split()]

        large = (total+absDiff)//2
        small = total-large

        if large*2 == absDiff+total and small>=0:
            print("{} {}".format(large,small))
        else:
            print("impossible")


if __name__ == "__main__":
    main()