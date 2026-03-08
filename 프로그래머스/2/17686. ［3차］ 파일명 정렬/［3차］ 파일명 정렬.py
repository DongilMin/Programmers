def solution(files):
    temp = []
    for file in files:
        num_start = -1
        for i in range(len(file)):
            if file[i].isdigit():
                num_start = i
                break
        head = file[:num_start]
        
        num_end = num_start
        for i in range(num_start, len(file)):
            if file[i].isdigit() and (i - num_end) < 5:
                num_end += 1
            else:
                break
        number = file[num_start:num_end]
        tail = file[num_end:]
        
        temp.append((head, number, tail))
        temp.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    answer = []
    for h, n, t in temp:
        answer.append(h + n + t)
    return answer