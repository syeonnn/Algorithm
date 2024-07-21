def solution(name, yearning, photo): # 사람 이름, 이름별 그리움 점수, 사진 속 인물 이름    
    answer = []
    name_yearning = dict()
    for i in range(len(name)):
        name_yearning[name[i]] = yearning[i]
        
    for pho in photo:
        temp = 0
        for p in pho:
            if p in name_yearning:
                temp += name_yearning[p]
        answer.append(temp)
    return answer