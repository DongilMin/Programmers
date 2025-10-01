def solution(numbers):

    # 1. 정답 배열을 -1로 초기화
    answer = [-1] * len(numbers)
    
    # 2. 뒷 큰수를 찾지 못한 숫자들의 '인덱스'를 저장할 스택
    stack = []

    # 3. 배열을 처음부터 끝까지 순회
    for i in range(len(numbers)):
        # 4. 스택이 비어있지 않고, 현재 숫자가 스택 맨 위 인덱스의 숫자보다 크다면
        while stack and numbers[stack[-1]] < numbers[i]:
            # 스택에서 인덱스를 꺼내고, 해당 인덱스의 뒷 큰수는 현재 숫자가 됨
            prev_index = stack.pop()
            answer[prev_index] = numbers[i]
        
        # 5. 현재 인덱스를 스택에 추가
        stack.append(i)
        
    return answer