def solution(s):
    s_lower = s.lower()
    result = []
    
    is_new_word = True
    
    for char in s_lower:
        if char == ' ':
            result.append(char)
            is_new_word = True
        elif is_new_word:
            result.append(char.upper())
            is_new_word = False
        else:
            result.append(char)
    
    return "".join(result)