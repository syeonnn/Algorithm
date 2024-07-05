# 2468
# 물에 잠기지 않는 안전영역의 최대 개수
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)] # N행 N열의 어떤 지역의 높이 정보 그래프

answer = [1]  # 아무 지역도 물에 잠기지 않는 경우

min_h = 101
max_h = 0
for row in graph:
  min_h = min(min(row), min_h)
  max_h = max(max(row), max_h)

def bfs(x,y,height): 
  que = deque()
  que.append((x,y))
  
  while que:
    x,y = que.popleft()
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
      nx, ny = x + dx, y + dy
      
      if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] > height:
        visited[nx][ny] = 1
        que.append((nx,ny))

# 높이 조절하면서 bfs/dfs 탐색
for height in range(min_h, max_h):
  cnt = 0
  visited = [[0]*N for _ in range(N)]
  
  for i in range(N):
    for j in range(N):
      if not visited[i][j] and graph[i][j] > height:
        cnt += 1
        visited[i][j] = 1
        bfs(i,j,height)
        
  answer.append(cnt) # 높이별 안전영역 정보 저장
  
print(max(answer))