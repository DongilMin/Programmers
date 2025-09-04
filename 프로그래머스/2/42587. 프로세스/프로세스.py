from collections import deque, defaultdict

def solution(priorities, location):
    answer = 0
    
    # 1. 큐를 생성하되, (우선순위, 원래 위치)를 함께 저장합니다.
    # enumerate를 사용하여 인덱스와 값을 튜플로 묶고 deque로 변환합니다.
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    while queue:
        # 2. 큐의 가장 앞에 있는 프로세스를 꺼냅니다.
        current_process = queue.popleft()
        current_priority = current_process[0]
        current_location = current_process[1]
        
        # 3. 큐에 남아있는 프로세스 중 우선순위가 더 높은 것이 있는지 확인합니다.
        # any() 함수는 하나라도 True이면 True를 반환하므로 효율적입니다.
        if any(current_priority < other_process[0] for other_process in queue):
            # 3-1. 있다면, 현재 프로세스를 큐의 맨 뒤로 보냅니다.
            queue.append(current_process)
        else:
            # 3-2. 없다면, 현재 프로세스를 실행합니다.
            answer += 1
            
            # 4. 실행된 프로세스가 우리가 찾던 프로세스인지 확인합니다.
            if current_location == location:
                return answer