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

    unique_dbs = 2

    f = open('data/archive/last.txt', 'r')
    last_date = f.read()
    f.close()

    f = open('data/archive/last_date.txt', 'r')
    last_date_string = f.read()
    f.close()

    if last_date_string == '':
        last_date_string = date_string_string

    last_date_list = last_date_string.split('/')

    for data_name in data_names:
        # loading data to be backed up into var
        current_file = open(f'data/{data_name}.json', 'r')
        data = json.load(current_file)
        current_file.close()
        if last_date != '':
            current_file = open(f'data/archive/{last_date}/{data_name}.json')
            old_data = json.load(current_file)
            if data == old_data:
                unique_dbs -= 1
            if unique_dbs == 0:
                print('# [no unique data to backup]')
                return 0

    comment_head = f"""
#####################{date_string_string} music backup here#####################
"""
    app =  open('app.py', 'a')
    app.write(comment_head)
    
    os.mkdir(f'data/archive/{date_string}', 0o666)

    for data_name in data_names:
        print(f'# [loading data from {data_name}.json]')
        current_file = open(f'data/{data_name}.json', 'r')
        data = json.load(current_file)
        current_file.close()
        # writing file name
        file_name = data_name

        # writing to backup file
        print(f'# [loading data to {file_name}.json backup]')

        with open(f'data/archive/{date_string}/{file_name}.json', 'w') as backup_file:
            json.dump(data, backup_file, indent=4)

        # creating display data function
        display_data_function = f"""
@app.route("/data/archive/{date_string}/{file_name}.json")
def load_{file_name}():
    f = open('data/archive/{date_string}/{file_name}.json')
    data = json.load(f)
    return data
"""

        # writing that function to app
        print(f'# [writing func to host {file_name}.json to app.py]')
        app =  open('app.py', 'a')
        app.write(display_data_function)

    if last_date_list[0] == today.month:
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
<script type="text/javascript" src="/static/js/current-albums-music.js" data_file="/data/archive/{date_string}/music_current.json"></script>
<script type="text/javascript" src="/static/js/current-tracks-music.js" data_file0="/data/archive/{date_string}/music_current_songs.json"></script>


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

    f = open('data/archive/archive_num.txt', 'r')
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

    f = open('data/archive/last.txt', 'w')
    f.write(date_string)
    f.close()

    f = open('data/archive/archive_num.txt', 'w')
    archive_num += 1
    f.write(str(archive_num))
    f.close()

    f = open('data/archive/last_date.txt', 'w')
    f.write(date_string_string)
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
