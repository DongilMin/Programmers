def solution(storey):
    def find_min(n):
        if n < 10:
            return min(n, 10 - n + 1)
        
        remainder = n % 10
        # 현재 자릿수를 버리는 경우 vs 올림을 하는 경우 중 최솟값 선택
        return min(remainder + find_min(n // 10), (10 - remainder) + find_min(n // 10 + 1))
    
    return find_min(storey)