def solution(s):
    answer = 0
    cnt1, cnt2 = 0,0
    
    for ch in s:
        if cnt1 == cnt2:
            answer += 1
            cmp = ch
        
        if ch == cmp:
            cnt1 += 1
        else:
            cnt2 += 1
        
    return answer