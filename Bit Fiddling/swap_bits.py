def swap_bits(x, i, j):
    if ((x >> i) & 1) != ((x >> j) & 1):
        mask = (i << i) | (1 << j)
        x ^= mask
        
    return x

