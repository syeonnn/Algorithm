def solution(citations):
    answer = 0
    # n편 중, h번 이상 인용된 논문이 h편 이상 (나머지는 h번 이하 인용)
    # h의 최대값
    citations.sort(reverse = True)
    
    for i,c in enumerate(citations):
        if c <= i:
            answer = i
            return answer
    
    return len(citations)  # ✅ 모두 조건 만족한 경우    