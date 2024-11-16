m = [
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
]


# Transpose

mm = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

def transpose(m):
    for row_idx in range(len(m)):
        for col_idx in range(len(m[row_idx])):
            if row_idx < col_idx:
                m[row_idx][col_idx], m[col_idx][row_idx] = m[col_idx][row_idx], m[row_idx][col_idx]
    return m

z = transpose(m)

print(z)