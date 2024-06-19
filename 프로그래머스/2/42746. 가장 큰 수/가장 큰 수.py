def solution(numbers):
    answer = ''
    
    # 숫자를 문자열로 취급해서 정렬
    numbers_str = [str(n) for n in numbers]
    # 3과 30을 비교했을 때 3을 더 큰 수 취급해야함 -> 1000이하의 자릿수로 채우기
    numbers_str.sort(key=lambda x: x*3, reverse=True)
   
    answer += ''.join(numbers_str)

    # 반례: numbers 값이 모두 0일 경우
    # flag = False
    # for a in answer:
    #     if a != '0':
    #         flag = True
    #         break
            
    if numbers_str[0] == '0':
        return '0'
            
    # return answer if flag else '0'
    return answer