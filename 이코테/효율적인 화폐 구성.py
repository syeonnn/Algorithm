n, m = map(int, input().split())
list = []
for _ in range(n):
  list.append(int(input())) # 화폐 단위 목

d = [10001]*(m+1) # m원까지 바텀업 방식으로 최소 화폐 개수 담는 dp 리스트 초기화

d[0] = 0
# 바텀업 실행
for i in range(n):
  for j in range(list[i], m+1): 
   if d[j-list[i]] != 10001:
    d[j] = min(d[j],d[j-list[i]]+1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
