def true_ordering(list_a):
    last_true = len(list_a) - 1

    for i in range(last_true, -1, -1):
        if list_a[i]:
            list_a[last_true], list_a[i] = list_a[i], list_a[last_true]
            last_true -= 1

    return list_a


print(true_ordering([False, True, True, False, True, False, True]))