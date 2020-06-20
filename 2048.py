matrix = []

for _ in range(4):
    matrix.append([int(x) for x in input().split(" ")])

direction = input()


def slideNumbers(m):
    for row in range(len(m)):
        swap = list()

        nums = [x for x in m[row] if x!= 0]
        for i in range(len(nums)):
            if i+1<len(nums):
                if nums[i] == nums[i+1]:
                    swap.append(2*nums[i])
                    nums[i+1] = 0
                elif nums[i] != 0:
                    swap.append(nums[i])
        if len(swap) != 0:
            swap.append(nums[-1])
            m[row][:len(swap)] = swap
            m[row][len(swap):] = [0 for _ in range(len(m)-len(swap))]
        else:
            m[row][:len(nums)] = nums
            m[row][len(nums):] = [0 for _ in range(len(m)-len(nums))]

    return m

def reverseMatrix(m):
    for row in range(len(m)):
        m[row] = list(reversed(m[row]))

    return m

if direction == '0':
    matrix = slideNumbers(matrix)
elif direction == '2':
    matrix = reverseMatrix(slideNumbers(reverseMatrix(matrix)))
elif direction == '1':
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    matrix = slideNumbers(matrix)
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
elif direction == '3':
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    matrix = reverseMatrix(slideNumbers(reverseMatrix(matrix)))
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for row in matrix:
    print(" ".join(map(str ,row)))

