from heapq import heappop, heappush
import sys
input = sys.stdin.readline

# 입력
N = int(input())
lheap = []
rheap = []

# 중간값 구하기
for _ in range(N):
  x = int(input())
  # 왼힙(최대힙), 오른힙(최소힙) 2개로 나누어 값 저장
  # 왼힙 길이 (+1) = 오른힙 길이
  # 왼힙pop = 중간값
  if len(lheap) == len(rheap):
    heappush(lheap, -x)
  else:
    heappush(rheap, x)

  if rheap and -lheap[0] > rheap[0]: 
    heappush(lheap, -heappop(rheap))
    heappush(rheap, -heappop(lheap))
  
  print(-lheap[0])
 