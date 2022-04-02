import json

with open(f'./data/favorites/music/music_all_time.json', 'r') as json_file: 
    all_time_data = json.load(json_file)

top = ['Kanye West', 
    'Playboi Carti', 
    'Lil Uzi Vert', 
    'Michael Jackson', 
    'Post Malone', 
    'Don Toliver', 
    'Childish Gambino', 
    'Drake', 
    'Drake, Future', 
    'Travis Scott', 
    'J. Cole',
    'Maroon 5',
    'Jack Johnson',
    'Future, Juice WRLD',
    'Khalid',
    'Trippie Redd',
    'The Weekend',
    'Old Dominion',
    'Tory Lanez',
    'Miles Davis',
    'Tim McGraw',
    'Kendrick Lamar',
    'Fleetwood Mac',
    'Radiohead',
    'Ariana Grande',
    'Bryson Tiller'
    ]

top_a = ['?', 'Boston', 'Hoodie SZN', 'Loose', 'Confessions of a Dangerous Mind', 'So Much Fun', 'Flower Boy', 'Thats What They All Say', 'Sweet Action']
for album in all_time_data:
    if all_time_data[album]['artists'] in top or all_time_data[album]['name'] in top_a:
        if all_time_data[album]['name'] == 'Graduation':
            score = .98
        elif all_time_data[album]['name'] == "My Beautiful Dark Twisted Fantasy":
            score = .925
        # elif all_time_data[album]['name'] == 'Late Registration':
        #     score = .979
        else:
            score = (len(all_time_data[album]['top_tracks'])*1.5 + len(all_time_data[album]['good_tracks'])*1.25)/(all_time_data[album]['total_tracks']*1.5)
    elif all_time_data[album]['artists'] == 'Frank Ocean':
        score = (len(all_time_data[album]['top_tracks'])*2 + len(all_time_data[album]['good_tracks'])*1.87)/(all_time_data[album]['total_tracks']*2)
    else:
        score = (len(all_time_data[album]['top_tracks'])*1.4 + len(all_time_data[album]['good_tracks']))/(all_time_data[album]['total_tracks']*1.4)
    all_time_data[album]['score'] = round(score * 10, 2)


with open(f'./data/favorites/music/music_all_time.json', 'w') as json_file: 
    json.dump(all_time_data, json_file, indent=4)


with open(f'./data/favorites/music/music_current.json', 'r') as json_file: 
    all_time_data = json.load(json_file)

for album in all_time_data:
    if all_time_data[album]['artists'] in top or all_time_data[album]['name'] in top_a:
        if all_time_data[album]['name'] == 'Graduation':
            score = .99
        elif all_time_data[album]['name'] == "My Beautiful Dark Twisted Fantasy":
            score = .925
        else:
            score = (len(all_time_data[album]['top_tracks'])*1.5 + len(all_time_data[album]['good_tracks'])*1.25)/(all_time_data[album]['total_tracks']*1.5)
    else:
        score = (len(all_time_data[album]['top_tracks'])*1.4 + len(all_time_data[album]['good_tracks']))/(all_time_data[album]['total_tracks']*1.4)
    all_time_data[album]['score'] = round(score * 10, 2)


with open(f'./data/favorites/music/music_current.json', 'w') as json_file: 
    json.dump(all_time_data, json_file, indent=4)