def solution(numbers):
    answer = 45 # -1
    
    for n in numbers:
        answer -= n
    
    return answer # numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수