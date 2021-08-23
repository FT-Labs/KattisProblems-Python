y = int(input())

while y != -1:
    currentTime = 0
    totalKm = 0
    for _ in range(y):
        km , time = [int(x) for x in input().split()]
        distTime = time - currentTime
        currentTime = time
        totalKm += distTime * km

    y = int(input())
    print(f"{totalKm} miles")