T = int(input())
for t in range(1, T + 1):
    goal = list(map(int,input()))
    origin = [0 for _ in range(len(goal))]
    cnt = 0

    for i in range(len(goal)):
        if goal[i] != origin[i]:

            for j in range(i,len(origin)):
                origin[j] = goal[i]

            cnt += 1

    print(f'#{t} {cnt}')
