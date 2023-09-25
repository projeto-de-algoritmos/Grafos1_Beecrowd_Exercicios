from collections import defaultdict, deque

def bfs(grafo):
   visitados = set() 
   fila = deque([1])  
   total_convidados = 1  

   while fila:
      atual = fila.popleft()
      visitados.add(atual)

      for amigo in grafo[atual]:
         if amigo not in visitados:
            total_convidados += 1
            fila.append(amigo) 

   return total_convidados
   

def contar_convidados(relacoes):
   grafo = defaultdict(list)

   for x, y in relacoes:
      grafo[x].append(y)
      grafo[y].append(x)

   return bfs(grafo)

while True:
   n = int(input())
   if n == 0:
      break

   relacoes = []
   for _ in range(n):
      x, y = map(int, input().strip("()").split(","))
      relacoes.append((x, y))

   print(f"{contar_convidados(relacoes)} convidados")
