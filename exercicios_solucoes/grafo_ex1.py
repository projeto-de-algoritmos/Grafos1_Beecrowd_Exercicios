def dfs(grafo, vertice, visitados, componente):
   visitados[vertice] = True
   componente.append(vertice)
   for vizinho in grafo[vertice]:
      if not visitados[vizinho]:
         dfs(grafo, vizinho, visitados, componente)

def procura_componentes_conectados(grafo, vertices):
    visitados = {vertice: False for vertice in vertices}
    componentes = []
    
    for vertice in vertices:
        if not visitados[vertice]:
         componente = []
         dfs(grafo, vertice, visitados, componente)
         componentes.append(componente)
    
    return componentes

def main():
   N = int(input())
   
   for case in range(1, N + 1):
      V, E = map(int, input().split())
      grafo = {chr(ord('a') + i): [] for i in range(V)}
      
      for _ in range(E):
         u, v = input().split()
         grafo[u].append(v)
         grafo[v].append(u)
      
      vertices = sorted(grafo.keys())
      componentes = procura_componentes_conectados(grafo, vertices)
      
      print(f'Case #{case}:')
      for componente in componentes:
         print(','.join(sorted(componente)) + ',')
      print(f'{len(componentes)} connected components\n')

if __name__ == "__main__":
   main()
