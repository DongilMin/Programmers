from collections import Counter

def solution(k, tangerine):
    
    counts = Counter(tangerine)
    sorted_counts = sorted(counts.values(), reverse=True)
    
    box_cnt = 0
    type_cnt = 0
    
    for box in sorted_counts:
    
        box_cnt += box
        type_cnt += 1

        if box_cnt >= k:
            break
    
    return type_cnt