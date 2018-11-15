


def compare(matrix,col,row,row_length, col_length):

    peak = True

    if col != 0:
        if matrix[row][col] < matrix[row][col-1]:
            return 0

    if col != col_length:
        if matrix[row][col] < matrix [row][col+1]:
            return 0

    if row != 0:
        if matrix[row][col] < matrix[row-1][col]:
            return 0

    if row != row_length:
        if matrix[row][col] < matrix[row+1][col]:
            return 0

    return ( matrix[row][col], row, col )


def peak_finder(matrix):

    row_length = len(matrix) - 1
    col_length = len(matrix[0]) - 1
    for row,row_element in enumerate(matrix):
        for col,col_element in enumerate(row_element):
            check = compare(matrix, col, row, row_length, col_length)
            if check == 0:
                continue
            else:
                return check


if __name__ == "__main__":
    problemMatrix = [
        [4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2],
        [5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3],
        [6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4],
        [7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5],
        [8, 9, 10, 11, 12, 11, 10, 9, 8, 7, 6],
        [7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5],
        [6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4],
        [5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3],
        [4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2],
        [3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]
    ]
    a = [[9]]
    print(peak_finder(problemMatrix))