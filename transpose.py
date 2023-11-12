# Transpose 2-D Maxtrix
test_in = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]
test_out = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [4, 7, 10]]

def transpose(matrix):
    transposed = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            transposed[j][i] = col
    
    return transposed

print(transpose(test_in) == test_out)