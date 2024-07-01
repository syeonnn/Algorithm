def solution(n, times):
    # 입국심사를 기다리는 사람 수 n, 한 명 심사하는 데 걸리는 시간 times

    answer = 0
    # 모든 사람이 심사를 받는데 걸리는 시간을 최소화 
    # => 최적값!! 총 소요시간만 구하면 되는 문제임
    
    # ( 아니면 dp로?? spent = [0]*(max(times)*n)... )
    
    # 이분탐색으로 최적값 찾아나가기
    left = min(times)
    right = max(times)*n
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for man in times: 
            people += mid // man # 총 소요 시간에 대해 각 심사관이 심사할 수 있는 인원들 합
            if people >= n: # 이미 시간 충분하다면
                break
                
        if people >= n:
            right = mid - 1
            answer = mid
            
        elif people < n:
            left = mid + 1
    
    return answer