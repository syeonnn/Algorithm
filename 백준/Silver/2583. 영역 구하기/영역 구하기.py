import sys
sys.setrecursionlimit(10**6)

M,N,K = map(int, input().split())
graph = [[0]*N for _ in range(M)]

# 내가 놓친 부분 : 
# 배열로 그래프 그릴 때 좌표와 문제에서 주어진 맵의 크기!  관계 정확히 이해하고 파악해서 그리기!!

for _ in range(K):
  sx, sy, ex, ey = map(int, input().split())
  for y in range(sy, ey):
    for x in range(sx, ex):
      graph[y][x] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
ans = []

def dfs(x,y):
  global cnt
  graph[x][y]=1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<M and 0<=ny<N and graph[nx][ny]==0:
      cnt += 1 # 영역 넓이 계산
      dfs(nx,ny)

for i in range(M):
  for j in range(N):
    if graph[i][j] == 0:
      cnt = 1
      dfs(i,j)
      ans.append(cnt)
      
print(len(ans))

ans.sort()
for a in ans:
  print(a, end=' ')
#print(' '.join(map(str, ans)))