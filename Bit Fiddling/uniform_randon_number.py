def uniform_random_number(lower_bound: int, upper_bound: int):
    
    possible_outcomes = upper_bound - lower_bound + 1
    
    while True:
        result, i = 0, 0
        
        while (1 << i) < possible_outcomes:
            result = result << 1 | zero_one_random()
            i += 1
            
        if result < possible_outcomes:
            break
            
        return result + lower_bound
            