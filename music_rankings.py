import json

with open(f'./data/favorites/music/music_all_time.json', 'r') as json_file: 
    all_time_data = json.load(json_file)

top = ['Kanye West', 
    'Michael Jackson', 
    'Post Malone', 
    'Don Toliver', 
    'Childish Gambino', 
    'Drake', 
    'Travis Scott', 
    'J. Cole',
    'Maroon 5',
    'Jack Johnson',
    'Khalid',
    'Trippie Redd',
    'Old Dominion',
    'Miles Davis',
    'Tim McGraw',
    'Kendrick Lamar',
    'Fleetwood Mac',
    'Radiohead',
    'Ariana Grande',
    'Bryson Tiller',
    'Nirvana',
    'AC/DC',
    'Baby Keem',
    "BROCKHAMPTON",
    'Polo G',
    'Duke Ellington, John Coltrane',
    'Aero Chord',
    'Migos',
    'Lil Baby, Gunna',
    'DaBaby',
    'Lil Baby',
    'Lil Yachty',
    'Thomas Rhett',
    'Various Artists',
    'Young Thug',
    'Tyler, The Creator',
    'Calvin Harris',
    'Calvin Harris, Funk Wav',
    '21 Savage, Metro Boomin',
    'Charles Mingus',
    'Billie Eilish',
    'Morgan Wallen'
    ]

special_albums = ['Scary Hours 2', "Birds In The Trap Sing McKnight", "Scorpion", "2014 Forest Hills Drive", "Culture"]
top_a = ['?', 'Boston', 'Hoodie SZN', 'Loose', 'Everybody', 'Confessions of a Dangerous Mind', 'So Much Fun', 'Flower Boy', 'Thats What They All Say', "Die Lit", "Luv Is Rage 2 (Deluxe)", 'Subluxe', 'So Much Fun (Deluxe)', 'The Incredible True Story']
for album in all_time_data:
    if (all_time_data[album]['artists'] in top and all_time_data[album]['name'] not in special_albums) or all_time_data[album]['name'] in top_a:
        # if all_time_data[album]['name'] == 'Graduation':
        #     score = .98
        if all_time_data[album]['name'] == "My Beautiful Dark Twisted Fantasy":
            score = .925
        elif all_time_data[album]['name'] == "To Pimp A Butterfly":
            score = .92
        elif all_time_data[album]['name'] == "JESUS IS KING":
            score = .929
        # elif all_time_data[album]['name'] == 'Sweet Action':
        #     score = .915
        # elif all_time_data[album]['name'] == 'Late Registration':
        #     score = .979
        else:
            score = (len(all_time_data[album]['top_tracks'])*1.5 + len(all_time_data[album]['good_tracks'])*1.25)/(all_time_data[album]['total_tracks']*1.5)
    elif all_time_data[album]['artists'] == 'The Weekend' or all_time_data[album]['artists'] == 'Frank Ocean' or all_time_data[album]['name'] == 'Whole Lotta Red' or all_time_data[album]['name'] == 'Eternal Atake' or all_time_data[album]['name'] == 'Future & Juice WRLD Present... WRLD ON DRUGS' or all_time_data[album]['name'] == "Without Warning" or all_time_data[album]['name'] == "Birds In The Trap Sing McKnight" or all_time_data[album]['name'] == "Scorpion" or all_time_data[album]['name'] == "2014 Forest Hills Drive" or all_time_data[album]['name'] == "Culture" or all_time_data[album]['name'] == "Madvillainy":
        score = (len(all_time_data[album]['top_tracks'])*2 + len(all_time_data[album]['good_tracks'])*1.87)/(all_time_data[album]['total_tracks']*2)
    else:
        score = (len(all_time_data[album]['top_tracks'])*1.4 + len(all_time_data[album]['good_tracks']))/(all_time_data[album]['total_tracks']*1.4)
    all_time_data[album]['score'] = round(score * 10, 2)


with open(f'./data/favorites/music/music_all_time.json', 'w') as json_file: 
    json.dump(all_time_data, json_file, indent=4)


with open(f'./data/favorites/music/music_current.json', 'r') as json_file: 
    all_time_data = json.load(json_file)

for album in all_time_data:
    try:
        if len(all_time_data[album]['tracks']) > 0:
            go = False
        else:
            go = True
    except:
        go = True

    if go:
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