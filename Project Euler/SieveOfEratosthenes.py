def primeFinder(n):

    numberList = [True] * (n+1)

    numberList[0] = False
    numberList[1] = False

    for i in range(2,n):
        j = i
        while i* j <= n :
            numberList[i*j] = False
            i += 1




    ans = []

    for i in range(len(numberList)):
        if numberList[i] == True:
            ans.append(i)

    print(ans)


primeFinder(100)