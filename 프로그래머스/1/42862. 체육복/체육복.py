def solution(n, lost, reserve):
    answer = 0

    # 분실+여분 중복되는 학생 꺼내기
    _lost = list(set(lost)-set(reserve))
    _reserve = list(set(reserve)-set(lost))

    for i in _reserve :
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)
    
    answer += n-len(_lost)

    return answer