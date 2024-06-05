import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  H, W = map(int, input().split())
  graph = [['.']+list(input().strip())+['.'] for _ in range(H)]
  graph = ['.' * (W + 2)] + graph + ['.' * (W + 2)]
  keys = list(map(str, input().rstrip()))
  if keys == ['0']:
    keys = []
  visited = [[0 for _ in range(W+2)] for _ in range(H+2)]
  answer = 0
  a = 0
  temp = []

  def bfs():
    global visited, answer, temp

    que = deque()
    que.append([0, 0])
    visited[0][0] = 1

    while que:
      x, y = que.popleft()
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= H+2 or ny >= W+2 or ny < 0 or graph[nx][ny] == '*' or visited[nx][ny]:
          continue

        if 'a' <= graph[nx][ny] <= 'z':
          if graph[nx][ny] not in keys: # 문을 열 수 있다면
            keys.append(graph[nx][ny])
            visited = [[0 for _ in range(W+2)] for _ in range(H+2)]  # 방문 기록 초기화

        elif 'A' <= graph[nx][ny] <= 'Z':
          if graph[nx][ny].lower() not in keys:
            continue

        elif graph[nx][ny] == "$" and (nx, ny) not in temp:  # "새로운" 문서 찾음
          answer += 1
          temp.append((nx, ny))

        que.append([nx, ny]) # 다음 탐색을 위해 큐에 위치 삽입
        visited[nx][ny] = 1 # 방문 처리

    return answer
    
  print(bfs())
