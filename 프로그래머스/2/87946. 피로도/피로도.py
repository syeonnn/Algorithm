from itertools import permutations

def solution(k, dungeons):
    # k: 현재 피로도have
    # dungeons: 최소 필요 피로도need, 소모 피로도cost 
    # 던전 방문 순서 조정으로 유저가 탐험할수 있는 최대 던전 수 구하기
    
    arr = permutations(dungeons) # 던전의 순서 배치에 따라 다른 조합들
    ans = -1
    
    for a in arr: # 해당 순서의 조합에 대해
        have = k
        cnt = 0
        for d in a: # 던전 탐색
            if have >= d[0]: # 피로도가 충분하다면
                have -= d[1] # 피로도 소모
                cnt += 1
            
        ans = max(cnt, ans)
            
    return ans