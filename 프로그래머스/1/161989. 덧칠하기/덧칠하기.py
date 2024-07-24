def solution(n, m, section):
    answer = 0
    # 1m 구역 n개, 롤러의 길이 m미터, 페인트를 다시 칠해야 하는 구역 번호 section
    
    start = section[0]
    
    for num in section:
        if num - start + 1 <= m:
            continue
        else:
            answer += 1
            start = num
            
    return answer + 1   # 롤러로 페인트칠해야 하는 최소 횟수