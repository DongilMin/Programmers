def solution(prices):
    # 정답을 저장할 리스트를 prices의 길이만큼 0으로 초기화
    answer = [0] * len(prices)
    
    # 각 가격을 기준으로 순회 (i는 기준 시점)
    for i in range(len(prices)):
        # i 이후의 가격들을 순회 (j는 비교 시점)
        for j in range(i + 1, len(prices)):
            # 1초가 흘렀으므로 i 시점의 유지 시간을 1 늘려줌
            answer[i] += 1
            # 가격이 떨어졌다면 더 이상 볼 필요가 없으므로 내부 반복 중단
            if prices[i] > prices[j]:
                break
                
    return answer