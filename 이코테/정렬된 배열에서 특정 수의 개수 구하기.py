# N개의 원소 array에서 x인 원소의 개수 출력
# 배열은 오름차순 배열 가정
from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
array = list(map(int, input().split()))

def cnt_by_range(array, left_value, right_value):
  left_index = bisect_left(array, left_value)
  right_index = bisect_right(array, right_value)
  print(f'r:{right_index}, l:{left_index}')
  return right_index - left_index

count = cnt_by_range(array, x, x)

if count == 0:
  print(-1)
else:
  print(count)
