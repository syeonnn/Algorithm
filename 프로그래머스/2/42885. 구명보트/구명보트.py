from collections import deque

def solution(people, limit):
    answer = 0
    # 두명의 무게 합이 limit 넘지않도록
    people.sort()
    people = deque(people)
    
    # 가장 무거운 + 가장 가벼운 > limit 이라면
    while people:
        if len(people) == 1:
            people.pop()
        elif people[0] + people[-1] > limit:
            people.pop()
        else:
            people.pop()
            people.popleft()
        answer += 1
            
    # 무거운 사람 혼자 보트 타야함
    return answer