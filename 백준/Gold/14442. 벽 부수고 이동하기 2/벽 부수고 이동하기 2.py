import sys
from collections import deque
read = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M, K = map(int, read().split())
graph = [ list(map(int,read().rstrip())) for _ in range(N) ]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K+1)]

def bfs(cnt,x,y):
  que = deque()
  que.append((cnt,x,y))
  visited[cnt][x][y] += 1

  while que:
    cnt,x,y = que.popleft()

    if x == N-1 and y == M-1:
      return visited[cnt][x][y]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] == 0 and visited[cnt][nx][ny] == 0:
          que.append((cnt,nx,ny))
          visited[cnt][nx][ny] = visited[cnt][x][y]+ 1
          
        if cnt < K and graph[nx][ny] == 1 and visited[cnt+1][nx][ny] == 0 : # 벽 부수기
          que.append((cnt+1,nx,ny))
          visited[cnt+1][nx][ny] = visited[cnt][x][y] + 1
          
  return -1

print(bfs(0,0,0)) 