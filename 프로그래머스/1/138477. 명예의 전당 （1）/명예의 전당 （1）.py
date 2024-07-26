def solution(k, score):
    temp = []
    answer = []
    
    for i in range(len(score)):
        if i < k:
            temp.append(score[i])
        
        elif i >= k and score[i] > min(temp): # 그 값보다 점수가 높다면
            temp.remove(min(temp))
            temp.append(score[i])
            
        answer.append(min(temp))
    
    # 매일 발표된 명예의 전당의 최하위 점수
    return answer