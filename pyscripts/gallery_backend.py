import json
import os
from datetime import datetime
def add_img():
    with open(f'./data/gallery/pics.json', 'r') as json_file:  
        data = json.load(json_file)
    in_dir = os.listdir('./static/img/gallery')
    in_data = data.keys()
    if in_dir == in_data:
        return
    to_add = list(set(in_dir) - set(in_data))
    to_remove = list(set(in_data) - set(in_dir))
    for f in to_add:
        print(f'adding {f}...')
        data[f] = {
            "name": f,
            "link": '',
            "caption": '',
            "date": datetime.now().strftime('%Y-%m-%d')
        }
    for f in to_remove:
        del data[f]

    with open(f'./data/gallery/pics.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)