#!/usr/bin/python


def isPrime(n):
    if n == 2:
        return True

    for i in range(2, int(n**.5)+1):
        if n%i == 0:
            return False

    return True


if __name__ == "__main__":
    p, b = map(int, input().split())

    while p != 0 and b != 0:

        if not isPrime(p):
            if pow(b, p, p) == b:
                print("yes")
            else:
                print("no")
        else:
            print("no")
        p, b = map(int, input().split())
