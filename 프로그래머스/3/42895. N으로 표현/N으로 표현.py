def solution(N, number):
    answer = 0
    
    if number == N:
        return 1
    
    # 사칙연산 +-*/과 N(1이상 9이하)의 조합으로 숫자 number 만들기
    # dp기준 = N 사용 횟수(1이상 8이하)
    
    # N 사용횟수의 최솟값 구하기
    # N 1회 사용하는 경우
    # N 2회 사용하는 경우 = 1회 사용경우 (연산) 1회 사용경우
    # N 3회 사용하는 경우 = 1회 사용경우 (연산) 2회 사용경우, 2회 사용경우 (연산) 1회 사용경우...
    # 중복 숫자 저장할 필요X -> 각각 횟수 경우의 값들은 set 자료형에 저장
    
    s = [ set() for _ in range(8) ]
    for idx in range(8):
        s[idx].add(int(str(N)*(idx+1))) # N, NN, NNN, ...
    
    for i in range(1,8): # N 사용 횟수 각 케이스들에 대해
        for j in range(i): # 어떤 두 가지 케이스를 결합할 것인지
            for op1 in s[j]: # 첫 번째 피연산자
                for op2 in s[i-j-1]:# 두 번째 피연산자
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
                    
        if number in s[i]:
            answer = i + 1
            return answer
        
    return -1