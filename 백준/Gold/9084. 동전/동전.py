from itertools import combinations

T = int(input())  # 테케
for _ in range(T):
  N = int(input())  # 동전 가지 수
  coins = list(map(int, input().split()))  # 오름차순으로 각 동전 금액 입력
  M = int(input())  # 동전으로 만들어야 할 금액

  dp = [1] + [0]*(M)

  for coin in coins:
    for i in range(1, M+1):
      if i >= coin:
        dp[i] += dp[i-coin]
        
  print(dp[M])
    