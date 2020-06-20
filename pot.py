rep = int(input())

total = 0
for i in range(rep):
    num = input()
    total += int(num[:-1])**int(num[-1])

print(total)