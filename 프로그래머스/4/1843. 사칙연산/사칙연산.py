import math

def solution(arr):
    answer = -1
    # 연산자 종류에 따라 max/min
    # 범위별 max값: dp[][][0]
    # 범위별 min값: dp[][][1]
    
    # 연산자와 숫자 별도 저장
    op = [a for a in arr if a=='-' or a=='+'] 
    nums = [int(n) for n in arr if n!='-' and n!='+']
    
    N = len(nums)
    dp_max = [ [-float('inf')] * N for _ in range(N)]
    dp_min = [ [float('inf')] * N for _ in range(N)]
    
    for length in range(N): # 연산 범위 (=괄호 너비)를 넓혀나감
        # 01, 12, 23, 02, 13, 03, ...이러한 범위로 연산하도록!!
        
        # 01, 02, 03, 12, 13, 23, ...이렇게 dp 연산하면
        # 의도(자유롭게 괄호 배치)에 맞는 연산이 안됨
        
        for start in range(N-length):   
            end = start+length
            if start == end:
                dp_min[start][end] = dp_max[start][end] = nums[start]
                continue
                
            for mid in range(start,end):
                if op[mid] == '+':
                    dp_min[start][end] = min(dp_min[start][mid] + dp_min[mid+1][end], dp_min[start][end])
                    dp_max[start][end] = max(dp_max[start][mid] + dp_max[mid+1][end], dp_max[start][end])
                elif op[mid] == '-':
                    dp_min[start][end] = min(dp_min[start][mid] - dp_max[mid+1][end], dp_min[start][end])
                    dp_max[start][end] = max(dp_max[start][mid] - dp_min[mid+1][end], dp_max[start][end])
                

    answer = dp_max[0][-1]
    
    return answer