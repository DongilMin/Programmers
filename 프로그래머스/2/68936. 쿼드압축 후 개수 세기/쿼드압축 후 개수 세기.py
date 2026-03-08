def solution(arr):
    results = [0, 0] # [0의 개수, 1의 개수]

    def compress(x, y, n):
        # 1. 시작점의 숫자 확인
        initial_val = arr[x][y]
        
        # 2. 영역 내 모든 숫자가 같은지 검사
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != initial_val:
                    # 3. 하나라도 다르면 4분할 재귀 호출
                    half = n // 2
                    compress(x, y, half)           # 왼쪽 위
                    compress(x, y + half, half)    # 오른쪽 위
                    compress(x + half, y, half)    # 왼쪽 아래
                    compress(x + half, y + half, half) # 오른쪽 아래
                    return

        # 4. 모두 같다면 해당 숫자 카운트 증가
        results[initial_val] += 1

    compress(0, 0, len(arr))
    return results