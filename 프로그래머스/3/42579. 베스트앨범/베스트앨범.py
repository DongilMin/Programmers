from collections import defaultdict

def solution(genres, plays):
    # 1단계: 데이터 재구성 및 합산
    # 장르별로 (재생 수, 고유 번호) 리스트를 저장할 딕셔너리
    genre_songs = defaultdict(list)
    # 장르별 총 재생 횟수를 저장할 딕셔너리
    genre_total_plays = defaultdict(int)

    # enumerate와 zip을 사용해 고유 번호, 장르, 재생 횟수를 한번에 순회
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_songs[genre].append((play, i))
        genre_total_plays[genre] += play

    # 1단계 결과 예시:
    # genre_songs: {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]}
    # genre_total_plays: {'classic': 1450, 'pop': 3100}

    # 2단계: 총 재생 횟수 기준으로 장르 정렬
    # 딕셔너리의 키를 정렬하되, 정렬 기준(key)은 장르별 총 재생 횟수(내림차순)로 지정
    sorted_genres = sorted(genre_total_plays.keys(), key=lambda g: genre_total_plays[g], reverse=True)
    
    # 2단계 결과 예시:
    # sorted_genres: ['pop', 'classic']

    answer = []
    # 3단계: 정렬된 장르 순서대로 순회
    for genre in sorted_genres:
        
        # 4단계: 장르 내 노래 정렬
        # 정렬 기준 1: 재생 수(내림차순), 정렬 기준 2: 고유 번호(오름차순)
        # 튜플을 사용해 다중 조건 정렬: (-play, index)
        # play에 음수(-)를 붙여 내림차순 정렬 효과를 줍니다.
        sorted_songs = sorted(genre_songs[genre], key=lambda song: (-song[0], song[1]))
        
        # 4단계 결과 예시 (genre='pop'일 때):
        # sorted_songs: [(2500, 4), (600, 1)]

        # 5단계: 상위 2곡의 '고유 번호'만 answer에 추가
        for song in sorted_songs[:2]:
            answer.append(song[1]) # song은 (play, index) 튜플이므로, index는 song[1]

    return answer