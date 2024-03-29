# ALSO GENERAL TO DO:
"""
Need to write GUI for adding an album, or movie to respective databases
need to write landing page for film, with shows and movies
"""
import json
import os
import sys
import calendar
from update_movies import update_movies
from update_music import update_music, update_tracks
from update_shows import update_shows
from datetime import datetime

# scan dir with os and get all file name
# for file in data
data_names = ['music_current', 'music_current_songs']


today = datetime.today()
date_string = f'{today.month}{today.day}{today.year}'
date_string_string = f'{today.month}/{today.day}/{today.year}'

def backup_current_music_data():
    total_albums = 0
    avg_score = 0
    total_tracks = 0
    total_score = 0
    top_3_albums = []
    unique_dbs = 2
    top_3_string = ""

    f = open('./data/archive/music/last.txt', 'r')
    last_date = f.read()
    f.close()

    f = open('./data/archive/music/last_date.txt', 'r')
    last_date_string = f.read()
    f.close()

    if last_date_string == '':
        last_date_string = date_string_string

    last_date_list = last_date_string.split('/')

    for data_name in data_names:
        # loading data to be backed up into var
        current_file = open(f'./data/favorites/music/{data_name}.json', 'r')
        data = json.load(current_file)
        current_file.close()
        if last_date != '':
            current_file = open(f'./data/archive/music/{last_date}/{data_name}.json', 'r')
            old_data = json.load(current_file)
            if data == old_data:
                unique_dbs -= 1
            if unique_dbs == 0:
                print('# [no unique data to backup]')
                return 0
        for d in data:
            if data_name == "music_current":
                total_tracks += len(data[d]["top_tracks"])
                total_albums += 1
                total_score += data[d]['score']
                top_3_albums.append([data[d]['name'], data[d]['score'], data[d]['artists']])
            else:
                total_tracks += 1
        avg_score = round(total_score/total_albums, 2)
        top_3_albums = sorted(top_3_albums, key=lambda x: x[1])
        top_3_albums.reverse()
        for i in range(0, 3):
            top_3_string += f"{i + 1}: {top_3_albums[i][0]} by {top_3_albums[i][2]}\n"
    comment_head = f"""
#####################{date_string_string} music backup here#####################
"""
    app =  open('app.py', 'a')
    app.write(comment_head)
    
    if sys.platform.startswith('win32'):
        os.mkdir(f'./data/archive/music/{date_string}', 0o666)
    else:
        os.mkdir(f'./data/archive/music/{date_string}')

    for data_name in data_names:
        print(f'# [loading data from {data_name}.json]')
        current_file = open(f'./data/favorites/music/{data_name}.json', 'r')
        data = json.load(current_file)
        current_file.close()
        # writing file name
        file_name = data_name

        # writing to backup file
        print(f'# [loading data to {file_name}.json backup]')

        with open(f'./data/archive/music/{date_string}/{file_name}.json', 'w') as backup_file:
            json.dump(data, backup_file, indent=4)

        # creating display data function
        display_data_function = f"""
@app.route("/data/archive/music/{date_string}/{file_name}.json")
def load_{file_name}_{date_string}():
    f = open('data/archive/music/{date_string}/{file_name}.json')
    data = json.load(f)
    return data
"""

        # writing that function to app
        print(f'# [writing func to host {file_name}.json to app.py]')
        app =  open('app.py', 'a')
        app.write(display_data_function)

    if int(last_date_list[0]) == today.month:
        date_range_string = f'{calendar.month_name[today.month]} {today.year}'
    elif int(last_date_list[2]) != today.year:
        date_range_string = f'{calendar.month_name[int(last_date_list[0])]} {last_date_list[2]} - {calendar.month_name[today.month]} {today.year}'
    else:
        date_range_string = f'{calendar.month_name[int(last_date_list[0])]} - {calendar.month_name[today.month]} {today.year}'
    # writing the html code
    html_code_top = """
{% extends "layout.html" %}

{% block content %}"""
    html_code_core = f"""
<script type="text/javascript" src="/static/js/favorites/music/current-albums-music.js" data_file="/data/archive/music/{date_string}/music_current.json"></script>
<script type="text/javascript" src="/static/js/favorites/music/current-tracks-music.js" data_file0="/data/archive/music/{date_string}/music_current_songs.json"></script>

<style>
#describe {"{"}
    color: #B6F29D;
    margin: 0px;
    font-family: monospace;
    background: #111;
    font-size: 15px;
{"}"}
</style>

<section class="my-albums" id="albums">
<div class="title-music">
    <p class="section__subtitle section__subtitle--books">{date_range_string}</p>

</div>
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

    f = open('./data/archive/music/archive_num.txt', 'r')
    archive_num = int(f.read())
    f.close()

    render_new_template_function = f"""
@app.route("/archive/music/{archive_num}")
def music_archive_{date_string}():

    return render_template("archive/music/{date_string}.html")
    """
    print(f'# [writing py code to render {date_string}.html in app.py]')
    with open('app.py', 'a') as app:
        app.write(render_new_template_function)

    f = open('./data/archive/music/last.txt', 'w')
    f.write(date_string)
    f.close()

    f = open('./data/archive/music/archive_num.txt', 'w')
    archive_num += 1
    f.write(str(archive_num))
    f.close()

    f = open('./data/archive/music/last_date.txt', 'w')
    f.write(date_string_string)
    f.close()

    f = open('./update_message.txt', 'w')
    f.write(f"""New asboyer.com music reviews!

Check out what I've been listening to during {date_range_string}:

total_tracks = {total_tracks}
total_albums = {total_albums}
avg_score = {avg_score}

top_3_albums:
{top_3_string}

https://asboyer.com/archive/music/{archive_num - 1}

- asboyer
""")
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
    backup_current_music_data()
    update_all_data()
