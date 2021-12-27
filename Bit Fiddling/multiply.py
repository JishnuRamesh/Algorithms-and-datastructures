def mult(x: int, y: int):
    
    def add(a: int, b: int):
        while b:
            a, b = a ^ b, (a & b) << 1
            
        return a
    
    running_sum = 0
    while x:
        
        if x & 1:
            running_sum = add(running_sum, y)
            
        x, y = x >> 1, y << 1
