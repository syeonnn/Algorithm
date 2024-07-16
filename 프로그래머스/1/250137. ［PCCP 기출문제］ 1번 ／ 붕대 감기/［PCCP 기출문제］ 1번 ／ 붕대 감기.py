def solution(bandage, health, attacks):
    answer = 0
    
    # bandage =  [시전 시간, 초당 회복량, 추가 회복량]
    [skill_time, skill_power, skill_plus] = bandage
    # t초 동안 : 1초마다 x만큼
    # t초 연속 성공 : y만큼의 체력 추가
    
    # health 최대체력
    # attacks = [공격 시간, 피해량] 
    
    # 남은 체력을 return 
    hp = health # 남은 체력
    skill_check = 0
    flag = True
    
    for i in range(1, attacks[-1][0]+1):    # 시간에 대해
        flag = True
        
        if hp <= 0:
            answer = -1
            break

        for attack in attacks:  
            if attack[0] == i:  # 공격당하면
                flag = False
                hp -= attack[1]
                break
                
        if flag:
            skill_check += 1
            hp += skill_power
            
        elif not flag:
            skill_check = 0
            
        if skill_check == skill_time:
            skill_check = 0
            hp += skill_plus
            
        if hp >= health:
            hp = health

    return hp if hp > 0 else -1