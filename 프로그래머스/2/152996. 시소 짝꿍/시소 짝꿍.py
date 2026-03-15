from collections import Counter

def solution(weights):
    answer = 0
    
    weights = Counter(weights)
    
    for w in weights:
        if weights[w] > 1:
            answer += weights[w] * (weights[w] - 1) // 2
            
    counter = sorted(weights.keys())
    
    for w in counter:
        for t in [3/2, 4/2, 4/3]:
            target = w * t
            if target in counter:
                answer += weights[w] * weights[target]
    
    return answer

