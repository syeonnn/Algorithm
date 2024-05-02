from heapq import heappop, heappush
import sys
input = sys.stdin.readline

# 입력
T = int(input())
for _ in range(T):
  M = int(input()) # 수열의 크기
  array = []
  for _ in range(0, M, 10):
    array.append(list(map(int,input().split())))
  lheap = [] # 최대힙 (중간값 포함)
  rheap = [] # 최소힙
  ans = []

  for i in range(0, M//10+1):
    for idx,n in enumerate(array[i]): # 10개 원소 가운데 홀수번째 수 1,3,5,7,9 읽었을 때만 중앙값 출력
      if len(lheap) == len(rheap):
        heappush(lheap, -n)
      else:
        heappush(rheap, n)

      if rheap and -lheap[0] > rheap[0]:
        heappush(rheap, -heappop(lheap))
        heappush(lheap, -heappop(rheap))
        
      if idx % 2 == 0:
        ans.append(-lheap[0])

  print(len(ans))
  
  for i in range(0,len(ans),10):
    print(' '.join(map(str,ans[i:i+10])))
