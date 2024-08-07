def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for target in babbling:
        for c in can:
            if c*2 not in target:
                target = target.replace(c,' ')

        if len(target.strip())==0:
            answer += 1
                
    return answer