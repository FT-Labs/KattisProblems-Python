from collections import Counter


d1,d2 = [int(x) for x in input().split()]
x = [x for x in range(1,d1+1)]
y = [x for x in range(1,d2+1)]



n = []

for i in x:
    for j in y:
        n.append(i+j)

n = Counter(n)

for i in n.most_common():
    if i[1] == n.most_common(1)[0][1]:
        print(i[0])
    else:
        break


