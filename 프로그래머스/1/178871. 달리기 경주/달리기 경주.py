def solution(players, callings):
    # answer = []

    players_dict = { p: i for i, p in enumerate(players) }

    for name in callings:
        idx = players_dict[name]    
        # players배열의 idx번째 요소와 idx-1번째 요소를 swap
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        players_dict[players[idx]] = idx
        players_dict[players[idx-1]] = idx-1
        
    return players   # 선수들의 이름을 1등부터 등수 순서대로