from itertools import product

def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    result = []
    
    # # 1. 중복순열
    # # 5**5 로 모든 경우의 수에 대해 배열 생성
    # for i in range(1,6):
    #     for a in product(alpha, repeat = i):
    #         result.append(''.join(a))
    # result.sort()
    # # word가 해당하는 인덱스 값 + 1 반환
    # answer = result.index(word) + 1
    
    # 2. 재귀
    # 0~4 인덱스에 대해 순서대로 'A'~'U' 대입
    cnt = -1
    
    def func(x, string):
        nonlocal cnt, answer
        if x <= 5:
            cnt += 1
            if string == word:
                answer = cnt
                return
        else:
            return
        
        for i in range(5):
            func(x+1, string+alpha[i])
            
    func(0, '')
    
    return answer