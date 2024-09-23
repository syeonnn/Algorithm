from collections import deque

def solution(priorities, location):
    answer = 0
    
    # 알파벳 순서 배열 == priorities
    processes = deque(enumerate(priorities))

    # location번째 인덱스의 값이 몇번째로 실행되는지
    while processes:
        i, p = processes.popleft()
        
        # 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면
        if any(p < pri for _, pri in processes):
            processes.append((i, p))
            
        else :
            answer += 1
            if i == location:
                break

    return answer