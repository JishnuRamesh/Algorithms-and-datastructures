
class map:

    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.value = [None] * self.size


    def put(self,key,value):

        probeIndex = 0
        hashValue = self.hash_function(key,len(self.keys), probeIndex)


        if self.keys[hashValue] == None or \
            self.keys[hashValue] == "X":

            self.keys[hashValue] = key
            self.value[hashValue] = value

        elif self.keys[hashValue] == key:
            self.value[hashValue] = value

        else:

            positionFound = False

            while not  positionFound:

                probeIndex += 1
                rehash = self.hash_function(key,len(self.keys),probeIndex)

                if self.keys[hashValue] == None or \
            self.keys[hashValue] == "X":
                    self.keys[hashValue] = key
                    self.value[hashValue] = value
                    positionFound = True

                elif self.keys[hashValue] == key:
                    self.value[hashValue] = value
                    positionFound = True


    def get(self,key):

        probeIndex = -1
        found = False

        while found != True and probeIndex < self.size:
            probeIndex += 1
            hashValue = self.hash_function(key, len(self.keys), probeIndex)

            if self.keys[hashValue] == None:
                return False

            elif self.keys[hashValue] == key:
                return self.value[hashValue]

            else:
                continue


    def delete(self,key):

        probeIndex = 0
        hashValue = self.hash_function(key,self.size,probeIndex)

        found = False
        stop = False
        inital = hashValue

        while  self.keys[hashValue] != None and not found and not  stop:

            if self.keys[hashValue] == key:
                self.keys[hashValue] = "X"
                found = True

            else:
                probeIndex += 1
                hashValue = self.hash_function(key,self.size,probeIndex)
                if hashValue == inital:
                    stop = True

        return found


    def hash_function(self,key,size, probeIndex):

        return ( (key % size) + probeIndex )

