from heapq import heappop, heappush
import sys
from collections import defaultdict

input = sys.stdin.readline

# 입력
N = int(input())  # 문제 리스트에 있는 문제 수
min_heap = []  # 쉬운 순 정렬 (min heap)
max_heap = []  # 어려운 순 정렬 (max heap)
solved = defaultdict(int)

for _ in range(N):
  P, L = map(int, input().split())  # 문제번호 P, 난이도 L
  heappush(min_heap, (L, P))  # 쉬운 문제는 번호 작은 순
  heappush(max_heap, (-L, -P))  # 어려운 문제는 번호 큰 순

M = int(input())  # 명령문 수
for _ in range(M):
  commands = list(input().split())

  if commands[0] == 'recommend':
    if commands[1] == '1':  # 가장 어려운 문제
      while solved[abs(max_heap[0][1])] != 0: # 안 푼 문제 중에서 찾기
        solved[abs(max_heap[0][1])] -= 1 # 같은 번호 다른 난이도 문제 필터링하는 용도
        heappop(max_heap)
      print(-max_heap[0][1])

    elif commands[1] == '-1':  # 가장 쉬운 문
      while solved[min_heap[0][1]] != 0:
        solved[min_heap[0][1]] -= 1 # 같은 번호 다른 난이도 문제 필터링하는 용도
        heappop(min_heap)
      print(min_heap[0][1])

  if commands[0] == 'add':
    p, l = int(commands[1]), int(commands[2])
    heappush(min_heap, (l, p))
    heappush(max_heap, (-l, -p))

  elif commands[0] == 'solved':
    solved[int(commands[1])] += 1 
    # 출력은 문제번호만 요구함
    # 따라서, 같은 번호 다른 난이도 문제에 대해 '번호 기준'으로 풀이 여부 기록
