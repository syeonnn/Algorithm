T = int(input())
for t in range(1, T + 1):
    N = int(input())

    ans = {"2":0, "3":0, "5":0, "7":0, "11":0}

    for key in ans.keys():
        while N % int(key) == 0:
            N //= int(key)
            ans[key] += 1
    print(f'#{t}',*ans.values())
    # print(f'#{t} ', end='')
    # print(*ans.values())
