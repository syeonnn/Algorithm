# 스타트링크
# bfs

# sys.setrecursionlimit(10**6)

from collections import deque
import sys
# 수빈이 위치, 동생 위치
N,K = map(int, sys.stdin.readline().split())
count = [0 for _ in range(100001)]

# 수빈이가 동생을 찾는 가장 빠른 시간 출력
def bfs():
  que = deque()
  que.append(N)
  count[N] = 1
  
  while que:
    cur = que.popleft()
    
    if cur == K:
      return count[K]-1
      
    for i in [2*cur, cur-1, cur+1]:
      if 0 <= i <= 100000 and count[i] == 0:
        count[i] = count[cur] + 1
        que.append(i)
    
print(bfs())