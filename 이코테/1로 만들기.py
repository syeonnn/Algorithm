X = int(input())

d = [0]*30001
# d[1]은 이미 1 이므로 0으로 초기화된 값 유

for i in range(2,X+1):  # 2부터 X까지
  # 점화식
  # Ai = min(Ai-1, Ai/2, Ai/3, Ai/5) + 1

  d[i] = d[i-1] + 1
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2] + 1)
  if i%3 == 0:
    d[i] = min(d[i], d[i//3] + 1)
  if i%5 == 0:
    d[i] = min(d[i], d[i//5] + 1)

print(d[X])
