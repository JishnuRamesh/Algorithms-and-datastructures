def mult(a:list, b:list):

    sign = -1 if (a[0] < 0 ^ b[0] < 0) else 1

    a[0], b[0] = abs(a[0]), abs(b[0])
    result = [0] * (len(a)+ len(b))

    for i in reversed(range(len(a))):
        for j in reversed(range(len(b))):

            result[i+j+1] += a[i] * b[j]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] %=  10


    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


