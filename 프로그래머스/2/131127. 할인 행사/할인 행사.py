from collections import Counter
from collections import defaultdict

def solution(want, number, discount):
    
    want_dict = defaultdict(int)
    
    result = 0
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    for day in range(len(discount) - 9):
        sub_sequence = discount[day:day + 10]
        
        if Counter(sub_sequence) == want_dict:
            result += 1
    
    return result