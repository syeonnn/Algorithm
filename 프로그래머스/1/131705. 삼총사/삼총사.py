import itertools

def solution(number):
    answer = 0
    # 3명의 정수 번호를 더했을 때 0이 되면 '삼총사'!
    # 삼총사를 만들 수 있는 방법의 수
    
    for element in itertools.combinations(number, 3):
        if sum(element) == 0:
            answer += 1
        
    return answer