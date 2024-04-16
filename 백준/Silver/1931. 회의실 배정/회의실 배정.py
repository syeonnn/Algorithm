N = int(input())  # 회의의 수 N
timetable = []

for _ in range(N):
  timetable.append(list(map(int, input().split())))

# 끝나는 시간, 시작하는 시간 순으로 정렬
timetable.sort(key=lambda x : (x[1],x[0]))
answer = 0
end_table = 0

for new_start, new_end in timetable:
    if end_table <= new_start:
        answer += 1
        end_table = new_end
        
print(answer)