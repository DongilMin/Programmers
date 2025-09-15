from collections import defaultdict

def solution(genres, plays):
    
    genre_songs = defaultdict(list)
    genre_total_plays = defaultdict(int)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_songs[genre].append((play, i))
        genre_total_plays[genre] += play
    
    sorted_genres = sorted(genre_total_plays.keys(), key=lambda x:genre_total_plays[x], reverse=True)
    
    answer = []
    for genre in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key=lambda song: (-song[0], song[1]))
        
        for song in sorted_songs[:2]:
            answer.append(song[1])
    return answer
    
    
    
    
    
    
    
    
    
    
    
    