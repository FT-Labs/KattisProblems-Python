contestants = []

for i in range(5):
    contestants.append(sum([int(x) for x in input().split(" ")]))

print(f"{contestants.index(max(contestants))+1} {max(contestants)}")