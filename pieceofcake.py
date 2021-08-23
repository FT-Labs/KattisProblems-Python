sizes = [int(i) for i in input().split(" ")]

volume = 1

if sizes[1]>=sizes[0]/2:
    volume *= sizes[1]
else:
    volume *= sizes[0]-sizes[1]
if sizes[2]>=sizes[0]/2:
    volume *= sizes[2]
else:
    volume *= sizes[0]-sizes[2]

print(volume*4)

