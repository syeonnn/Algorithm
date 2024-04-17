n = int(input())
array = list(map(int, input().split()))

# 내림차순 정렬되는 것을 목표로, 최소한의 병사를 열외시킨다.
dp = [1 for _ in range(n)]
array.reverse()

for i in range(1,n):
  for j in range(i):
    if array[j] < array[i]:  
      dp[i] = max(dp[i], dp[j]+1)
 
print(n - max(dp))
