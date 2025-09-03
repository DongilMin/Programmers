def solution(clothes):
    counts = {}
    for name, kind in clothes:
        counts[kind] = counts.get(kind, 0) + 1
        
    answer = 1
    for kind in counts:
        answer *= (counts[kind] + 1)
    return answer - 1