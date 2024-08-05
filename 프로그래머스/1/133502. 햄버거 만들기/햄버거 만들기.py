def solution(ingredient):
    answer = 0
    # 빵 – 야채 – 고기 - 빵 : 1-2-3-1
    
    temp = []
    for igd in ingredient:
        temp.append(igd)
        # 아이디어 !! -4 인덱스에서부터 탐색 시작하는 것 !! 시간초과 해결은 : remove아닌 pop
        if temp[-4:] == [1,2,3,1]:
            for _ in range(4):
                temp.pop()
            answer += 1
            
    return answer