def reverse_digits(x: int):

    result, x_remaining = 0, abs(x)

    while x_remaining:
        result, x_remaining = result*10 + x_remaining % 10, x_remaining//10

    return result if x > 0 else -result
