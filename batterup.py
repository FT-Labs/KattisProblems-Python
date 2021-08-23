div = int(input())
scores = input().split(" ")

total = 0.

for i in scores:
    if int(i)==-1:
        div -= 1
    else:
        total += int(i)

print(total/div)
