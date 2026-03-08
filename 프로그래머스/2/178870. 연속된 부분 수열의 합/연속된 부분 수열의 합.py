def solution(sequence, k):
    answer = []
    left = 0
    right = 0
    current_sum = sequence[0]
    min_len = float('inf')

    while right < len(sequence):
        if current_sum == k:
            current_length = right - left
            if current_length < min_len:
                min_len = current_length
                answer = [left, right]
            
            # 합이 k와 같아도 더 짧은 구간이 뒤에 나올 수 있으므로 계속 진행
            current_sum -= sequence[left]
            left += 1
        elif current_sum < k:
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        else:
            current_sum -= sequence[left]
            left += 1

    return answer