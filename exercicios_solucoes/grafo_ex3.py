
import math
import os
import random
import re
import sys
    
from collections import  deque


def quickestWayUp(ladders, snakes):
    
    grafo = {x: y for x, y in ladders + snakes}
    
    fila = deque([(1, 0)])
    
    visitado = [False] * 101

    while fila:
        no, jogadas = fila.popleft()
        if no == 100:
            return jogadas
        
        visitado[no] = True

        for i in range(1, 7):
            proximoNo = no + i

            if proximoNo <= 100 and not visitado[proximoNo]:
                if proximoNo in grafo:
                    fila.append((grafo[proximoNo], jogadas + 1))
                else:
                    fila.append((proximoNo, jogadas + 1))

    return -1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()

    


