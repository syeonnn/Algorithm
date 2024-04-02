# 전체사람 수 n
n = int(input())
# 촌수 계산해야 하는 두 사람의 번호`
[x,y] = list(map(int, input().split()))
# [parent,child] = sorted([x,y]) #오름차순이니까 순서대로 부모, 자식
# 부모 자식 관계 수 m
m = int(input())
# 관계 m의 경우~
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
  # 부모, 자식 순
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

result = [0]*(n+1)

def dfs(idx,result):
  global flag
  visited[idx] = True
  
  if idx == y:
    flag = True
    return result[idx]
    
  for comp in graph[idx]:
    if not visited[comp]:
      result[comp] = result[idx] + 1
      dfs(comp,result)

flag = False

result[x]=1

dfs(x,result)

print(result[y]-1) if result[y]!=1 else print(-1)
# 친척 관계가 없는 경우 -1 , 아니라면 촌수 정수 출력