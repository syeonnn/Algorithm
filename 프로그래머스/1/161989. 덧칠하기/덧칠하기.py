def solution(n, m, section):
    answer = 0
    # 1m 구역 n개, 롤러의 길이 m미터, 페인트를 다시 칠해야 하는 구역 번호 section
    
    # 한 번에 칠해지는지 확인
    if section[-1] - section[0] + 1 <= m:
        return 1
    
    start = section[0]
    end = section[0] + m - 1
    
    for s in section:
        if s <= end:
            continue
        else:
            answer += 1
            start = s
            end = start + m - 1
        
    
    return answer + 1   # 롤러로 페인트칠해야 하는 최소 횟수