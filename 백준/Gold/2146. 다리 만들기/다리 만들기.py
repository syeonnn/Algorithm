import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# DFS로 서로 다른 섬 구분하기
# BFS로 다른 섬간 최단 거리 구하기

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0 for _ in range(n)] for _ in range(n)]
name = 1
ans = sys.maxsize

def dfs(x,y):  
  # 섬 번호 부여, 방문 여부 기록
  graph[x][y] = name
  visited[x][y] = 1
  
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    # 범위 밖이면 제외
    if nx<0 or nx>=n or ny<0 or ny>=n:
      continue
    # 육지라면 섬 경계짓기 위해 탐색
    if graph[nx][ny] == 1 and visited[nx][ny] == 0:
      dfs(nx,ny)


def bfs(name):
  global ans
  que = deque()
  dist = [[-1 for _ in range(n)] for _ in range(n)]
  # 같은 번호의 섬 좌표 모두 큐에 넣기
  # 다른 번호의 섬까지의 최소거리 찾는거니까

  for i in range(n):
    for j in range(n):
      if graph[i][j] == name:
        que.append((i,j))
        # dist 0으로 초기화해야돼? 응! 덧셈해서 거리 구하고 최솟값 갱신해야해서 필요함
        dist[i][j] = 0


  while que:
    x,y = que.popleft()
    
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      # 범위 밖이면 제외
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue  
      # 다른 번호의 섬에 도착하면
      if graph[nx][ny] != name and graph[nx][ny] > 0:
        ans = min(ans,dist[x][y])
        return
      # 바다를 건너가는 중 (방문하지않은 길로)
      if graph[nx][ny] == 0 and dist[nx][ny] == -1:
        que.append((nx,ny))
        dist[nx][ny] = dist[x][y] + 1
  
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == 0:
      dfs(i,j)
      name += 1

for j in range(1,name):
  bfs(j)

print(ans)