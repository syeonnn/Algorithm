# 현위치 (1,1) -> 출구 (N,M)
# 괴물있 0 괴물없 1
# 간선 길이 같음, 최소 이동 칸의 개수 구하기

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input()))) 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque() # 큐 생성한 뒤
  queue.append((x,y)) # 삽입!
  
  # 큐에 노드 남아있다면
  while queue:
    x,y = queue.popleft()  # 큐에서 뽑기!

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위를 벗어난 경우
        continue
      if graph[nx][ny] == 0: # 괴물이 있는 경우
        continue
      if graph[nx][ny] == 1:  # 괴물 없고 현재 노드 방문하지 않은 경우
        graph[nx][ny] = graph[x][y] + 1    # 방문 처리+거리 계산
        queue.append((nx,ny))  # 인접 노드를 큐에 삽입
  
  return graph[n-1][m-1]

print(bfs(0,0))
