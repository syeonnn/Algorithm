from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    time = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    curr_weight = 0
    
    while trucks:
        time += 1
        curr_weight -= bridge.popleft()
        
        if curr_weight + trucks[0] <= weight :
            curr_weight += trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
    
    answer = time + bridge_length
    return answer