import json

with open(f'./data/favorites/music/music_all_time.json', 'r') as json_file: 
    all_time_data = json.load(json_file)

for album in all_time_data:
    if 'Kanye' in all_time_data[album]['artists']:
        if all_time_data[album]['name'] == 'Graduation':
            score = .99
        else:
            score = (len(all_time_data[album]['top_tracks'])*1.5 + len(all_time_data[album]['good_tracks'])*1.25)/(all_time_data[album]['total_tracks']*1.5)
    else:
        score = (len(all_time_data[album]['top_tracks'])*1.4 + len(all_time_data[album]['good_tracks']))/(all_time_data[album]['total_tracks']*1.4)
    all_time_data[album]['score'] = round(score * 10, 2)


with open(f'./data/favorites/music/music_all_time.json', 'w') as json_file: 
    json.dump(all_time_data, json_file, indent=4)