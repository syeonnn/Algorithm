N = int(input())

# dp
dp = [0] * (1000 + 1) # 돌 1개 ~ N개일 때 각각 턴 수

dp[1] = 1
dp[2] = 2
dp[3] = 1
 
for n in range(4, N+1):
    dp[n] = min(dp[n-1], dp[n-3]) + 1
 
if dp[N] % 2 == 1:    # 홀수번째 턴으로 끝나면
    print('SK')
else:
    print('CY')

# dp 규칙 찾아보았을 때 결론, 짝수: CY, 홀수: SK
# if N % 2 == 0:
#   print("CY")
# else:
#   print("SK")