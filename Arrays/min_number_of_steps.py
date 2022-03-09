def can_reach(a: list):
    n = len(a)
    if not a:
        return False

    def backtrack(current, count=0):
        if current == n - 1:
            return True, count

        for i in range(a[current], 0, -1):
            count += 1
            res = backtrack(current + i, count)
            if res[0]:
                return res[0], res[1]

            count -= 1
        return False, -1

    return backtrack(0)


print(can_reach([3, 0, 1, 0, 2, 0, 1]))
