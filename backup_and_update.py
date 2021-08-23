# TO DO:
# copy all json files into "data backup dir"

# for music, back up currently listening to and put a timestamp on it, then generate a webpage hosting that data under 'archives'

# ALSO GENERAL TO DO:
"""
Need to figure out a way to seamlessly move all time album into currently listening to
Need to add tv shows under section, perhaps under film
Need to figure out how to write site backup data constantly
Need to figure out how to update the website on launch
Need to write GUI for adding an album, or movie to respective databases
need to write landing page for film, with shows and movies
"""
import json
import os
import sys
from update_movies import update_movies
from update_music import update_music, update_tracks
from update_shows import update_shows
from datetime import datetime

# scan dir with os and get all file name
# for file in data
data_names = ['music_current', 'music_current_songs']

today = datetime.today()
date_string = f'{today.month}{today.day}{today.year}'

def backup_current_music_data():

    unique_dbs = 2

    f = open('data_backup/last.txt', 'r')
    last_date = f.read()

    for data_name in data_names:
        # loading data to be backed up into var
        print(f'# [loading data from {data_name}.json]')
        current_file = open(f'data/{data_name}.json', 'r')
        data = json.load(current_file)
        current_file.close()
        if last_date != '':
            print()
            current_file = open(f'data_backup/{data_name}_{last_date}.json')
            old_data = json.load(current_file)
            if data == old_data:
                unique_dbs -= 1
            if unique_dbs == 0:
                print('no unique data to backup')
                return 0

    for data_name in data_names:
        print(f'# [loading data from {data_name}.json]')
        current_file = open(f'data/{data_name}.json', 'r')
        data = json.load(current_file)
        current_file.close()
        # writing file name
        file_name = f'{data_name}_{ate_string}'

        # writing to backup file
        print(f'# [loading data to {file_name}.json]')

        with open(f'data_backup/{file_name}.json', 'w') as backup_file:
            json.dump(data, backup_file, indent=4)

        # creating display data function
        display_data_function = f"""
@app.route("/data/archive/{file_name}.json")
def load_{file_name}():
    f = open('data_backup/{file_name}.json')
    data = json.load(f)
    return data
        """

        # writing that function to app
        print(f'# [writing func to host {file_name}.json to app.py]')
        app =  open('app.py', 'a')
        app.write(display_data_function)

    # writing the html code
    html_code_top = """
{% extends "layout.html" %}

{% block content %}"""
    html_code_core = f"""
<script type="text/javascript" src="/static/js/current-albums-music.js" data_file="/data/archive/music_current_{date_string}.json"></script>
<script type="text/javascript" src="/static/js/current-tracks-music.js" data_file0="/data/archive/music_current_songs_{date_string}.json"></script>

<section class="my-albums" id="albums">
</section>

<section class="my-songs" id="songs">
</section> 
    """
    html_code_bottom = """
{% endblock %}
    """
    html_code = html_code_top + html_code_core + html_code_bottom
    print(f'# [writing html code to {date_string}.html]')
    html_file = open(f'templates/archive/music/{date_string}.html', 'w')
    html_file.write(html_code)

    render_new_template_function = f"""
@app.route("/archive/music/{date_string}")
def music_archive_{date_string}():
    return render_template("archive/music/{date_string}.html")
    """
    print(f'# [writing py code to render {date_string}.html in app.py]')
    with open('app.py', 'a') as app:
        app.write(render_new_template_function)

    f = open('data_backup/last.txt', 'w')
    f.write(date_string)
    f.close()

def update_all_data():
    update_movies()
    update_music('all')
    update_tracks()
    update_shows()

def update_and_backup():
    backup_current_music_data()
    update_all_data()

if __name__ == "__main__":
    update_and_backup()
