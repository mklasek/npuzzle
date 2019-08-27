from class_state import *

#seznam

class List:
    array = []

    #konstr.
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]

    def print(self):
        print(self.array)

    #vložit do seznamu
    def insert(self, item):
        i = 0
        while self.array[i] != None:
            if i == self.size - 1:
                return False        #seznam je plný
            i += 1
        self.array[i] = item
        return True

    #najít v seznamu
    def find(self, item):
        if not isinstance(item, State):
            return False
        found = False
        i = 0
        while not found:
            if i == self.size - 1:
                return False        #nenalezeno
            if self.array[i] == None:
                i += 1
                continue
            if statecmp(self.array[i], item):
                found = True
                return i
            i += 1

    #najít a vyjmout ze seznamu
    def remove(self, item):
        if not isinstance(item, State):
            return False
        i = 0
        while not statecmp(self.array[i], item):
            if i == self.size - 1:
                return False    #nenalezeno
            i = i + 1

        self.array[i] = None
        return True

    #vyjmout ze seznamu
    def remove_at(self, index):
        self.array[index] = None
        
    

    