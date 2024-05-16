T = int(input())
for t in range(1, T + 1):
    N = int(input())

    sen = ''
    for _ in range(N):
        char, num = input().split()
        sen += char * int(num)

    print(f'#{t}')
    for i in range(len(sen)//10+1):
        print(''.join(sen[i*10:i*10+10]))
