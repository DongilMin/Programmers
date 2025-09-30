from collections import deque

def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return len(cities) * 5

    total_time = 0
    cache = deque(maxlen=cacheSize)

    for city in cities:
        s_city = city.lower()

        if s_city in cache:
            total_time += 1

            cache.remove(s_city)
            cache.append(s_city)

        else:
            total_time += 5
            cache.append(s_city)
            
    return total_time