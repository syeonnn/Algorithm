N = int(input())

turn = 1 # 1 : 상근, -1 : 창영

# 기냥...
# while N > 0:
#   if N == 1:
#     print("SK" if turn == 1 else "CY")
#     break
#   elif N >= 3:
#     N -= 3
#   else:
#     N -= 1
#   turn *= -1

# dp
# dp = ['' for _ in range(N+1)] # 돌 1개 ~ N개일 때 각각 승자가 누구인지 저장

# dp 규칙 찾아보았을 때 결론, 짝수: CY, 홀수: SK
if N % 2 == 0:
  print("CY")
else:
  print("SK")