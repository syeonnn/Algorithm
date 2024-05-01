import sys
#from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 입출력
while True:
  n = int(input())
  if n == 0 :
    exit()
  sentence = input().replace(" ","")
  sen = list(sentence.strip().upper())
  
  # 암호화
  length = len(sen)
  answer = ['BLANK' for _ in range(length)]

  j = 0
  circle = 0
  for i in range(length):
    
    if j>=length:
      j = 0
      circle += 1
      j += circle # circle바퀴째

    answer[j] = sen[i]
    j += n # n만큼 떨어진 문자
  
  print(''.join(answer))