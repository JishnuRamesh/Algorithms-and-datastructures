import  math

def largestPrime(n):

    prime = set()

    while n % 2 == 0:
        prime.add(2)
        n = n/2

    for i in range(3, int (math.sqrt(n)+1 ) , 2) :

        while n % i == 0 :
            prime.add(i)
            n = n / i

     # Not needed for this question
    if n > 2:
        prime.add(n)


    print(max(prime))



largestPrime(12345678)