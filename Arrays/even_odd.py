
# O(n) time
# O(1) space
def even_odd(a: List[int]):
    next_even, next_odd = 0, len(a) -1
    
    while next_even < next_odd:
        if a[next_even] % 2 == 0:
            next_even += 1
        else:
            a[next_even], a[next_odd] = a[next_odd], a[next_even]
            next_odd -= 1
            
    return a

