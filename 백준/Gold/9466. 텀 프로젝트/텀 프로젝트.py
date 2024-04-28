import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x): # x는 멤버의 순서(자리)
  global count
  
  visited[x] = 1
  team.append(x)
  member = student[x]

  if visited[member] == 1:
    # 그냥 순서대로 방문하는 것 때문에 방문처리된 것일수도 있음
    # 짝꿍 매칭되는 지 여부 확인할 것
    if member in team:
      count += len(team[team.index(member):])
  else:
    dfs(member)
  
T = int(input())
for _ in range(T):
  count = 0
  n = int(input())
  student = [0] + list(map(int, input().split()))
  visited = [0 for _ in range(n+1)]
  
  for i in range(1,n+1): # 앞에서부터 순서대로 멤버들이 희망하는 짝꿍 탐색
    if visited[i] == 0:
      team = []
      dfs(i)
      
  print(n - count)