S = input()
suffix = [S[i:] for i in range(len(S))]

suffix.sort()
for s in suffix:
  print(s)