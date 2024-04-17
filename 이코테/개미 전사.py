# 식량창고 개수 N
N = int(input())
K = list(map(int, input().split())) # 식량창고에 저장된 식량의 개수

# DP 테이블 초기화
d = [0]*100

# DP 진행, bottom-up 반복문
d[0] = K[0]
d[1] = max(K[0],K[1])
for i in range(2,N):
  d[i] = max(d[i-1], d[i-2] + K[i])

print(d[N-1])
