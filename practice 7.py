def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        fiz = []
        for j in range(m):
            fiz.append(value)
        matrix.append(fiz)
    return matrix
result = get_matrix(4, 1, 7)
result1 = get_matrix(5,1,8)
result2 = get_matrix(8,1,3)
print(result)
print(result1)
print(result2)







