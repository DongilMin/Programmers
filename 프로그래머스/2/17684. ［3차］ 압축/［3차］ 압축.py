def solution(msg):

    answer = []
    
    dictionary = {chr(ord('A') + i): i + 1 for i in range(26)}
    next_index = 27

    i = 0
    while i < len(msg):

        w = msg[i]
        j = i + 1

        while j < len(msg) and msg[i:j+1] in dictionary:
            j += 1
        
        w = msg[i:j]

        answer.append(dictionary[w])

        if j < len(msg):
            c = msg[j]
            dictionary[w + c] = next_index
            next_index += 1
        
        i += len(w)

    return answer