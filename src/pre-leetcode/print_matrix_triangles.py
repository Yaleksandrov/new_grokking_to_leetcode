m = [
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
]


def print_lover_triangle(m):
    for row_idx in range(len(m)):
        for col_idx in range(len(m[row_idx])):
            if col_idx <= row_idx:
                print(m[row_idx][col_idx], end= ' ')

print_lover_triangle(m)

# (0, 2) (1, 1) (2, 0) -> (0, 2-0), (1, 2-1), (2, 2-2) -> (row, len(m[row])-1-row)

print("\n**********************\n")

def print_opposite_diag(m):
    for row_idx in range(len(m)):
        for col_idx in range(len(m[row_idx])):
            if col_idx == len(m[row_idx]) - 1 - row_idx:
                print(m[row_idx][col_idx], end = ' ')
                
print_opposite_diag(m)

print("\n**********************\n")

def print_upper_triangle(m):
    for row_idx in range(len(m)):
        for col_idx in range(len(m[row_idx])):
            if col_idx >= len(m[row_idx]) - 1 - row_idx:
                print(m[row_idx][col_idx], end= ' ')

print_upper_triangle(m)