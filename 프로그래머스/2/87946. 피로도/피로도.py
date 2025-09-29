from itertools import permutations

def solution(k, dungeons):
    
    arr = permutations(dungeons)
    
    result = 0
    
    for curr in arr:
        hp = k
        cnt = 0
        for d in curr:
            if hp < d[0]:
                break
            elif hp < d[1]:
                break
            else:
                hp -= d[1]
                cnt += 1
        result = max(result, cnt)
    
    return result