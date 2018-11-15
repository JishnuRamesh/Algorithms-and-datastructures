

def one_peak_finder(matrix):

    n = len(matrix)

    mid = n // 2
    start = 0
    end = n - 1

    while start < mid and end > mid:

        if matrix[mid] < matrix[mid+1]:
            start = mid+1
            mid = (start + end ) //2

        elif matrix[mid] < matrix[mid-1]:
            end = mid-1
            mid = (start + end) // 2

        else:
            return (mid,matrix[mid])

    if matrix[start] > matrix[end]:
        return  (start,matrix[start])
    else:
        return (end,matrix[end])



def peak_finder(matrix):
    row_end = len(matrix) - 1
    col_end = len(matrix[0]) -1
    col_start = 0
    row_start = 0
    col_mid =  (col_start+col_end) // 2


    while col_start < col_mid:
        new_list = []
        for i in range(row_end+1):
            new_list.append(matrix[i][col_mid])
        (row,element) = one_peak_finder(new_list)

        if matrix[row][col_mid] < matrix[row][col_mid-1]:
            col_end = col_mid-1
            col_mid = (col_start+col_mid) // 2

        elif matrix[row][col_mid] < matrix[row][col_mid+1]:
            col_start = col_mid+1
            col_mid = ( col_start + col_end ) // 2

        else:
            return (row,col_mid,matrix[row][col_mid])


    if col_start == col_mid and col_start != col_end:
        new_list = []
        for i in range(row_end+1):
            new_list.append(matrix[i][col_mid])
        (row,element) = one_peak_finder(new_list)

        if matrix[row][col_start] < matrix[row][col_start+1]:
            col_start = col_start+1
            col_mid = col_mid + 1

        else:
            return (row,col_mid,matrix[row][col_mid])

    new_list = []
    for i in range(row_end+1):
        new_list.append(matrix[i][col_mid])
    (row, element) = one_peak_finder(new_list)
    return (row, col_mid, matrix[row][col_mid])


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
    #a = [[9,11],[0,0]]
    print(peak_finder(problemMatrix))