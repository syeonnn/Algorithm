import sys
from collections import deque

input = sys.stdin.readline

N, M, P = map(int,input().split())
S = [0] + list(map(int,input().split()))
board = [list(str(input())) for _ in range(N)]
conquer = [deque() for _ in range(P+1)]
ans = [0 for _ in range(P+1)]

for i in range(N):
  for j in range(M):
    if board[i][j] != '.' and board[i][j] != '#':
      conquer[int(board[i][j])].append((i,j))
      ans[int(board[i][j])] += 1

def bfs():
  moved = True
  while moved:
    moved = False 
    # 플레이어가 더이상 성 건설 불가하면 게임 끝
    # 한 명의 플레이어라도 성 건설했을 때 게임continue
    
    for p in range(1,P+1): # 플레이어마다 돌아가면서(=반복해서)
      if not conquer[p]: # 탐색할 성이 없다면
        continue
      temp_q = conquer[p]
      
      for _ in range(1,S[p]+1): # 이동 범위에 대해
        if not temp_q: # 탐색할 성이 없다면 = 아직 이동 범위 내 모든 구역 탐색하지 못했지만 막혀버림
          break
          
        for _ in range(len(temp_q)): # 각각의 (new)성들에 대해 탐색!
          x,y = temp_q.popleft()
          ## 이동 범위 내 탐색 + 성 건설
          for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny <= M and board[nx][ny] == '.':
              board[nx][ny] = str(p)
              temp_q.append((nx,ny))
              moved = True
              ans[p] += 1

bfs()
print(*ans[1:])