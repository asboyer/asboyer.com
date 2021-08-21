from flask import Flask, render_template, send_from_directory
import os, json


app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<page>")
def main_page(page):
    if os.path.exists(f'templates/{page}.html'):
        return render_template(f'{page}.html')
    else:
        return render_template("error.html")

@app.route("/press")
def press():
    return render_template("about/news.html")

# blogs

@app.route("/blog")
def blog():
    return render_template("blog/blog.html")

@app.route("/blog/<name>")
def blog_post(name):
    if name == "1":
        return render_template("soon.html")
    elif os.path.exists(f'templates/blog/{name}.html'):
        return render_template(f"blog/{name}.html")
    else:
        # make error page
        return render_template("error.html")

# favorites

# music
@app.route("/music")
def music():
    return render_template("favorites/music/music.html")

@app.route("/music/<name>")
def music_path(name):
    if os.path.exists(f'templates/favorites/music/{name}.html'):
        return render_template(f"favorites/music/{name}.html")
    else:
        # make error page
        return render_template("error.html")


# movies
@app.route("/movies")
def movies():
    return render_template("favorites/movies/movies.html")

@app.route("/shows")
def shows():
    return render_template("favorites/shows/shows.html")

# archives

@app.route("/archive/music/0")
def music_archive_0():
    return render_template("archive/music/april-june-2021.html")

@app.route("/archive/music/1")
def music_archive_1():
    return render_template("archive/music/july-2021.html")

@app.route("/archive/music/<name>")
def archive_music_path(name):
    if os.path.exists(f'templates/archive/music/{name}.html'):
        return render_template(f"archive/blog/{name}.html")
    else:
        # make error page
        return render_template("error.html")

#SEO
@app.route("/robots.txt")
def se1():
    return send_from_directory(app.root_path, "robots.txt")

@app.route("/sitemap.xml")
def se2():
    return send_from_directory(app.root_path, "sitemap.xml")

@app.route("/data/movies.json")
def movies_json():
    f = open('data/movies.json')
    data = json.load(f)
    return data

@app.route("/data/music_all_time.json")
def music_json():
    f = open('data/music_all_time.json')
    data = json.load(f)
    return data

@app.route("/data/music_current.json")
def music_json_current_albums():
    f = open('data/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/music_current_songs.json")
def music_json_current_tracks():
    f = open('data/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/data/shows.json")
def load_shows():
    f = open('data/shows.json')
    data = json.load(f)
    return data

@app.route('/tests/music')
def test_music():
    return render_template('tests/music.html')


# @app.route("/books")
# def books():
#     return render_template("favorites/books/books.html")

# @app.route("/books/<name>")
# def book_path(name):
#     if os.path.exists(f'templates/favorites/books/{name}.html'):
#         return render_template(f"favorites/books/{name}.html")
#     else:
#         # make error page
#         return render_template("error.html")

# @app.route("/books/shelf")
# def books_shelf():
#     return render_template("favorites/books/bookshelf.html")

# # shelf

# @app.route("/books/shelf/<name>")
# def book_shelf_path(name):
#     if os.path.exists(f'templates/favorites/books/shelf/{name}.html'):
#         return render_template(f"favorites/books/shelf/{name}.html")
#     else:
#         # make error page
#         return render_template("error.html")

# @app.route("/books/library")
# def books_library():
#     return render_template("favorites/books/library.html")

    
@app.route("/data/archive/music_current_8212021.json")
def load_music_current_8212021():
    f = open('data_backup/music_current_8212021.json')
    data = json.load(f)
    return data
        
@app.route("/data/archive/music_current_songs_8212021.json")
def load_music_current_songs_8212021():
    f = open('data_backup/music_current_songs_8212021.json')
    data = json.load(f)
    return data
        
@app.route("/archive/music/8212021")
def music_archive_8212021():
    return render_template("archive/music/8212021.html")
    