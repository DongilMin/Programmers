def solution(s):
    s = s[2:-2].split("},{")
    s = sorted(s, key=lambda x:len(x))
    
    s = [list(map(int, a.split(","))) for a in s]
    answer = []
    
    for sub_list in s:
        for ele in sub_list:
            if ele not in answer:
                answer.append(ele)
                break
                
    return answer