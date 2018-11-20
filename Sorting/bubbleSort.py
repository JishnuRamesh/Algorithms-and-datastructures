

def bubbleSort(lista):

    n = len(lista)

    for i in range(n-1, 0, -1):

        for j in range(i):

            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp


    return lista


alist = [54,26,93,17,77,31,44,55,20]
print(bubbleSort(alist))
