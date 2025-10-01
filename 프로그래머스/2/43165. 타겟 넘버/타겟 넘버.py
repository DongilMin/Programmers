def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(index, current_sum):
        # 1. 탈출 조건: 모든 숫자를 다 사용했을 때
        if index == n:
            # 타겟 넘버와 현재 합계가 같으면 1을 반환 (방법 1개 찾음)
            if current_sum == target:
                return 1
            # 다르면 0을 반환
            else:
                return 0
        
        # 2. 재귀 호출: 현재 숫자를 더하거나 빼는 두 가지 경우를 모두 탐색
        # 현재 숫자를 더하는 경우의 수
        add_case = dfs(index + 1, current_sum + numbers[index])
        # 현재 숫자를 빼는 경우의 수
        subtract_case = dfs(index + 1, current_sum - numbers[index])
        
        # 두 경우의 수를 합산하여 반환
        return add_case + subtract_case

    # 시작점(index=0, sum=0)에서 DFS 시작
    answer = dfs(0, 0)
    return answer