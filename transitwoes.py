times = [int(i) for i in input().split(" ")]
walktimes = [int(i) for i in input().split(" ")]
bustimes = [int(i) for i in input().split(" ")]
busintervals = [int(i) for i in input().split(" ")]

total = 0
for x in range(times[-1]):

    walktime = walktimes[x]
    bustime = bustimes[x]
    businterval = busintervals[x]

    if walktime<=businterval:
        total += businterval
    else:
        total = total + (walktime//businterval)*businterval

    total += bustimes[x]

total += walktimes[-1]

if total<= times[1]:
    print("yes")
else:
    print("no")
