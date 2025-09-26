from collections import Counter

def solution(k, tangerine):
    counts = Counter(tangerine)
    
    sorted_counts = sorted(counts.values(), reverse=True)
    
    box_count = 0  # 상자에 담은 귤의 총 개수
    type_count = 0 # 귤의 종류 수
    
    # 3. 개수가 많은 순서대로 상자를 채웁니다.
    for count in sorted_counts:
        box_count += count
        type_count += 1
        
        # 상자에 담은 귤의 개수가 k 이상이 되면 멈춥니다.
        if box_count >= k:
            break
            
    return type_count