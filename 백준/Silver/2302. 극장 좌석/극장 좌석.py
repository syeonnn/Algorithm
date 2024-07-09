import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
vips = [0] + [int(input()) for _ in range(M)] + [N+1]

dp = [0 for _ in range(42)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

# 점화식에 따라 dp값 미리 연산
for i in range(3, N + 1):
  dp[i] = dp[i - 1] + dp[i - 2]

answer = 1
for m in range(1, M+2):
  answer *= dp[vips[m] - vips[m-1] - 1]  # vip바로 전 좌석까지의 이동 가능한 경우(시작점 ~ vip 또는 vip ~ vip 자리 사이의 좌석들)
  
print(answer)