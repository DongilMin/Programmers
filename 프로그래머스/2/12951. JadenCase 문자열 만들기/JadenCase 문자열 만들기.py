def solution(s):
    is_new = True
    answer = ""
    for char in s:
        if char == ' ':
            answer += char
            is_new = True
        elif is_new:
            answer += char.upper()
            is_new = False
        else:
            answer += char.lower()
    return answer