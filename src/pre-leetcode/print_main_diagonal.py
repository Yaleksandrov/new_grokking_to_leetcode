m = [
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
]

def print_main_diag(m):
    for row_idx in range(len(m)):
        for col_idx in range(len(m[row_idx])):
            if row_idx == col_idx:
                print(m[row_idx][col_idx], end = ' ')

print_main_diag(m)