def solution(arr):
    answer = []
    
    for number in arr:
        # 1. answer가 비어있거나, 
        # 2. answer의 마지막 원소가 현재 숫자와 다를 경우에만 추가
        if not answer or answer[-1] != number:
            answer.append(number)
            
    return answer
