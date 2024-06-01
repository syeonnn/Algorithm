import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

for _ in range(T):
  H, W = map(int, input().split())
  graph = [list(input().strip()) for _ in range(H)]
  keys = list(map(str, input().rstrip()))
  visited = [[0 for _ in range(W)] for _ in range(H)]
  answer = 0
  temp = []
  # 가장자리의 벽이 아닌 곳을 통해 빌딩 안팎 드나들기
  # dfs로 해보기
  
  def dfs(x,y):
    global visited, answer, temp
    #print(x,y)
    if 0<=x<H and 0<=y<W:
      for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx = x + dx
        ny = y + dy
        #print(nx,ny)
        
        if 0<=nx<H and 0<=ny<W and visited[nx][ny] == 0:
          
          if 'a'<=graph[nx][ny]<='z':
            #print("소문자")
            keys.append(graph[nx][ny])
            visited = [[0 for _ in range(W)] for _ in range(H)] # 초기화
            visited[nx][ny] = 1
            graph[nx][ny] = "."
            keys.append(graph[nx][ny])
            dfs(nx,ny)
            
          elif 'A'<=graph[nx][ny]<='Z':
            #print("대문자")
            if graph[nx][ny].lower() in keys:
              visited[nx][ny] = 1
              graph[nx][ny] = "."
              dfs(nx,ny)
  
          elif graph[nx][ny] == "$": # 문서찾음
            #print("찾앗다")
            if (nx,ny) not in temp:
              answer += 1
              temp.append((nx,ny))
            
            graph[nx][ny] = "."
            visited[nx][ny] = 1
            dfs(nx,ny)
  
          elif graph[nx][ny] == '.':
            #print(nx,ny)
            visited[nx][ny] = 1
            dfs(nx,ny)
        
    return answer

  a = 0
  for h in range(H):
    for w in range(W):
      if h==0 or h== H-1 or w==0 or w==W-1:
        if graph[h][w] == '.':
          a = dfs(h,w)

  print(a)
