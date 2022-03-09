def add(list_a):
    list_a[-1] += 1
    
    for i in reversed(range(1, len(list_a))):
        if list_a[i] != 10:
            break
            
        list_a[i] = 0
        list_a[i-1] += 1
        
    if list_a[0] == 10:
        list_a[0] = 1
        list_a.append(0)
        
    return list_a