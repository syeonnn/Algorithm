def solution(plans):
    answer = []
    plans_mins = []
    
    
    # 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야 하는 과제부터 진행
    # 멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작
    
    for i in range(len(plans)):
        h,m = map(int, plans[i][1].split(":"))
        # 과제명, 시작시간, 소요시간
        plans_mins.append([plans[i][0], 60*h + m, int(plans[i][2])]) 
    # 시작 시간 순서대로 정렬
    plans_mins.sort(key = lambda x: x[1])
    
    temp = []
    temp.append(plans_mins[0])
    time = plans_mins[0][1]
    
    for i in range(1, len(plans_mins)):
        next = plans_mins[i][1]
    
        while temp:
            name, start, need = temp.pop()
            
            if time < start:
                time = start

            if (time + need) <= next:
                answer.append(name)
                time += need
            else:
                need -= (next - time)   # 이 부분 계산에서...완전 빙글뱅글...
                temp.append([name, start, need])
                time = next
                break
            
        temp.append(plans_mins[i])

    for t in temp[::-1]:
        answer.append(t[0])
        
    return answer   # 끝낸 순서대로 과제 이름