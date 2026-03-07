from collections import deque

def solution(priorities, location):
    dq = deque([(p, i) for i, p in enumerate(priorities)])
    
    answer = 0
    
    while dq:
        
        curr = dq.popleft()
        
        if any(curr[0] < other[0] for other in dq):
            dq.append(curr)
        else:
            answer += 1
            if location == curr[1]:
                return answer
    return answer