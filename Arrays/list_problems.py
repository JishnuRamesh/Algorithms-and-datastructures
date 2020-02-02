
def array_game(lista):

    if len(lista) < 0 or lista[0] == 0:
        return False

    if len(lista) == 1 :
        return True

    else:
        possible = False
        while not possible and lista[0] > 0:
            try:
                possible = array_game(lista[lista[0]:])
            except IndexError:
                pass
            lista[0] = lista[0] - 1

        return possible

