def solution(mats, park):
    # 1. 가장 큰 돗자리부터 확인하기 위해 내림차순으로 정렬
    mats.sort(reverse=True)
    
    rows = len(park)
    cols = len(park[0])
    
    for k in mats:
        for r in range(rows - k + 1):
            for c in range(cols - k + 1):
                
                is_empty = True
                for i in range(r, r + k):
                    for j in range(c, c + k):
                        # 사람이 있는 칸을 발견하면 해당 공간은 사용 불가
                        if park[i][j] != "-1":
                            is_empty = False
                            break  # 안쪽 반복문 탈출
                    if not is_empty:
                        break  # 바깥쪽 반복문도 탈출
                if is_empty:
                    return k
    return -1
                