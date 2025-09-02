

def solution(players, callings):
    player_to_rank = {player: i for i, player in enumerate(players)}
    
    for player in callings:
        rank = player_to_rank[player]
        
        ahead_player = players[rank - 1]
        ahead_rank = rank - 1
    
        players[rank], players[ahead_rank] = players[ahead_rank], players[rank]
        
        player_to_rank[player] = ahead_rank
        player_to_rank[ahead_player] = rank

    return players