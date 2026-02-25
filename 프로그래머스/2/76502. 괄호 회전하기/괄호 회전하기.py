from collections import deque

def check(s):
    mapping = {")" : "(", "]" : "[", "}" : "{"}
    stack = []
    
    for c in s:
        if c in "[({":
            stack.append(c)
        else:
            if not stack:
                return False
            if stack.pop() != mapping[c]:
                return False
            
    return not stack
    
def solution(s):
    answer = 0
    dq = deque(s)
    
    for i in range(len(s)):
        
        if check(dq):
            answer += 1
            
        tmp = dq[0]
        dq.popleft()
        dq.append(tmp)
        
    return answer
        