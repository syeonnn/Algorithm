def solution(number):
    answer = 0
    # 3명의 정수 번호를 더했을 때 0이 되면 '삼총사'!
    # 삼총사를 만들 수 있는 방법의 수
    l = len(number)
    
    for i in range(0, l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
     
    return answer