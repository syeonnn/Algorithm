def solution(a, b, n):
    answer = 0
    
    # a개 주면 b개 받음
    # 갖고 있는 병 개수 n개
    
    while n >= a :
        answer += (n // a) * b # 받은 콜라 병 개수
        n = (n // a) * b + n % a
            
    return answer