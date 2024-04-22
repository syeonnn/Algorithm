# 안전 영역

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input()) # 그래프 크기 n*n
graph = []
max_limit = 0
min_limit = 101
result = 0

for _ in range(n):
  data = list(map(int, input().split()))
  graph.append(data)
  max_limit = max(max_limit,max(data))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,limit):
  for j in range(4):
    nx = x + dx[j]
    ny = y + dy[j]
    if 0<=nx<n and 0<=ny<n and graph[nx][ny] > limit and visited[nx][ny] is False: # r그래프 범위 내o, 물에 잠기지x, 방문x 경우
      visited[nx][ny] = True
      dfs(nx,ny,limit)

for i in range(max_limit):
  visited = [[False for _ in range(n)] for _ in range(n)]
  cnt = 0
  
  for x in range(n):
    for y in range(n):
      if visited[x][y] is False and graph[x][y] > i:
        cnt += 1
        visited[x][y] = True
        dfs(x,y,i)
        
  result = max(result,cnt)

print(result)