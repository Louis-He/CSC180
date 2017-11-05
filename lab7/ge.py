# D.2. python CODE
def ge_fw(matrix):
    if len(matrix) == 0:
        return [-1, matrix]


    for i in range(0, len(matrix)):
        co = (float)(matrix[i][i])
        if co == 0:
            temp = matrix[len(matrix) - 1]
            matrix[len(matrix) - 1] = matrix[i]
            matrix[i] = temp
            co = (float)(matrix[i][i])

        for j in range(i + 1, len(matrix)):
            number = (float)(matrix[j][i])
            c = (float)(number / co)

            for k in range(i, len(matrix[j])):
                matrix[j][k] = matrix[j][k] - (matrix[i][k] * c);

    return [0, matrix]

#def ge_bw(matrix):