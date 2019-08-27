from class_state import *
from class_list import *
from utility import *
import math
import copy
import time
import sys

sys.setrecursionlimit(20000)


n = 3                           #velikost
stav0 = State(n, 0, None)       #náhodný počáteční stav
stav0.print()

#vyřešitelnost
ss = solvability(stav0)
if not ss:
    print('Nevyřešitelná konfigurace')
    sys.exit()

input()



cil = order(stav0)

size = 1000 * n**2
Closed = List(size)
closedsize = 0
Open = List(size)

#zapsat počáteční stav do seznamu Open
Open.insert(stav0) 
opensize = 1   

while True:
    if opensize == 0:
        print('Řešení neexistuje')
        break

    #nalezení nejlepšího stavu v seznamu Open
    fmin = math.inf
    i = 0
    searched = 0
    while searched < opensize:
        if Open.array[i] == None:
            i += 1
            continue 

        h = heur(Open.array[i])
        if h < fmin:
            fmin = h
            index = i
        searched += 1
        i += 1

    st = copy.deepcopy(Open.array[index]) 
    Open.remove(st)
    opensize -= 1
    Closed.insert(st)

    if statecmp(st, cil):
        print('Řešení nalezeno')
        break

    #expanze stavu
    successors = expand(st) 

    #vložení následníků do seznamu Open
    for i in range(4):
        if successors.array[i] != None:
            opind = Open.find(successors.array[i]) 
            clind = Closed.find(successors.array[i])

            #není ani v jednom seznamu
            if not opind and not clind:
                Open.insert(successors.array[i]) 
                opensize += 1

            #je v seznamu Open
            elif opind != False:
                if heur(Open.array[opind]) > heur(successors.array[i]):
                    Open.array[opind] = copy.deepcopy(successors.array[i])
                if heur(Open.array[opind]) == heur(successors.array[i]) and Open.array[opind].g > successors.array[i].g:
                    Open.array[opind] = copy.deepcopy(successors.array[i])

            #je v seznamu Closed
            elif clind != False:
                if heur(Closed.array[opind]) > heur(successors.array[i]):
                    Closed.remove_at(clind)
                    Open.insert(successors.array[i])
                    opensize += 1


    print(opensize)


print('end')





    

















