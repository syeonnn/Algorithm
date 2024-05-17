T = int(input())
for t in range(1, T + 1):
    N = int(input()) # 명령어 수

    speed = 0
    answer = 0
    for i in range(N):
        cmd = list(map(int, input().split())) # 배열을 이용해 입력값 개수를 유동적으로 받음

        if cmd[0] == 1:
            speed += cmd[1]
        elif cmd[0] == 2:
            speed -= cmd[1]
            if speed < 0:   speed = 0
        answer += speed

    print(f'#{t} {answer}')
