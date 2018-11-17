


# https://techdevguide.withgoogle.com/resources/compress-decompression/#code-challenge
def compression(data, i = 0):


    n = len(data)

    if n < 1:
        return


    result = ""

    while i < n:

        if data[i] == '[':
            i += 1
            continue

        elif data[i].isnumeric():
            num = data[i]
            i += 1
            res, i = compression(data, i)
            for j in range(int(num)):
                result = result + res


        elif data[i].isalpha():
            result = result + data[i]
            i += 1

        elif data[i] == ']':
            return result, i+1

    return  result , i+1



print(compression("3[abc]4[ab]c"))

