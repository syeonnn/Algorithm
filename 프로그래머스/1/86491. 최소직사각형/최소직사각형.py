def solution(sizes):
    answer = 0
    # 더 긴 변 중에 젤 긴 길이
    w = max([max(l) for l in sizes])
    # 더 짧은 변 중에 젤 긴 길이
    h = max([min(l) for l in sizes])
    
    answer = w*h
    return answer