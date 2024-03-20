# DFS_음료수 얼려 먹기

n, m = map(int, input().split()) # 가로, 세로
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
  # 주어진 범위를 벗어난 경우
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  # 현재 노드 아직 방문하지 않은 경우
  if graph[x][y] == 0:
    graph[x][y] = 1 # 방문 처리
    # 인접 노드들 재귀적 호출
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx,ny)
    return True
  
  return False
  
# 모든 노드 탐색
result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) is True:
        result += 1
print(result)

