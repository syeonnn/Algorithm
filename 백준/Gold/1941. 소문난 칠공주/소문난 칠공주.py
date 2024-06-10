import sys
from itertools import combinations
from collections import deque

def checkBFS(comb,visited): # 서로 가로나 세로로 인접한지
  count = 1 # 인접한 사람들을 모두 탐색했을 때 조합7명을 모두 검출할 수 있는지
  que = deque([comb[0]])
  visited[comb[0][0]][comb[0][1]] = 1
  
  while que:
    x,y = que.popleft()
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
      nx, ny = x + dx, y + dy
      if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
        visited[nx][ny] = 1
        if (nx,ny) in comb:
          que.append((nx,ny))
          count += 1
          
  return count == 7

# 1. 7명의 조합을 백트래킹으로 구한다.

graph = [list(input().strip()) for _ in range(5)]

# 2. 파이썬에는 combinations 라이브러리가 있다.
c = [(i, j) for i in range(5) for j in range(5)]
answer = 0

for comb in list(combinations(c, 7)):
  visited = [[0 for _ in range(5)] for _ in range(5)]
  s_count = sum(1 for x,y in comb if graph[x][y] == 'S')
  
  if s_count >= 4:
    if checkBFS(comb,visited):
      answer += 1

print(answer)