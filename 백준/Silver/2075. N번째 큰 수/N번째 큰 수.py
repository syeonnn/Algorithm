import sys
from heapq import heappop, heappush, nlargest
input = sys.stdin.readline

N = int(input())
heap = []

# N번째 큰 수 = 가장 큰 수 N개 가운데 가장 작은 값
for _ in range(N):
  nums = map(int,input().split())
  for num in nums:
    if len(heap) < N: # 힙에 빈자리가 있다면
      heappush(heap,num) 
    if len(heap) >= N and num > heap[0]: 
        # 힙에 빈자리가 없고 
        # 새로운 값이 힙의 최소값보다 크다면 = 밀어낼 만한 수라면
      heappop(heap) 
      heappush(heap,num)
print(heap[0])