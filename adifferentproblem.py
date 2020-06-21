while True:
    try:
        x,y = input().split(" ")
        if int(x)>=int(y):
            print(int(x)-int(y))
        else:
            print(int(y)-int(x))
    except EOFError:
        break
