T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    sm, sd, em, ed = map(int, input().split())

    calender = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    days = 0
    if sm == em:
        days = ed - sd + 1
    else:
        days += calender[sm] - sd + ed + 1

        for month in range(sm+1, em):
           days += calender[month]

    print(f'#{t} {days}')
