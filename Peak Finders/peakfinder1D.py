
# One Dimensional peak finder
def one_peak_finder(matrix):

    n = len(matrix)

    mid = n // 2
    start = 0
    end = n - 1


    while start < mid and end > mid:

        # Check if peak is on the right side
        if matrix[mid] < matrix[mid+1]:
            start = mid+1
            mid = (start + end ) //2

        # Check iff the peak is on the left
        elif matrix[mid] < matrix[mid-1]:
            end = mid-1
            mid = (start + end) // 2

        # We found the peak
        else:
            return (mid,matrix[mid])

    if matrix[start] > matrix[end]:
        return  (start,matrix[start])

    else:
        return (end,matrix[end])





if __name__ == "__main__":

    x = [1,2,3,4,5]
    print(x)
    ans = one_peak_finder(x)
    print(ans)