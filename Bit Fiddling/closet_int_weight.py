
# O(n)
def closet_int_weight(x):
    num_of_bits = 64

    for i in range(num_of_bits -1):
        if (x >> i) & 1 != (x >> i+1) & 1:
            x ^= (1<< i) | (1 << i+1)
            return x

    raise ValueError("All bits are either 0 or 1")