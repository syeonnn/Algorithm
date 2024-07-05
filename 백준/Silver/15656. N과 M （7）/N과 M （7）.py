N, M = map(int, input().split())
# 길이가 M인 수열을 모두 구한다.
# N개의 자연수 중에서 (중복가능)M개 고름

nums = list(map(int, input().split()))
temp = [0 for i in range(M)]

def func(idx):
  global temp
  
  if idx == M:
    
    print(*temp)
    idx = 0
    return
    
  for num in nums:
    temp[idx] = num
    func(idx+1)

nums.sort()
func(0)
