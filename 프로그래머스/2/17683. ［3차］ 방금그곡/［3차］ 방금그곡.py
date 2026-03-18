def change_note(s):
    # #이 붙은 음을 소문자 한 글자로 치환
    return s.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", "b")

def solution(m, musicinfos):
    answer = "(None)"
    max_time = 0
    m = change_note(m) # 찾으려는 멜로디 치환
    
    for musicinfo in musicinfos:
        start, end, title, info = musicinfo.split(',')
        
        # 재생 시간 계산
        sh, sm = map(int, start.split(':'))
        eh, em = map(int, end.split(':'))
        time = (eh * 60 + em) - (sh * 60 + sm)
        
        # 악보 치환 및 실제 재생된 악보 생성
        info = change_note(info)
        # 재생 시간만큼 악보를 반복하거나 자름
        full_music = (info * (time // len(info) + 1))[:time]
        
        # 멜로디 포함 여부 확인
        if m in full_music:
            if time > max_time: # 재생 시간이 더 긴 것만 갱신
                max_time = time
                answer = title
                
    return answer