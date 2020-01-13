

# O(1) * n = O(n)
def count_bits(num):
    num_of_ones = 0
    while num:
        num_of_ones += num & 1
        num >>= 1
    return num_of_ones


# O(1) * n = O(n)
def parity(num):
    number_parity = 0
    while num:
        number_parity ^= num & 1
        num >>= 1
    return number_parity


# O(1) * k = O(k)
def parity_drop_first_set_bit(num):
    num_of_parity = 0
    while num:
        num_of_parity ^= num & 1
        num &= (num-1)
    return num


# Assuming parity has been precomputed in Precomputed parity for 16 bit words
# if L is the size of the word for which parity was precomputed and n is the word size
# run time is O(n/L)
Precomputed = {}
def parity_precomputed(num):
    mask = 16
    bit_mask = 0xFFFF
    return ( Precomputed[num >> mask * 3] ^
             Precomputed[(num >> mask * 2) & bit_mask] ^
             Precomputed[(num >> mask * 1) & bit_mask] ^
             Precomputed[num & bit_mask] )


def divide_and_conquer_parity(num, mask=48):
    if num == 1 or num == 0:
        return num
    else:
        return (divide_and_conquer_parity((num >> mask), mask=mask//2) ^
                divide_and_conquer_parity((num & mask), mask=mask // 2))