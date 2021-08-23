text = input().split(" ")
repBool = False
for i in range(len(text)):
    y = text[i]
    for x in range(len(text)):
        if i==x:
            pass
        else:
            if y==text[x] and not  repBool:
                print("no")
                repBool = True
                break


if not repBool:
    print("yes")
