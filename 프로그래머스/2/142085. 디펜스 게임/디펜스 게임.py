import heapq

def solution(n, k, enemy):
    pq = [] # 최소 힙
    
    for i, e in enumerate(enemy):
        heapq.heappush(pq, e) # 우선 무적권 사용 목록에 추가
        
        if len(pq) > k: # 무적권 개수를 초과하면
            n -= heapq.heappop(pq) # 가장 적은 적이 있던 라운드에 병사 투입
            
        if n < 0: # 병사가 부족하면 종료
            return i
            
    return len(enemy) # 모든 라운드 방어 성공