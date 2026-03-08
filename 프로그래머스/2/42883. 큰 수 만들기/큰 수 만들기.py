def solution(number, k):
    answer = ''
    
    stack = []
    cnt = 0

    
    for num in number:
        
        while stack and k > 0 and num > stack[-1]:
            stack.pop()
            k -= 1
            
        stack.append(num)
    
    while k > 0:
        stack.pop()
        k -= 1
        
    return ''.join(stack)
