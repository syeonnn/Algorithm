import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input()) # 연산 개수
heap = []

for _ in range(N):
  x = int(input())
  
  # x 자연수라면 배열에 넣는다.
  if x > 0:
    heappush(heap, x)
    
  # x 0이라면 배열에서 가장 작은 값 출력+제거
  if x == 0:
    if len(heap) == 0:
      print(0)
      continue
    print(heappop(heap))