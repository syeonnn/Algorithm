from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    time = 0
    bridge = deque([0] * bridge_length)
    curr_weight = 0
    
    while truck_weights:
        time += 1
        curr_weight -= bridge.popleft()
        
        if curr_weight + truck_weights[0] <= weight :
            curr_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    
    answer = time + bridge_length
    return answer