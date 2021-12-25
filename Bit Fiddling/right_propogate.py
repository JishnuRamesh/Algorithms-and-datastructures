def right_propogate(x):
    """
        Right propogate the right most set bit
    :param x: number to propogate
    :return: Popogated number
    """
    return x | (x-1)