def solution(word):
    answer = 0
    char_map = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    
    # 각 자릿수별 가중치
    weights = [781, 156, 31, 6, 1]
    
    for i in range(len(word)):
        # 현재 문자에 해당하는 인덱스 * 가중치
        answer += char_map[word[i]] * weights[i]
    
    # 단어 자체의 순서(길이)를 더해줌
    answer += len(word)
    
    return answer