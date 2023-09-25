from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(inicio, fim):
   x1, y1 = ord(inicio[0]) - ord('a') + 1, int(inicio[1])
   x2, y2 = ord(fim[0]) - ord('a') + 1, int(fim[1])

   visitados = [[False] * 9 for _ in range(9)]
   fila = deque([(x1, y1, 0)])

   while fila:
      x, y, movimentos_cavalo = fila.popleft()

      if x == x2 and y == y2:
         return movimentos_cavalo

      for i in range(8):
         nx, ny = x + dx[i], y + dy[i]
         if valido_no_tabuleiro(nx, ny) and not visitados[nx][ny]:
            visitados[nx][ny] = True
            fila.append((nx, ny, movimentos_cavalo + 1))

def valido_no_tabuleiro(x, y):
   return 1 <= x <= 8 and 1 <= y <= 8

while True:
   try:
      inicio, fim = input().split()
      movimentos_cavalo = bfs(inicio, fim)
      print(f"To get from {inicio} to {fim} takes {movimentos_cavalo} knight movimentos_cavalo.")
   except EOFError:
      break
