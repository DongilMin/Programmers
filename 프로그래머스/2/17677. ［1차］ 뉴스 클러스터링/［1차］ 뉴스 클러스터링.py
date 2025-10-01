from collections import Counter


def solution(str1, str2):
    
    multiset1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    multiset2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    
    counter1 = Counter(multiset1)
    counter2 = Counter(multiset2)
    
    intersection_size = sum((counter1 & counter2).values())
    union_size = sum((counter1 | counter2).values())
    
    if union_size == 0:
        return 65536
    
    j = intersection_size / union_size
    
    return int(j * 65536)