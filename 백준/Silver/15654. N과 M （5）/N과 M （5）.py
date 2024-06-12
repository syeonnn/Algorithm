N, M = map(int, input().split())
# N개의 자연수 중에서 M개를 고른 수열

numbers = list(map(int, input().split())) # N개의 자연수
numbers.sort()
isused = [0 for _ in range(N)]
result = [0 for _ in range(M)] # 자연수 M개의 수열
ans = []

def func(x):
  global result
  
  if x == M:
    print(' '.join(map(str,result)))
    return 
    
  for i in range(N):
    if not isused[i]:
      isused[i] = 1
      result[x] = numbers[i]
      func(x+1)
      isused[i] = 0

func(0)