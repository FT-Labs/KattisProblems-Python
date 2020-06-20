x = 500
maxVal = 1000
minVal = 1
print(x)
while True:

    guess = input()

    if "lower" in guess:
        maxVal = int((maxVal+minVal)/2)
        x = int((maxVal+minVal)/2)
    elif "higher" in guess:
        minVal = x
        x = int((maxVal+minVal+1)/2)
    elif "correct" in guess:
        break
    print(x)






