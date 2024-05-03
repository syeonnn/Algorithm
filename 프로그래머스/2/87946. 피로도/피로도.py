from itertools import permutations
    
def solution(k, dungeons):
    # k: 현재 피로도have
    # dungeons: 최소 필요 피로도need, 소모 피로도cost 
    # 던전 방문 순서 조정으로 유저가 탐험할수 있는 최대 던전 수 구하기
    answer = -1               
    
    permutationList = permutations(dungeons)
    
    for p in (permutationList):
        have = k
        count = 0
        
        for need, cost in p:
            # 가질 수 있는 최대값이 나오면 for루프 종료
            if answer == len(dungeons):
                break
                
            if have >= need:
                have -= cost
                count += 1
            else:
                answer = max(answer,count)
                break
            answer = max(answer,count)

    return answer