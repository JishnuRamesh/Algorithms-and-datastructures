
def insertionSort(lista):

    n = len(lista)


    for i in range(1, n):

        currentValue = alist[pos]
        pos = i

        while pos > 0 and alist[pos-1] > currentValue:
            alist[pos] = alist[pos-1]
            pos = pos-1

        alist[pos] = currentValue


    return lista



alist = [54,26,93,17,77,31,44,55,20]
print(insertionSort(alist))