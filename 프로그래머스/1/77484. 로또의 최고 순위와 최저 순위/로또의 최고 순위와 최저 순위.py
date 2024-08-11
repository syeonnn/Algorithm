from collections import Counter

def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}

    arr = Counter(lottos)
    cnt0 = arr[0]
    temp = 0 # 알아볼 수 있는 번호들 중 당첨번호와 같은 번호 개수
    for num in win_nums:
        temp += arr[num]
    
    if cnt0 == 0:
        answer = [rank[temp], rank[temp]]
    else:
        high = temp + cnt0 if temp <= 6-cnt0 else 6
        low = temp
        answer = [rank[high], rank[low]]
    
    return answer # 당첨 가능한 최고 순위와 최저 순위