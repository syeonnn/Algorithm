n, m = map(int, input().split()) # n행 m열
graph = [list(map(int, input())) for _ in range(n)]
# 1로 된 가장 큰 정사각형의 크기 반환

answer = graph[0][0]
for i in range(1, n):
  for j in range(1, m):
    if graph[i][j] == 1:
      graph[i][j] = min(graph[i-1][j], graph[i][j-1], graph[i-1][j-1]) + 1

for row in graph:
    answer = max(max(row), answer)

print(answer**2)