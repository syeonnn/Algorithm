# https://www.acmicpc.net/problem/15649

N, M = map(int, input().split())
# 1부터 N까지 자연수 중에서 
# 중복 없이 M개를 고른 수열

isused = [0 for _ in range(N+1)]
array = [0 for _ in range(M)]

def make(x):
  if x == M:
    print(" ".join(map(str, array)))
    return
    
  for j in range(1, N+1):
    if not isused[j]:
      array[x] = j
      isused[j] = 1
      make(x+1)
      isused[j] = 0

make(0) # 수열의 인덱스 0부터 n-1까지