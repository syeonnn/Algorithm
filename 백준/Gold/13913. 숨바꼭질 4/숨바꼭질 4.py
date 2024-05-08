import sys
from collections import deque

input = sys.stdin.readline

# 입력 : 수빈이가 있는 위치N, 동생이 있는 위치 K
N, K = map(int, input().split())

visited = [-1 for _ in range(100001)]
path = [0 for _ in range(100001)]

def print_path(x):
  result = []

  for _ in range(visited[K] + 1): # 이동시간 동안
    result.append(x)
    x = path[x] # 이전 방문 노드 갱신
  print(' '.join(map(str, result[::-1])))

def bfs(x):
  que = deque()
  que.append(x)
  visited[x] = 0

  while que:
    x = que.popleft()

    if x == K:
      print(visited[K])
      print_path(x) # 도착지점부터 시작지점까지 방문 노드를 거꾸로 찾아 올라가기
      return

    for nx in (x+1, x-1, x*2):
      if nx < 0 or nx > 100000 or visited[nx] >= 0:
        continue
        
      visited[nx] = visited[x] + 1
      que.append(nx)
      path[nx] = x
        
bfs(N)