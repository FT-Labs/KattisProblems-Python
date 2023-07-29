#!/usr/bin/python



def rotate_90_degree_clckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)

    return new_matrix

r = int(input())

while r != 0:
    m = []
    mx = 0

    for i in range(r):
        l = [_ for _ in input()]
        for x in range(len(l)):
            if l[x] == '-':
                l[x] = '|'
            elif l[x] == '|':
                l[x] = '-'


        mx = max(mx, len(l))
        m.append(l)

    for i in m:
        while len(i) != mx:
            i.append(" ")


    m = rotate_90_degree_clckwise(m)

    for i in m:
        print("".join(i).rstrip(" "))
    r = int(input())

    if r != 0:
        print()
