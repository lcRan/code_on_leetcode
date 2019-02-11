def SprialMaxtrix(matrix):
    ret = []
    rows = len(matrix)
    if rows == 0:
        return  ret
    cols = len (matrix[0])
    i, j = 0, 0
    while (rows > 0) and (cols > 0):
        for k in range (j, j + cols):
            ret.append(matrix[i][k])
        if rows > 1:
            for k in range (i + 1, i + rows):
                ret.append(matrix[k][j + cols - 1])
            if cols > 1:
                for k in range (j + cols - 2, j - 1, -1):
                    ret.append(matrix[i + rows - 1][k])
                for k in range (i + rows - 2, i, -1):
                    ret.append(matrix[k][j])
        rows -= 2
        cols -= 2
        i += 1
        j += 1
    return ret

print (SprialMaxtrix([]))
print (SprialMaxtrix([[1]]))
print (SprialMaxtrix([[1, 2, 3],[4, 5, 6]]))
print (SprialMaxtrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))