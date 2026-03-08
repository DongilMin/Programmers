from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    target = (s1 + s2) // 2
    
    # 총합이 홀수면 절대 같게 만들 수 없음
    if (s1 + s2) % 2 != 0:
        return -1
    
    limit = len(q1) * 4
    for i in range(limit):
        if s1 == target:
            return i
        
        if s1 > target:
            num = q1.popleft()
            s1 -= num
            q2.append(num)
        else:
            num = q2.popleft()
            s1 += num
            q1.append(num)
            
    return -1