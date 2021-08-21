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
from update_movies import update_movies
from update_music import update_music, update_tracks
from update_shows import update_shows
from datetime import datetime

# scan dir with os and get all file name
# for file in data
data_names = ['music_current', 'music_current_songs']

today = datetime.today()
date_string = f'{today.month}/{today.day}/{today.year}'

def backup_current_music_data()
    for data_name in data_names:
        # loading data to be backed up into var
        print(f'# [loading data from {data_name}.json]')
        current_file = open(f'{data_name}.json', 'r')
        data = json.load(current_file)
        current_file.close()

        # writing file name
        file_name = f'{data_name}_{date_string}'

        # writing to backup file
        print(f'# [loading data to {file_name}.json]')
        with open(file_name, 'w') as backup_file:
            json.dump(data, backup_file, indent=4)

        # creating display data function
        display_data_function = f"""
        @app.route("/data/archive/{file_name}.json")
        def load_{file_name}():
            f = open('data/data_backup/{file_name}.json')
            data = json.load(f)
            return data
        """

        # writing that function to app
        print(f'# [writing func to host {file_name}.json to app.py]')
        with open('app.py', 'a') as app:
            app.write(display_data_function)

    # writing the html code
    html_code_top = """
    {% extends "layout.html" %}

    {% block content %}
    """
    html_code_core = f"""
    <script type="text/javascript" src="/static/js/archive/music/{date_string}/current-albums-{date_string}.js"></script>
    <script type="text/javascript" src="/static/js/archive/music/{date_string}/current-tracks-{date_string}.js"></script>

    <section class="my-albums" id="albums">
    </section>

    <section class="my-songs" id="songs">
    </section> 
    """
    html_code_bottom = """
    {% endblock %}
    """
    html_code = html_code_top + html_code_core + html_code_top
    print(f'# [writing html code to {date_string}.html]')
    with open(f'templates/archive/music/{date_string}.html', 'w') as html_file:
        html_file.write(html_code)

    render_new_template_function = f"""
    @app.route("/archive/music/{date_string}")
    def music_archive_{date_string}():
        return render_template("archive/music/{date_string}.html")
    """
    print(f'# [writing py code to render {date_string}.html in app.py]')
    with open('app.py', 'a') as app:
        app.write(render_new_template_function)

    # writing the js code var
    js_code_albums = """
    $(document).ready(function(){

        var music_div = `
        <div class="albums">
        `
        $.getJSON("/data/music_current_{0}.json", function(json) {
            $.each(json, function(title, values){
                var tracklist = ""
                var styles = ""
                if(title == "From Me To You") {
                    tracklist += '-long'
                }
                // make an array of these albums for nowarp, same with small font

                var album_div = 
                `<div class="album__container">
                <a href="https://open.spotify.com/album/${values.id}" class="album__item">
                    <img src="${values.image}" alt="${title}" class="portfolio__img">
                <div class="album_overlay">
                    <div class="album-text">
                        <p class="title" style="${styles}">${title.replace("(Deluxe)", "").replace("(Remastered)", "").replace("(Original Motion Picture Soundtrack)", "").replace("(Legacy Edition)", "").replace(" (Platinum VIP Edition)", "").replace(" [Deluxe Edition]", "")}</p>
                        <p class="artist">${values.artists}</p>
                        <div class="the-tracks">
                            <ul class="tracklist${tracklist}">
                            <li class="tracks${tracklist}">Top Tracks:</li>
                `
                var track_list = ''
                for (let i = 0; i < values.top_tracks.length; i++) {
                    track_list += `
                                <li>${values.top_tracks[i]}</li>
                                `
                }
                var album_div_end = `
                            </ul>
                        </div>
                    </div>
                </div>
                </a>
            </div>
            `
            
            music_div = music_div + album_div + track_list + album_div_end
            });
            music_div = music_div + `
            </div>
            `
            $('#albums').append(music_div)

        });

    });

    """.format(0=f'{date_string}')

    # making the date dir in js dir
    os.mkdir(f"/static/js/archive/music/{date_string}")

    print(f'# [writing js code to /static/js/archive/music/{date_string}/current-albums-{date_string}.js]')
    # writing the js code for albums to file
    with open(f"/static/js/archive/music/{date_string}/current-albums-{date_string}.js", "w") as js_albums:
        js_albums.write(js_code_albums)

    # writing the js code for tracks
    js_code_tracks = """
    $(document).ready(function(){

        var music_div = `
        <div class="songs">
        `
        $.getJSON("/data/music_current_songs_{0}.json", function(json) {
            $.each(json, function(title, values){
                var styles = ""
                // make an array of these albums for nowarp, same with small font

                var album_div = 
                ` 
                <div class="song__container">
                    <a href="https://open.spotify.com/track/${values.id}" class="song__item">
                        <img src="${values.image}" alt="${title}" class="portfolio__img">
                    <div class="song_overlay">
                        <div class="album-text">
                            <p class="song-title" style="${style}">${title}</p>
                            <p class="song-artist">${values.artist}</p>
                        </div>
                    </div>
                    </a>
                </div>
            </div>
            `
            music_div += album_div
            $('#songs').append(music_div)

        });

    });
    """
    print(f'# [writing js code to /static/js/archive/music/{date_string}/current-tracks-{date_string}.js]')
    # writing the js code for tracks to file
    with open(f"/static/js/archive/music/{date_string}/current-tracks-{date_string}.js", "w") as js_tracks:
        js_tracks.write(js_code_tracks)

def update_all_data()
    # update all data here
    pass

if __name__ == "__main__":
    backup_current_music_data()
