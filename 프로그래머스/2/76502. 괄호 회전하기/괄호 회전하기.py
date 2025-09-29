from collections import deque

def check_correct(s):
    
    mapping = {")": "(", "]": "[", "}": "{"}
    
    stack = []
    
    for char in s:

        if char in "([{":
            stack.append(char)
        
        elif char in ")]}":

            if not stack:
                return False
            
            if stack.pop() != mapping[char]:
                return False

    return not stack

def solution(s):
    
    dq = deque(s)
    
    result = 0
    if check_correct(dq):
       result += 0
        
    for rotate in range(len(s)):
        tmp = dq[0]
        dq.popleft()
        dq.append(tmp)
        if check_correct(dq):
            result += 1
        
    
    return result