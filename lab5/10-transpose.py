def transpose(matrix):
    res = []
    for j in range(len(matrix)):
        t = []
        for i in range(len(matrix[0])):
            t = t + [matrix[i][j]]
        res = res + [t]
    return res
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = transpose(matrix)
for line in matrix:
    print(*line)