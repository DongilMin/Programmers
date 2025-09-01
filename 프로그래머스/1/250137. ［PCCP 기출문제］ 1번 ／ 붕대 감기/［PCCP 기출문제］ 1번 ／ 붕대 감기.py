def solution(bandage, health, attacks):
    # attacks 배열을 공격 시간 순으로 정렬
    attacks.sort()
    
    time = 0
    succ_heal = 0
    curr_hp = health
    attack_idx = 0  # 다음에 올 공격의 인덱스를 추적
    
    # 마지막 공격 시간까지만 시뮬레이션
    last_attack_time = attacks[-1][0]

    while time <= last_attack_time:
        attack_time, damage = attacks[attack_idx]
        
        # 현재 시간이 다음 공격 시간과 일치하는가?
        if time == attack_time:
            # 1. 공격 받음
            curr_hp -= damage
            succ_heal = 0  # 연속 성공 초기화
            
            # 2. 사망 여부 체크
            if curr_hp <= 0:
                return -1
            
            # 다음 공격을 가리키도록 인덱스 증가
            attack_idx += 1
            
        else:
            # 3. 공격이 없는 경우, 회복
            # 최대 체력이 아닐 때만 회복
            if curr_hp < health:
                curr_hp += bandage[1]  # 초당 회복
                succ_heal += 1
                
                # 추가 회복 조건 달성
                if succ_heal == bandage[0]:
                    curr_hp += bandage[2]
                    succ_heal = 0 # 추가 회복 후 연속 성공 초기화
                
                # 회복 후 체력이 최대 체력을 넘지 않도록 조정
                if curr_hp > health:
                    curr_hp = health

        # 시간 1초 증가
        time += 1
        
    return curr_hp