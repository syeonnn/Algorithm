def solution(s, skip, index):
    answer = ''

    # 실제 연산 = 메인 로직을 단순화하기 위한
    # 데이터 전처리의 중요성!!
    
    ### 모두 아스키 코드로 변환 후 연산하면 길어짐...
    # 다른 방법
    alpha = 'abcdefghijklmnopqrstuvwxyz'    # 26
    # skip 요소 제외시키기
    filterd_alpha = [a for a in alpha if a not in set(skip)]
    result = [filterd_alpha[( filterd_alpha.index(el) + index ) % len(filterd_alpha)] for el in s]
    answer = ''.join(result)
    return answer