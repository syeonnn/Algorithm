def solution(h1, m1, s1, h2, m2, s2):
    answer = -1

    def cal(h,m,s):        
        # 기준 시각에서의 시침, 분침, 초침의 위치
        # 시침 이동 각도 계산) 1시간:30도, 1분:1/2, 1초:1/120
        [h_degree, m_degree, s_degree] = [(h*30 + m*1/2 + s*1/120)%360, (m*6 + s*1/10)%360, s*6]
        # 0시 0분 0초일 때 알람 한 번만 울림!
        temp = -1
        
        # 매분(=60초)마다 초침은 시계 한 바퀴를 돌면서 시침, 분침과 겹쳐짐
        temp += (h*60 + m)*2
        
        # 마지막 초침의 위치에 따라
        if s_degree >= m_degree: temp += 1
        if s_degree >= h_degree: temp += 1

        # 예외 처리
        # 59분 -> 00분 : 분침과 초침 겹치지 않음
        temp -= h
        # 11시 -> 12시 : 시침과 초침 겹치지 않음, 24시는 포함X
        # 12시 정각에는 한 번만 울림!
        if h >= 12: temp -= 2
        
        return temp
    
    # 0시 0분 0초 ~ ?시 ?분 ?초까지 알람 울리는 횟수의 뺄셈
    answer = cal(h2, m2, s2) - cal(h1, m1, s1)
    
    # 시작 시각이 0시와 12시인 경우에는 1씩 더해줌
    if ((h1 == 0 or h1 == 12) and (m1 == 0 and s1 == 0)):
       answer +=1
    
    return answer