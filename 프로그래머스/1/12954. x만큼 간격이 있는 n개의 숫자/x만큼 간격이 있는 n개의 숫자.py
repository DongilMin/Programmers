def solution(x, n):
    answer = []
    curr = x
    for i in range(0, n):
        answer.append(curr)
        curr += x
    return answer