import json

with open(f'./data/favorites/music/music_all_time.json', 'r') as json_file: 
    all_time_data = json.load(json_file)

for album in all_time_data:
    score = (len(all_time_data[album]['top_tracks'])*1.25 + len(all_time_data[album]['good_tracks'])*.75)/(all_time_data[album]['total_tracks']*1.25)
    all_time_data[album]['score'] = round(score * 10, 2)


with open(f'./data/favorites/music/music_all_time.json', 'w') as json_file: 
    json.dump(all_time_data, json_file, indent=4)