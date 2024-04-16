from collections import deque

N = int(input())
graph = []
for _ in range(N):
  graph.append(list(map(int, input())))

ans = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# def dfs(x,y):
#   graph[x][y] = 0
#   global cnt

#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0<=nx<N and 0<=ny<N and graph[nx][ny]==1:
#       dfs(nx,ny)
#       cnt += 1

# for i in range(N):
#   for j in range(N):
#     if graph[i][j] == 1:
#       cnt = 1
#       dfs(i,j)
#       ans.append(cnt)

def bfs(x,y):
  cnt = 1
  que = deque()
  que.append((x,y))
  
  while que:
    x,y = que.popleft()
    graph[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<N and graph[nx][ny]==1:
        que.append((nx,ny))
        graph[nx][ny] = 0
        cnt += 1
    
  return cnt

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      count = bfs(i,j)
      ans.append(count)
      
# 총 단지수
print(len(ans))
# 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
print('\n'.join(map(str, sorted(ans))))