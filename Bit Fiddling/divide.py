def divide(x: int, y: int):
    result, power = 0, 32
    y_power = y << power
    
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
            
        result += 1 << power
        x -= y_power
        
    return result


def divide_v2(dividend, divisor):

    max_int = 2**31 - 1
    min_int =-2**31 - 1
    half_min_int = -min_int//2

    if dividend == min_int and divisor == -1:
        return max_int

    negatives = 0
    if dividend > 0:
        negatives += 1
        dividend = -dividend
    if divisor > 0:
        negatives += 1
        divisor = -divisor

    power = []
    doubles = []

    power_of_two = 1
    while divisor >= dividend:
        doubles.append(divisor)
        power.append(power_of_two)

        if divisor < half_min_int:
            break

        divisor += divisor
        power_of_two += power_of_two


    quotient = 0

    for i in reversed(range(len(doubles))):
        if doubles[i] >= dividend:
            quotient += power_of_two[i]
            dividend -= doubles[i]

    return  quotient if negatives != 1 else -quotient