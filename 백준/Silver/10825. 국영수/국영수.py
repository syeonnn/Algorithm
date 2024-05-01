import sys
input = sys.stdin.readline

N = int(input())
chart = [list(input().split()) for _ in range(N)]
  
# 정렬
chart.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in chart:
  print(student[0])
