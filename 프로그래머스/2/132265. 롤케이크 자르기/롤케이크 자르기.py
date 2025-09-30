from collections import Counter

def solution(topping):

    answer = 0
    
    # 철수(왼쪽 조각)의 토핑을 관리할 Counter
    chulsoo_toppings = Counter()
    
    # 동생(오른쪽 조각)의 토핑을 관리할 Counter (초기에는 모든 토핑을 가짐)
    brother_toppings = Counter(topping)
    
    # 롤케이크를 왼쪽부터 순회하며 토핑을 하나씩 철수에게 넘겨줍니다.
    for t in topping:
        # 1. 철수에게 토핑 추가
        chulsoo_toppings[t] += 1
        
        # 2. 동생의 토핑에서 제거
        brother_toppings[t] -= 1
        # 만약 해당 토핑의 개수가 0이 되면, Counter에서 키를 완전히 삭제합니다.
        # 이렇게 해야 토핑의 '종류' 수를 정확히 셀 수 있습니다.
        if brother_toppings[t] == 0:
            del brother_toppings[t]
            
        # 3. 두 사람의 토핑 종류 수가 같은지 확인
        if len(chulsoo_toppings) == len(brother_toppings):
            answer += 1
            
    return answer