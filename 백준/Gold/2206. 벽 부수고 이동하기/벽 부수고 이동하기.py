# 벽 부수고 이동하기
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]

def bfs(a, b, c):
  que = deque()
  que.append((a, b, c))
  visited[a][b][c] = 1
  
  while que:
    x, y, bomb = que.popleft()

    # for문안에서 값 비교하면 아직 nx,ny인덱스값에 대해 연산 전이라서 원하는 값 반환안됨!
    if x == N - 1 and y == M - 1:
      return visited[x][y][bomb]
      
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        # 헤멘 포인트 : 값 비교할 때 int, str 데이터 타입 확인하기
        if graph[nx][ny] == 0 and visited[nx][ny][bomb] == 0:  # 벽이 아니고 방문 한 적 없다면
          visited[nx][ny][bomb] = visited[x][y][bomb] + 1
          que.append((nx, ny, bomb))
        
        if graph[nx][ny] == 1 and bomb == 0:
          # 벽이고 아직 부시기 전이면 한 번 부시기
          visited[nx][ny][1] = visited[x][y][0] + 1
          que.append((nx, ny, 1))
  return -1

# 최단 거리 출력, 불가능할 때는 -1 출력
print(bfs(0, 0, 0))