import collections

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(row, col):
  
  q = collections.deque([(row, col)])

  while q:
    r, c = q.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if nr >= 0 and nr < n and nc >= 0 and nc < m and graph[nr][nc] == 1:
        q.append((nr,nc))
        graph[nr][nc] = graph[r][c] + 1


  return graph[n-1][m-1]

print(bfs(0,0))