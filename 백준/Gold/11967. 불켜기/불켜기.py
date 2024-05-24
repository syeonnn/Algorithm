from collections import deque
import sys

input = sys.stdin.readline

# 초기세팅
N, M = map(int, input().split())
graph = [[[] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
  x, y, a, b = map(int, input().split())
  graph[x][y].append((a,b))

light = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [[0 for _ in range(N+1)] for _ in range(N+1)]

def bfs(x,y):
  cnt = 1
  # 시작 지점
  que = deque()
  que.append((x,y))
  light[x][y] = 1
  visited[x][y] = 1
  for a, b in graph[x][y]:
    if not light[a][b]:
      light[a][b] = 1
      cnt += 1

  while que:
    x,y = que.popleft()
    for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
      nx, ny = x + dx, y + dy
      if 0 < nx <= N and 0 < ny <= N and not visited[nx][ny] and light[nx][ny] == 1:
        visited[nx][ny] = 1 # 방문 처리 + 접근 가능한 위치임을 표시
        que.append((nx,ny))
        
        for a, b in graph[nx][ny]: # 스위칭 가능한 방 불 키기
          if not light[a][b]:
            light[a][b] = 1
            cnt += 1
          # 새로 불이 켜진 방으로 진입할 수 있는 방, 큐에 넣기 => 재탐색
          for da, db in [(-1,0),(1,0),(0,1),(0,-1)]:
            na, nb = a + da, b + db
            if 0 < na <= N and 0 < nb <= N and visited[na][nb] and light[na][nb] == 1:
              que.append((na,nb))

  return cnt      

print(bfs(1,1))