def can_reach(a:list):
    
    n = len(a)
    if not a:
        return False
    
    def backtrack(current):
        if current == n-1:
            return True
    
        for i in range(a[current], 0, -1):
            if backtrack(current+i):
                return True
            
            
        return False
    
    return backtrack(0)



print(can_reach([3,2,0,0,2,0,1]))
