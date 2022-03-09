def remove_duplicates(a:list):
    n = len(a)
    left = 0
    for right in range(1, n):
        if a[left] != a[right]:
            if left +1 != right:
                a[left+1] = a[right]
            left += 1
    return a


print(remove_duplicates([2,3,5,5,7,11,11,11,13]))
print(remove_duplicates([2,2,2,2,2,2,1]))


def remove_duplicates_v2(a:list):
    n = len(a)
    left = 0
    for right in range(1, n):
        if a[left] != a[right]:
            if left +1 != right:
                a[left+1] = a[right]
            left += 1
    return a, left+1


print(remove_duplicates_v2([2,2,2,2,2,2,1]))
print(remove_duplicates_v2([2,3,5,5,7,11,11,11,13]))


def remove_duplicates_v3(a:list):
    n = len(a)
    left = 0
    current_count = 1
    current_item = a[0]
    for right in range(1, n):
        if current_count >= 2 and a[left] != a[right] or left+2 < right:
            left += 1
            a[left] = a[right]
            current_item = a[left]
            current_count = 1

        elif a[left] != a[right]:
            current_item = a[right]
            current_count = 1
            left += 1

        elif current_item == a[right] and current_count < 2:
            left += 1
            current_count += 1

    return a

print(remove_duplicates_v3([1,2,2,2,2, 3,3,3,4,4,4,4,4,5,5, 5]))