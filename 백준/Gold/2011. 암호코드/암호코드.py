# encrypt, decrypt
secret = list(map(int,input()))  # 5000자리 이하의 암호
dp = [1,1] + [0 for _ in range(len(secret)-1)]

if secret[0] == 0:
  print(0)
else:  
  for i in range(1,len(secret)):
    j = i + 1
    if secret[i] > 0:
      dp[j] += dp[j-1]
    if 10 <= (secret[i-1]*10 + secret[i]) <= 26:
      dp[j] += dp[j-2]
    
  print(dp[-1] % 1000000)
# 나올 수 있는 해석의 가짓수 % 1000000
# 암호가 잘못되어 암호를 해석할 수 없는 경우에는 0을 출력한다.