N, M = map(int, input().split())
list = list(map(int, input().split())) #N 개 떡 개별 높이

start = 0
end = max(list)

result = 0
while (start <= end):
  total = 0
  mid = (start + end) // 2
  for x in list:
    if x > mid:
      total += x - mid
    if total < M:
      end = mid - 1
    else:
      result = mid # 최적 해 result 값 갱신
      start = mid + 1

print(result)
