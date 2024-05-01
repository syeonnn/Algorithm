# https://www.acmicpc.net/problem/1600

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입출력
K = int(input())
w,h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

# 최소한의 동작으로 출발->도착 가는 방법 BFS

# k번만 수행가능한 나이트 동작
kdx = [1,2,2,1,-1,-2,-2,-1]
kdy = [2,1,-1,-2,-2,-1,1,2]
# 기본 동작
dx = [-1,1,0,0]
dy = [0,0,-1,1]

  
def bfs(x,y,k):
  que = deque()
  visited = [[[0]*(K+1) for _ in range(w)] for _ in range(h)] 
  
  que.append((x,y,k))
  visited[x][y][k] = 1

  while que:
    x,y,k = que.popleft()

    if x == h-1 and y == w-1:
      return visited[x][y][k] -1
    
    if k < K: # 아직 나이트 동작 가능한 횟수 남아있으면
      for i in range(8): # 나이트 동작 먼저 시도
        nx = x + kdx[i]
        ny = y + kdy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w: # 범위밖 또는 이미 방문
          continue
        if visited[nx][ny][k+1] >= 1 or graph[nx][ny] == 1:
          continue
        if graph[nx][ny] == 0: 
          visited[nx][ny][k+1] = visited[x][y][k] + 1
          que.append((nx,ny,k+1))
            
    for i in range(4): # 기본 동작 수행
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= h or ny < 0 or ny >= w: # 범위밖 또는 이미 방문
        continue
      if visited[nx][ny][k] >= 1 or graph[nx][ny] == 1:
        continue
      if graph[nx][ny] == 0: 
        visited[nx][ny][k] = visited[x][y][k] + 1
        que.append((nx,ny,k))
        
  return -1        

print(bfs(0,0,0)) # graph x,y좌표 + 나이트 이동방식 수행 횟수
