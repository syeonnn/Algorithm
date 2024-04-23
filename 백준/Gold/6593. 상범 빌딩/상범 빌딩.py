# 상범 빌딩
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

# bfs_최단 시간
def bfs(x,y,z):
  que = deque()
  que.append((x,y,z))
  count[x][y][z] = 1
  
  while que:
    x,y,z = que.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
        
      if 0<=nx<L and 0<=ny<R and 0<=nz<C:
        if graph[nx][ny][nz] == 'E':
          print(f'Escaped in {count[x][y][z]} minute(s).')
          return
        if graph[nx][ny][nz] == '.' and count[nx][ny][nz] == 0:
          count[nx][ny][nz] = count[x][y][z]+1
          que.append((nx,ny,nz))
  print("Trapped!")    
  
# 3차원 배열 입력받기
while True:
  L, R, C = map(int, input().split())
  if L+R+C == 0: 
    break
  graph = []
  count = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
  for _ in range(L):
    graph.append([list(input().rstrip()) for _ in range(R)])
    temp = input()

  for x in range(L):
    for y in range(R):
      for z in range(C):
        if graph[x][y][z] == 'S':
          bfs(x,y,z)