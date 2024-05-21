import math
def solution(progresses, speeds):
    answer = []
    need = []
    # 각 기능에 대해 100%까지 소요되는 일 수 저장하는 배열need [7,3,9]
    for i,p in enumerate(progresses):
        need.append(math.ceil((100-p)/speeds[i]))
    
    std = need[0]
    cnt = 1

    for n in need[1:]:
        if n <= std:    # 배포 기준일보다 작업 소요일 작으면
            cnt += 1
        elif n > std:       #  배포 기준일보다 작업 소요일 크면
            answer.append(cnt)
            cnt = 1
            std = n # 배포 기준일 갱신
            
    # 마지막 배포일...
    answer.append(cnt)
    
    return answer