import json

top_track_weight = 1.25
mid_track_weight = .75
good_track_weight = 1

# open all time file
with open(f'./data/favorites/music/music_all_time.json', 'r') as json_file: 
    all_time_data = json.load(json_file)

for album in all_time_data:
    top_tracks = len(all_time_data[album]['top_tracks'])*top_track_weight
    mid_tracks = len(all_time_data[album]['mid_tracks'])*mid_track_weight
    good_tracks = len(all_time_data[album]['good_tracks'])*good_track_weight

    total_tracks = all_time_data[album]['total_tracks']

    score = (top_tracks + mid_tracks + good_tracks)/(total_tracks*top_track_weight)

    all_time_data[album]['algo_score'] = round(score * 10, 2)
    score = all_time_data[album]['algo_score'] 

    avg_score = round((score + all_time_data[album]['asboyer_score']) / 2, 2)

    # if avg_score > score:
    #   keep it unless score is below a 7

    if avg_score < score and all_time_data[album]['asboyer_score'] > 7:
        print(all_time_data[album]['name'])
        avg_score = score

    all_time_data[album]['score'] = avg_score

with open(f'./data/favorites/music/music_all_time.json', 'w') as json_file: 
    json.dump(all_time_data, json_file, indent=4)

# current favs file
with open(f'./data/favorites/music/music_current.json', 'r') as json_file: 
    all_time_data = json.load(json_file)

# if currently reviewing the album    
for album in all_time_data:
    try:
        if len(all_time_data[album]['tracks']) > 0:
            go = False
        else:
            go = True
    except:
        go = True

    if go:
        top_tracks = len(all_time_data[album]['top_tracks'])*top_track_weight
        mid_tracks = len(all_time_data[album]['mid_tracks'])*mid_track_weight
        good_tracks = len(all_time_data[album]['good_tracks'])*good_track_weight

        total_tracks = all_time_data[album]['total_tracks']
        score = (top_tracks + mid_tracks + good_tracks)/(total_tracks*top_track_weight)

        all_time_data[album]['algo_score'] = round(score * 10, 2)
        score = all_time_data[album]['algo_score']


        avg_score = round((score + all_time_data[album]['asboyer_score']) / 2, 2)

        # if avg_score > score:
        #   keep it unless score is below a 7

        if avg_score > score and score > 7:
            avg_score = score

        all_time_data[album]['score'] = avg_score

with open(f'./data/favorites/music/music_current.json', 'w') as json_file: 
    json.dump(all_time_data, json_file, indent=4)