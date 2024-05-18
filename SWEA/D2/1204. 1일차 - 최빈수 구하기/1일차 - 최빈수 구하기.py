T = int(input())
for t in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    answer = [0 for _ in range(101)]

    for score in array:
        answer[score] += 1

    # 조건에 해당하는 모든 값 반환(index함수 역할 업그레이드)
    max_idxs = [i for i, value in enumerate(answer) if value == max(answer)] 

    print(f'#{N} {max_idxs[-1]}')
