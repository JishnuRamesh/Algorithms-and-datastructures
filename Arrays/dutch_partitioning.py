def pivot(pivot_index: int, list_a: list):
    pivot = list_a[pivot_index]

    lower, equal, higher = 0, 0, len(list_a) - 1

    while equal < higher:

        if list_a[equal] < pivot:
            list_a[lower], list_a[equal] = list_a[equal], list_a[lower]
            equal += 1
            lower += 1

        elif list_a[equal] == pivot:
            equal += 1

        else:
            list_a[equal], list_a[higher] = list_a[higher], list_a[equal]
            higher -= 1

    return  list_a


print(pivot(3, [0,1,2,0,2,1,1]))
