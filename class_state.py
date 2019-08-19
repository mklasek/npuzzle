import random
import class_stack
import copy

class State:
    
    #int n... rozměr
    #int g... hloubka
    #State parent... rodič
    #array[][]... vyjádření stavu

    def __init__(self, n, g, par):
        self.parent = par
        self.n = n
        self.g = g
        self.array = [[0 for i in range(n)] for i in range(n)]

        numbers = class_stack.Stack(n * n)
        for i in range(n * n):
            numbers.push(i)
        random.shuffle(numbers.stack)

        for i in range(n):
            for j in range(n):
                self.array[j][i] = numbers.pop()
        

    def print(self):
        row = ""
        for i in range(self.n):
            for j in range(self.n):
                if self.array[i][j] >= 10:
                    row = row + " " + str(self.array[i][j])
                else:
                    row = row + "  " + str(self.array[i][j])

            print(row)
            row = ""

##############################################################################
#porovnání stavů (==)
def statecmp(state1, state2):
    if state1 == None or state2 == None:
        return False
    if state1.n != state2.n:
                print('Incomparable')
                return False
           
    for i in range(state1.n):
        for j in range(state1.n):
            if state1.array[i][j] != state2.array[i][j]:
                return False
    else:
        return True

#seřazení
def order(state):
        cc = copy.deepcopy(state)
        numbers = class_stack.Stack(cc.n * cc.n)
        
        for i in range(cc.n * cc.n):
            numbers.push(cc.n * cc.n - i)

        for i in range(cc.n):
            for j in range(cc.n):
                cc.array[i][j] = numbers.pop()

        cc.array[cc.n - 1][cc.n - 1] = 0
        return cc







    






