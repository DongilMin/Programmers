from collections import deque

def solution(cacheSize, cities):
    
    dq = deque(maxlen = cacheSize)
    answer = 0
    
    for city in cities:
        city = city.lower()
        if city in dq and dq:
            answer += 1
            dq.remove(city)
        else:
            answer += 5
            
        dq.append(city)
        
    return answer