import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# 실제 배열을 저장하지 않고, 길이만을 추적하므로 출력 배열이 올바르지 않을 수 있다.
# 따라서 실제 위치를 저장한 배열을 따로 만들 필요가 있다.

# dp = [array[0]]

# # 첫번째 원소부터 차례대로 탐색
# for x in array:
#   if dp[-1] < x:
#     dp.append(x)
#   else:
#     index = bisect_left(dp,x)
#     dp[index] = x # 더 긴 증가하는 수열을 만들기 위해 갱신

# print(len(dp))  # 가장 긴 증가하는 부분 수열의 길이
# print(' '.join(map(str,dp)))

dp = [1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)

max_cnt = max(dp)
print(max_cnt)

answer = []
# for i in range(n-1, -1, -1):
#   if dp[i] == max_cnt:
#     answer.append(array[i])
#     max_cnt -= 1

for i, x in enumerate(dp[::-1]):
  if x == max_cnt:
      answer.append(array[len(dp) - i - 1])
      max_cnt -= 1

answer.reverse()
print(' '.join(map(str,answer)))
