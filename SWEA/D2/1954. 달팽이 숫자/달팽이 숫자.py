T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    N = int(input()) # 달팽이 크기 N
    board = [[0 for _ in range(N)] for _ in range(N)]
    i, cnt = 0, 1
    x, y = 0, -1
    d = [(0,1),(1,0),(0,-1),(-1,0)]

    # board 탐색하면서 코너 or 0이 아닌 숫자 만났을 때 방향 전환
    while cnt <= N*N:
        nx, ny = x + d[i][0], y + d[i][1]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
            board[nx][ny] = cnt
            cnt += 1
            x,y = nx,ny
        else:
            i = (i + 1) % 4

    print(f'#{t}')
    for row in board:
        print(*row)
