def devide(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(': cnt += 1
        else: cnt -= 1
        if cnt == 0:
            return p[:i+1], p[i+1:]

def is_right(p):
    stack = []
    for char in p:
        if char == '(': stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if not p: return ""
    
    u, v = devide(p)
    
    if is_right(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = u[1:-1]
        temp = ""
        for char in u:
            if char == '(': temp += ')'
            else: temp += '('
        return answer + temp