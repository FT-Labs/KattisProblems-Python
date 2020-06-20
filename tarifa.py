megabyte = int(input())
months = int(input())

ans = 0

while months>0:
    curmb = int(input())
    ans += megabyte - curmb
    months -= 1

print(ans+megabyte)