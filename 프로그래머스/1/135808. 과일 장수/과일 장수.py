def solution(k, m, score):
    answer = 0
    
    # 박스별
    # (최저 사과 점수) x (한 상자에 담긴 사과 개수)
    
    score.sort(reverse = True)
    for i in range(len(score)//m):
        answer += ( score[i*m+(m-1)] * m )

    return answer # 최대 이익