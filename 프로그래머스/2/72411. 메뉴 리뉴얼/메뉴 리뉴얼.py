from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for size in course:
        
        candidates = []
        for order in orders:
            for card in combinations(sorted(order), size):
                candidates.append("".join(card))

        counter = Counter(candidates)
        
        if counter and max(counter.values()) >= 2:
            max_val = max(counter.values())
            for menu, count in counter.items():
                if count == max_val:
                    answer.append(menu)
                    
    return sorted(answer)