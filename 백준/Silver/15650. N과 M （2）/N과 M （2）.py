import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 수열은 오름차순 정렬이어야 함
array = [0 for _ in range(M)]
isused = [0 for _ in range(N+1)]

def func(x):
  if x == M:
    print(' '.join(map(str, array)))
    return
    
  for i in range(1, N+1):
    if not isused[i]:
      if x == 0 or (x > 0 and i > array[x-1]):
        array[x] = i
        isused[i] = 1
        func(x+1)
        isused[i] = 0
        
      else:
        continue
  return    
    
func(0)
  