try:
    names = []
    while True:
        data = input().split()
        tot = 0.0
        cnt = 0
        name = ""
        for i in data:
            try:
                tot += float(i)
                cnt += 1
            except:
                name += i + " "
        name = name.strip(" ")
        tot /= cnt
        names.append((name,tot))
except:
    for i in names:
        print("{:.6f} {}".format(i[1],i[0]))



