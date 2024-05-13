import sys

input = sys.stdin.readline

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

# 최대 이익 출력
# dp[K] = K일째에 얻을 수 있는 최대 이익

for i in range(N): # 0 ~ N-1
  dp[i+1] = max(dp[i], dp[i+1])  # 시간초과 해결하기 위해 앞뒤 원소 크기 비교로 dp 배열 요소 갱신
  if i + array[i][0] <= N:
    dp[i+array[i][0]] = max(dp[i] + array[i][1], dp[i+array[i][0]])
  
print(dp[-1])