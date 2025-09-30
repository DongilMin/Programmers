import re
from collections import Counter

def solution(s):
    numbers = re.findall(r'\d+', s)
    
    counts = Counter(numbers)
    
    sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    
    answer = [int(item[0]) for item in sorted_items]
    
    return answer