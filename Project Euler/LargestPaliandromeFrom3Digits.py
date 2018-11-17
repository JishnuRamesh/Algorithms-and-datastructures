
from collections import deque

#find the largest palindrome made from the product of two 3-digit numbers.
def largestPaliandromeFromThreeDigitNumber():

    first = 999
    second = 999
    pals = []

    found = False

    while  first > 99:

        for i in range(first, 100, -1):


            num = first * i

            num = str(num)

            queue = deque()

            for item in num:
                queue.appendleft(item)

            #print(queue)

            pal = True

            while len(queue) > 1 and pal :
                if queue.pop() != queue.popleft():
                    pal = False

            if pal:
                pals.append(int(num))
                break

        first = first -1

    print(max(pals))



largestPaliandromeFromThreeDigitNumber()