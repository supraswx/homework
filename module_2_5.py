def get_matrix(n, m, value):
    matrix = []
    for i in range(1, n + 1):
        a = []
        matrix.append(a)
        for j in range(1, m + 1):
            a.append(value)
    print(matrix)

result1 = get_matrix(2, 4, 10)
result2 = get_matrix(6, 3, 2)
result3 = get_matrix(5, 2, 52)