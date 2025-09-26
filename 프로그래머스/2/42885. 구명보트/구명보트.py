def solution(people, limit):

    # 1. 사람들을 몸무게순으로 정렬합니다.
    people.sort()
    
    answer = 0
    left = 0  # 가장 가벼운 사람의 인덱스
    right = len(people) - 1  # 가장 무거운 사람의 인덱스
    
    # 2. 모든 사람이 구출될 때까지 반복합니다.
    while left <= right:
        # 보트를 하나 사용합니다.
        answer += 1
        
        # 3. 가장 무거운 사람과 가장 가벼운 사람을 함께 태울 수 있는지 확인합니다.
        if people[left] + people[right] <= limit:
            # 함께 태울 수 있다면, 가장 가벼운 사람도 보트에 탑니다.
            left += 1
            
        # 가장 무거운 사람은 항상 보트에 탑니다.
        right -= 1
            
    return answer
