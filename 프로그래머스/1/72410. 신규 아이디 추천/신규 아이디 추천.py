def solution(new_id):
    
    # 1단계: 모든 대문자를 소문자로 치환
    answer = new_id.lower()
    
    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    temp_answer = ""
    for char in answer:
        # isalnum(): 알파벳 또는 숫자인지 확인
        if char.isalnum() or char in ['-', '_', '.']:
            temp_answer += char
    answer = temp_answer
    
    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    answer = answer.strip('.')
    
    # 5단계: 빈 문자열이라면, "a"를 대입
    if not answer:  # if len(answer) == 0: 과 동일
        answer = 'a'
        
    # 6단계: 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거.
    #        제거 후 마침표(.)가 끝에 위치한다면 끝의 마침표(.) 문자를 제거.
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')
        
    # 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임.
    while len(answer) <= 2:
        answer += answer[-1]
        
    return answer