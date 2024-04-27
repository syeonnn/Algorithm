import sys
from collections import deque
input = sys.stdin.readline

# n행 m열
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
surr = [[0 for _ in range(m)] for _ in range(n)]

def bfs(x,y):
  que = deque()
  que.append((x,y))
  visited[x][y] = 1
  
  while que:
    x,y = que.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 0:
          visited[x][y] += 1
          
        if graph[nx][ny] != 0 and visited[nx][ny] == 0:
          visited[nx][ny]  = 1
          que.append((nx,ny))
  
time = 0
while True:
  visited = [[0 for _ in range(m)] for _ in range(n)]
  cnt = 0
  
  # 빙산 탐색
  # 1차 : 주변에 바닷물 접한 정도 현황 조사
  # n차 : 빙산이 녹으면서 분리되는지 여부 조사
  for i in range(n):
    for j in range(m):
      if graph[i][j] != 0 and visited[i][j] == 0:
        bfs(i,j)
        cnt += 1

  for i in range(n):
    for j in range(m):
      if graph[i][j] != 0:
        graph[i][j] -= (visited[i][j]-1)
        if graph[i][j] < 0: graph[i][j] = 0

  time += 1
  
  if cnt >= 2: # 덩어리 2개 이상
    break
  if cnt == 0: # 얼음 모두 녹음
    print(0)
    exit()
 
print(time-1)