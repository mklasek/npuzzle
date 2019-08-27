#zásobník

class Stack:
    stack = []
    length = 0

    #konstr.
    def __init__(self, length):
        self.stack = [None] * length
        self.length = length

    #vložit do zásobníku
    def push(self, member):
        if self.stack[0] == None:
            self.stack[0] = member
            return True
        else:
            for i in range(self.length):
                if self.stack[i] == None:
                    break
            else:
                print('Stack is full')
                return False

            for j in range(i):
                self.stack[i - j] = self.stack[i - j - 1] 
            self.stack[0] = member
            return True

    #odebrat ze zásobníku
    def pop(self):                                 
        ret = self.stack[0]
        i = 0
        while self.stack[i] != None and i < self.length - 1:
            if i == self.length - 1:
                self.stack[i] = None
                return ret
            self.stack[i] = self.stack[i + 1]
            i = i + 1

        self.stack[i] = None

        return ret


    def print(self):
        print(self.stack)


