import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    while scoville[0] < K:
        
        if len(scoville) < 2:
            return -1
        
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)
        
        new_scoville = first_min + (second_min * 2)
        heapq.heappush(scoville, new_scoville)
        cnt += 1
    return cnt