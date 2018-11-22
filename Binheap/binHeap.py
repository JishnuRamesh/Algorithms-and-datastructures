

class Binheap:

    def __init__(self):
        self.heapList = [0]
        self.size = 0



    # Percup and maintain the bin heap structure
    def percUp(self,i):

        while i//2 > 0 :

            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = temp

            i = i// 2



    # O(log n)
    def insert(self, value):
        self.heapList.append(value)
        self.size += 1
        self.percUp(self.size)


    def percDown(self, i):

        while i*2 <= self.size:

            # Needs to find the minimum child to percolate down
            mc = minChild(i)
            if self.heapList[i] < self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp

            i = mc


    def minChild(self, i):

        if  (2*i + 1) > self.size:
            return  2*i
        else:
            if self.heapList[2*i] < self.heapList[2*i + 1]:
                return 2*i
            else:
                return  2*i + 1


    # O(log n)
    def delMin(self):
        retVal = self.heapList[i]
        self.size -= 1
        self.heapList[1] = self.heapList[self.size]
        self.heapList.pop()
        self.percDown(1)
        return retVal


    # Builds a heap from a list in O(n). Used for heap sort as well. That will take O(nlogn)
    def buildHeap(self, alist):
        i =len(alist) // 2
        self.size = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0 :
            self.percDown(i)
            i -= 1