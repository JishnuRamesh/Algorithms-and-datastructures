
def mergeSort(lista):

    if len(lista) > 1:

        mid = len(lista) // 2

        leftHalf = lista[:mid]
        rightHalf = lista[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)


        i=0
        j=0
        k=0

        while i < len(leftHalf) and j < len(rightHalf):

            if leftHalf[i] < rightHalf[j]:
                lista[k] = leftHalf[i]
                i = i+ 1

            else:
                lista[k] = rightHalf[j]
                j = j+1
            k = k+1

        while i < len(leftHalf):
            lista[k] =  leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            lista[k] = rightHalf[j]
            j += 1
            k += 1


lista = [54,26,93,17,77,31,44,55,20]
mergeSort(lista)
print(lista)

