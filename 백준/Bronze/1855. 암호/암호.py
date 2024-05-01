import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입출력
k = int(input()) # 열 수
crypto = list(''.join(input().strip()))

graph = []
for i in range(0, len(crypto), k):
  graph.append(crypto[i:i+k]) # 4행 3열 그래프로 만들기

for j in range(len(graph)): # 4개 행에 대해
  if j % 2 != 0: #홀수 행 reverse
    graph[j].reverse() # reverse는 값 반환x, reversed는 값 반환o

# 굳이 배열로 답 뽑아낼 필요없다면 스트링으로!!
answer = ''
b = 0
for b in range(k): # 0 1 2 열에 대해
  for a in range(len(graph)): # 0 1 2 3 행에 대해
    answer += graph[a][b]

print(answer)