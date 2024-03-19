def solution(name):
    answer = 0
    
    # 조이스틱 상하 조작
    notA = [min(ord(name[i])-ord('A'),ord('Z')-ord(name[i])+1) for i in range(0,len(name))]
    answer+=sum(notA)
    print("answer",answer)
    
    left_right = len(name)-1
    
    for i,value in enumerate(name):
        # 조이스틱 좌우 조작
        # 왼쪽 이동 최적해 = 연속된 A문자열 직전 인덱스*2 + (전체 문자열 길이 - 연속된 A문자열의 마지막 인덱스)
        # 오른쪽 이동 최적해 = (전체 문자열 길이 - 연속된 A문자열의 마지막 인덱스)*2 + 연속된 A문자열 직전 인덱스
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        left_right = min(left_right,i*2+len(name)-next ,2*(len(name)-next)+i)
        
        
    return answer + left_right