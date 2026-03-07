from collections import deque

def solution(order):
    dq2 = deque() # 보조 컨테이너 벨트 (스택)
    answer = 0
    idx = 0 # 현재 내가 실어야 하는 order의 인덱스
    
    # 주 컨테이너 벨트에서는 1번부터 순서대로 물건이 나옴
    for box in range(1, len(order) + 1):
        dq2.append(box) # 일단 보조 벨트에 넣음
        
        # 보조 벨트의 맨 위 물건이 현재 실어야 하는 물건(order[idx])과 일치하는 동안 반복
        while dq2 and dq2[-1] == order[idx]:
            dq2.pop() # 보조 벨트에서 꺼내서 트럭에 실음
            answer += 1
            idx += 1
            
    return answer