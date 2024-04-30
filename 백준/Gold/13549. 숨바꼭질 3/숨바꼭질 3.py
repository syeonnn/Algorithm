# 숨바꼭질 3
# 13549

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split()) # 수빈 동생

visited = [-1 for _ in range(100001)]

def bfs(x):
  que = deque()
  que.append(x)
  visited[x] = 0

  while que:
    x = que.popleft() 

    if x == k:
      return visited[k]
      
    # -1,+1,*2 연산 반복 수행하면서 그 숫자까지 걸리는 시간을 연산해나감
    # for문 안에서 범위 안밖 검사
    # 단, *2 연산 결과를 먼저 처리할 수 있도록 함 (가장 k에 가까운 큰 수이니)

    for nx in (x-1,x+1,x*2):
      if nx < 0 or nx >= 100001 or visited[nx] != -1:
        continue
      # if 0<=nx<100001 and visited[nx] == 0:  
      if nx == x*2:
        visited[nx] = visited[x]
        if nx == 0: # 0또는1의 경우 엣지케이스 주의
          que.append(nx)
          continue
        que.appendleft(nx) # 우선, 2배 연산이 가장 효율적인 길이다
      else:
        visited[nx] = visited[x] + 1
        que.append(nx)

# if n == 0: 
#   print(bfs(1)+1)
# else :
#   print(bfs(n))

print(bfs(n))