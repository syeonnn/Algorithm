from itertools import combinations

def solution(nums):
    answer = 0

    for comb in combinations(nums,3):
        flag = True
        sum_3 = sum(comb) 
        for s in range(2, sum_3):
            if sum_3 % s == 0:
                flag = False
                break
        if flag:
            answer += 1

    return answer