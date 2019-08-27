from class_state import *
from class_list import *
import math

#heuristická funkce je součet vzdáleností všech "kamenů" od jejich finální pozice pošťáckou metrikou
def heur(state):
    if state == None:
        return math.inf
    h = 0

    for i in range(state.n):
        for j in range(state.n):
            if state.array[i][j] == 0:
                dif = (state.n - i - 1) + (state.n - j - 1)
            else:
                final_i = (state.array[i][j] - 1) // state.n
                final_j = (state.array[i][j] - 1) % state.n
                dif = abs(final_i - i) + abs(final_j - j)
            h = h + dif
    h = h + state.g

    return h



#expanze stavu
def expand(state):
    #libovolný stav může být rodičem maximálně 4 různých stavů
    successors = List(4)
    if state == None:
        return successors

    #nalezení 0
    i = 0
    j = 0
    for k in range(state.n):
        for l in range(state.n):
            if state.array[k][l] == 0:
                i = k
                j = l
                break
        else:
            continue
        break

    #0 nahoru
    if i != 0:
        succ = copy.deepcopy(state)
        succ.array[i][j] = succ.array[i - 1][j]
        succ.array[i - 1][j] = 0
        #rodič
        succ.parent = copy.deepcopy(state)
        #hloubka
        succ.g = state.g + 1
        successors.insert(succ)

    #0 dolů
    if i != state.n - 1:
        succ = copy.deepcopy(state)
        succ.array[i][j] = succ.array[i + 1][j]
        succ.array[i + 1][j] = 0
        succ.parent = copy.deepcopy(state)
        succ.g = state.g + 1
        successors.insert(succ)

    #0 doleva
    if j != 0:
        succ = copy.deepcopy(state)
        succ.array[i][j] = succ.array[i][j - 1]
        succ.array[i][j - 1] = 0
        succ.parent = copy.deepcopy(state)
        succ.g = state.g + 1
        successors.insert(succ)

    #0 doprava
    if j != state.n - 1:
        succ = copy.deepcopy(state)
        succ.array[i][j] = succ.array[i][j + 1]
        succ.array[i][j + 1] = 0
        succ.parent = copy.deepcopy(state)
        succ.g = state.g + 1
        successors.insert(succ)

    return successors


#vyřešitelnost
def solvability(state):
    K = -1

    for k in range(state.n):
        for l in range(state.n):
            if state.array[k][l] == 0:
                K = k + 1
                break
        else:
            continue
        break

    row = [None for i in range(state.n * state.n)]
    for i in range(state.n):
        for j in range(state.n):
            row[j + state.n * i] = state.array[i][j]
    
    N = 0
    for i in range(state.n * state.n):
        for j in range(state.n * state.n - i):
            if row[i + j] == 0:
                continue
            if row[i] > row[i + j]:
                N += 1

    print('K: ')
    print(K)
    print('N: ')
    print(N)
    if state.n % 2 == 0:
        if (K + N) % 2 == 0:
            return True
        else:
            return False
    else:
        if N % 2 == 0:
            return True
        else:
            return False

        




    

    

