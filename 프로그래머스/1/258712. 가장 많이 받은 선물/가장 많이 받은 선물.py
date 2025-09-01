def solution(friends, gifts):
    
    num_friends = len(friends)
    
    name_to_idx = {name: i for i, name in enumerate(friends)}
    
    gift_record = [[0] * num_friends for _ in range(num_friends)]

    for gift in gifts:
        giver, receiver = gift.split()
        gift_record[name_to_idx[giver]][name_to_idx[receiver]] += 1
    
    gift_indicates = [0] * num_friends
    for i in range(num_friends):
        
        total_given = sum(gift_record[i])
        total_received = sum(gift_record[r][i] for r in range(num_friends))
        
        gift_indicates[i] = total_given - total_received
    
    
    next_months_gifts = [0] * num_friends
    for i in range(num_friends):
        for j in range(i + 1, num_friends):
            
            # 규칙 1: 두 사람이 주고받은 선물 개수 비교
            i_gave_to_j = gift_record[i][j]
            j_gave_to_i = gift_record[j][i]
            
            if i_gave_to_j > j_gave_to_i:
                next_months_gifts[i] += 1
            elif i_gave_to_j < j_gave_to_i:
                next_months_gifts[j] += 1
            else:                
                if gift_indicates[i] > gift_indicates[j]:
                    # i의 선물 지수가 더 높으므로 i가 받음
                    next_months_gifts[i] += 1
                elif gift_indicates[j] > gift_indicates[i]:
                    # j의 선물 지수가 더 높으므로 j가 받음
                    next_months_gifts[j] += 1
                # 선물 지수도 같으면 아무도 받지 않음 (규칙 3)
                
    if not next_months_gifts:
        return 0
    return max(next_months_gifts)