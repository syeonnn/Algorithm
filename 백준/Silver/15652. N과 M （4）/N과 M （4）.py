from itertools import combinations_with_replacement
# 중복 조합

N, M = map(int, input().split())
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.

number = [0 for _ in range(M)] # M자리수의 자연수 나타내는 배열

def func(x):
  if x==M:
    print(' '.join(map(str,number)))
    return
  for i in range(1, N+1):
    
    if x==0 or (x > 0 and i >= number[x-1]):
      number[x] = i
      func(x+1)
  return
func(0)