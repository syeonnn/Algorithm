from collections import deque
import sys

f,s,g,u,d = map(int,sys.stdin.readline().split())

# 1층~f층에 대해 s->g로 가기 위해 눌러야 하는 버튼 수의 최솟값

def bfs():
  que = deque()
  que.append(s)
  count[s] = 1
  
  while que:
    x = que.popleft()

    if x == g:
      return count[g] - 1
    else: 
      for i in (x+u, x-d):
        if 0 < i <= f and count[i] == 0:
          que.append(i)
          count[i] = count[x]+1    
    
  return "use the stairs"

count = [0 for _ in range(f+1)]
print(bfs())