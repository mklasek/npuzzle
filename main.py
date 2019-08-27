from class_state import *
from class_list import *
from util import *
from class_stack import *
import math
import copy
import sys

#pro náročné úlohy
sys.setrecursionlimit(20000)


n = 3                                   #rozměr
stav0 = State(n, 0, None)               #náhodný počáteční stav
#stav0.array = [[2, 1, 4], [3, 6, 5],[7, 0, 8]]     #manuálně zadaný počáteční stav
#stav0.array = [[0, 1, 2], [3, 4, 5],[6, 7, 8]]

stav0.print()

#vyřešitelnost
ss = solvability(stav0)     #funkce v util.py
if not ss:
    print('State not solvable')
    input()
    sys.exit()

print('State solvable')
input()


goal = order(stav0)

#maximální velikost seznamů open, closed
size = 1000 * n**2      
Closed = List(size)
Open = List(size)

#zapsat počáteční stav do seznamu Open
Open.insert(stav0) 
opensize = 1   

while True:
    #je seznam Open prázdný?
    if opensize == 0:
        print('Solution doesn\'t exist')
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

    if statecmp(st, goal):
        print('Solution found')
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


    #print(opensize)

input()

#nalezení a vypsání cesty
path = Stack(st.g)
while True:
    st = copy.deepcopy(st.parent)
    if st.g == 0:
        print('Path found')
        break

    index = Closed.find(st)
    st = copy.deepcopy(Closed.array[index])
    path.push(st)
    #print(st.g)
    st.print()
    print('\n')



input()
