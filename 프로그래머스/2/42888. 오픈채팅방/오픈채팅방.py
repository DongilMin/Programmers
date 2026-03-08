def solution(record):
    user_db = {} 
    
    for r in record:
        parts = r.split() 
        command = parts[0]
        uid = parts[1]
        
        if command in ["Enter", "Change"]:
            nickname = parts[2]
            user_db[uid] = nickname
    
    result = []
    for r in record:
        parts = r.split() 
        command = parts[0]
        uid = parts[1]
        if command == "Enter":
            result.append(f"{user_db[uid]}님이 들어왔습니다.")
        elif command == "Leave":
            result.append(f"{user_db[uid]}님이 나갔습니다.")
    return result