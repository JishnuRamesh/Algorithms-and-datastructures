
def selectionSort(lista) :

    n = len(lista)

    for i in range(n-1, 0, -1):

        maxPos = 0

        for j in range(1, i+1):

            if lista[j] > lista[maxPos]:
                maxPos = j

        temp = lista[j]
        lista[j] = lista[maxPos]
        lista[maxPos] = temp

    return lista


alist = [54,26,93,17,77,31,44,55,20]
print(selectionSort(alist))