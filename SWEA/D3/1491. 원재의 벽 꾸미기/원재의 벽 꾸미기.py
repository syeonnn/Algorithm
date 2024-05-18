import math

T = int(input())
for t in range(1, T + 1):
    # 조건 주의!!
    # 1 X 1타일 * N개 -> R * C, 따라서 R * C <= N
    # A * |R - C| + B * (N - R * C)

    N, A, B = map(int, input().split())
    min_result = math.inf

    for r in range(1, N+1):
        c = 1
        while r*c <= N:
            result = A * abs(r-c) + B * (N-r*c)
            min_result = min(result, min_result)
            c += 1

    print(f'#{t} {min_result}')
