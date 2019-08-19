from class_state import *

class List:
    array = []


    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]

    def print(self):
        print(self.array)

    def insert(self, item):
        i = 0
        while not self.array[i] == None:
            if i == self.size - 1:
                print('List is full')
                return False
            i = i + 1
        self.array[i] = item
        return True

    def find(self, item):
        if not isinstance(item, State):
            return False
        found = False
        i = 0
        while not found:
            if i == self.size - 1:
                #print('item not found')
                return False
            if self.array[i] == None:
                i += 1
                continue
            if statecmp(self.array[i], item):
                found = True
                return i
            i += 1

    def remove(self, item):
        if not isinstance(item, State):
            return False
        i = 0
        while not statecmp(self.array[i], item):
            if i == self.size - 1:
                print('item not found')
                return False
            i = i + 1

        self.array[i] = None
        return True

    def remove_at(self, index):
        self.array[index] = None
        
    

    