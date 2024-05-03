from itertools import permutations


    
def solution(k, dungeons):
    # 현재 피로도 k
    # 최소 필요 피로도 >= 소모 피로도 dungeons     
    # 던전 방문 순서 조정으로 유저가 탐험할수 있는 최대 던전 수 구하기
    answer = -1
    
    def explore(p,hp,idx):
        nonlocal answer
        
        while idx < len(dungeons):
            if hp >= p[idx][0]:
                hp -= p[idx][1]
                idx += 1
                explore(p,hp,idx)
            else:
                answer = max(answer, idx)
                break
        answer = max(answer, idx)
                
    
    permutationList = permutations(dungeons,len(dungeons))
    for idx, p in enumerate(permutationList):
        hp = k
        explore(p,hp,0) # 해당 조합에서 (hp피로도=k 상태로) 첫번째 던전부터 탐색
        if answer == len(dungeons):
            break

    return answer