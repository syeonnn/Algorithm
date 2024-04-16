N = int(input())  # 회의의 수 N

timetable = []
for _ in range(N):
  timetable.append(list(map(int, input().split())))

# 끝나는 시간, 시작하는 시간 순으로 정렬
timetable.sort(key=lambda x : (x[1],x[0]))
cnt = 1
end_table = timetable[0][1]

for start, end in timetable[1:]:
  if end_table <= start:    
    end_table = end
    cnt += 1
    
print(cnt)  # 최대 사용할 수 있는 회의의 최대 개수