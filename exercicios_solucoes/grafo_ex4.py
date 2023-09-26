

import math
import os
import random
import re
import sys


def roadsAndLibraries(n, bibliotecas, estradas, cidades):

    grafo = [[] for i in range(n + 1)]
    for x, y in cidades:
        grafo[x].append(y)
        grafo[y].append(x)
        
    custo_total = 0 
    visitado = [False] * (n + 1)
    
    def dfs(u, grafo, visitado):
        visitado[u] = True
        n_cidades = 1 
        for v in grafo[u]:
            if visitado[v] == False:
                n_cidades += dfs(v, grafo, visitado)
        return n_cidades
    
    for v in range(1, n + 1):
        if visitado[v] == False:
            n_cidades = dfs(v, grafo, visitado)
            custo1 = (n_cidades-1) * estradas + bibliotecas
            custo2 = n_cidades * bibliotecas
            custo_total += min(custo1, custo2)
            
    return custo_total

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        bibliotecas = int(first_multiple_input[2])

        estradas = int(first_multiple_input[3])

        cidades = []

        for _ in range(m):
            cidades.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, bibliotecas, estradas, cidades)

        fptr.write(str(result) + '\n')

    fptr.close()
