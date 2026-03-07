from collections import Counter

def solution(str1, str2):
    
    m1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    m2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]
    
    counter1 = Counter(m1)
    counter2 = Counter(m2)
    
    i_size = sum((counter1 & counter2).values())
    u_size = sum((counter1 | counter2).values())
    
    if u_size == 0:
        return 65536
    
    return int (i_size / u_size * 65536)