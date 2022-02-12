import json

with open(f'./data/favorites/films/movies.json', 'r') as json_file: 
    all_time_data = json.load(json_file)

for movie in all_time_data:
        score = 0
        items = 0
        for s in all_time_data[movie]['scorecard']:
            score += all_time_data[movie]['scorecard'][s]
            items += 1
        if score/items != 10:
            score = round((score + all_time_data[movie]['rating'])/(items + 1), 2)
        else:
            score = round((score/items), 2)
        all_time_data[movie]['asboyer_score'] = score

with open(f'./data/favorites/films/movies.json', 'w') as json_file: 
    json.dump(all_time_data, json_file, indent=4)