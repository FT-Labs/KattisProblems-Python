rep = int(input())

qaly = 0.
for i in range(rep):
    x = [float(y) for y in input().split(" ")]
    qaly += x[0]*x[1]

print(qaly)
